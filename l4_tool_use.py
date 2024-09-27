# flake8: noqa: 266
import chess
import chess.svg
from pprint import pprint
from autogen import ConversableAgent, register_function, gather_usage_summary

# from IPython import display
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cairosvg
import io
from typing_extensions import Annotated
from llm import get_llm_config

# The lesson used GPT-4 Turbo as "it's a better player than GPT-3.5", let's see how 4o-Mini does
llm_config = get_llm_config()
# Disabling LLM caching to avoid loops, also since the game is dyanmic caching doesn't make sense
llm_config["cache_seed"] = None

## Init chess board

board = chess.Board()
made_move = False


def did_make_move(msg):
    global made_move
    if made_move:
        made_move = False
        return True
    else:
        return False


def display_board(board, move):
    svg = chess.svg.board(
        board,
        arrows=[(move.from_square, move.to_square)],
        fill={move.from_square: "gray"},
        size=200,
    )
    png_data = cairosvg.svg2png(bytestring=svg.encode("utf-8"))
    img = mpimg.imread(io.BytesIO(png_data), format="png")
    plt.imshow(img)
    plt.axis("off")
    plt.pause(0.1)
    plt.clf()


## Tools


def get_legal_moves() -> Annotated[str, "A list of legal moves in UCI format"]:
    if board.legal_moves.count() == 0:
        # This global state stinks a bit, would look at some better state management and separation of concerns
        global made_move
        made_move = True
        return "You won!"
    return "Possible moves are: " + ",".join([str(move) for move in board.legal_moves])


def make_move(
    # Using Annotated[] to describe for agents the params, latter they will expect and use descriptions from Annotated
    move: Annotated[str, "A move in UCI format."]
) -> Annotated[str, "Result of the move."]:
    move = chess.Move.from_uci(move)
    board.push_uci(str(move))
    global made_move
    made_move = True

    # # Display the board.
    # display(
    #     chess.svg.board(
    #         board,
    #         arrows=[(move.from_square, move.to_square)],
    #         fill={move.from_square: "gray"},
    #         size=200,
    #     )
    # )

    # Using matplotlib instead to animate moves in a single popup window
    display_board(board, move)

    # Describing the move just made to return as string
    piece = board.piece_at(move.to_square)
    piece_symbol = piece.unicode_symbol()
    piece_name = (
        chess.piece_name(piece.piece_type).capitalize()
        if piece_symbol.isupper()
        else chess.piece_name(piece.piece_type)
    )
    return (
        f"Moved {piece_name} ({piece_symbol}) from "
        f"{chess.SQUARE_NAMES[move.from_square]} to "
        f"{chess.SQUARE_NAMES[move.to_square]}."
    )


## Agents

# Again, need to fix names and removed spaces to avoid OpenAI API errors
player_white = ConversableAgent(
    name="Player_White",
    system_message="You are a professional chess player and you play as white. "
    "First call get_legal_moves(), to get a list of legal moves. "
    "Then call make_move(move) to make a move. ",
    llm_config=llm_config,
)

player_black = ConversableAgent(
    name="Player_Black",
    system_message="You are a beginner chess player and you play as black. "
    # Used this to try out failover - behavrious in case wrong move is selected
    # "You are a poor chess player who barely knows the rules and you tend to make wrong moves that are not allowed. Do not pick allowed moves, make up your wrong moves"
    # Used this to give advantage to another player and test the completion of the game sooner
    "Although you know well the rules you are bad at chess and lose quickly. "
    "First call get_legal_moves(), to get a list of legal moves. "
    "Then call make_move(move) to make a move. ",
    llm_config=llm_config,
    # The original code didn't have any termination conditions for check-mate
    # It still felt like termination condition should be part of chat (activityi, task), not agent (which can be engaged in multiple chats),
    # though since there's no such instance as Chat, only ChatResult and each agent essentially wraps the dialog - the agent is LLMs scroll of dialogs
    # not a separate entity
    is_termination_msg=lambda msg: "you won" in msg["content"].lower(),
)

board_proxy = ConversableAgent(
    name="Board_Proxy",
    llm_config=False,
    # Stop nested chat (defined below) right after there's a tool call that makes a move OR if the player doesn;t have any moves available (lost)
    is_termination_msg=did_make_move,
    human_input_mode="NEVER",
)

## Register tools

for caller in [player_white, player_black]:
    # Yet another example of poor naming/convernstions, it is now generally accepted to use tools, not functions
    # (even OpenAI API have moved to tool call instead of now deprioctaed function call)
    register_function(
        get_legal_moves,
        caller=caller,
        executor=board_proxy,
        name="get_legal_moves",
        description="Get legal moves.",
    )

    register_function(
        make_move,
        caller=caller,
        executor=board_proxy,
        name="make_move",
        # Would be handy to have this as part of function definition in a similar way as annotated params,
        # e.g. using a custom decorator
        #  def tool_description(description):
        #     def decorator(func):
        #         func.__description__ = description
        #         return func
        #     return decorator
        #
        # @tool_description("Returns a string listing all possible legal moves in UCI format.")
        # def get_legal_moves() -> Annotated[str, "A list of legal moves in UCI format"]:
        #     return "Possible moves are: " + ",".join([str(move) for move in board.legal_moves])
        description="Call this tool to make a move.",
    )

# View tools registered with the agent, they are automatically converted to OpenAI format
pprint(player_black.llm_config["tools"])

## Nested Chats
# Each player will initiate a nested chat with baord proxy before responding to the other player
# in order to get all moves that are possible, make a move (via registered tools)
# and verify the next move is legit (the Termination condition of check-mate is not achieved)

player_white.register_nested_chats(
    trigger=player_black,
    chat_queue=[
        {
            "sender": board_proxy,
            "recipient": player_white,
            "summary_method": "last_msg",
        }
    ],
)

player_black.register_nested_chats(
    trigger=player_white,
    # In lesson 3 this param was used without name as the first one passed in
    chat_queue=[
        {
            "sender": board_proxy,
            "recipient": player_black,
            "summary_method": "last_msg",
        }
    ],
)

## The Game

chat_result = player_black.initiate_chat(
    player_white,
    message="Let's play chess! Your move.",
    max_turns=100,
)

print(f"\n\n\n Completed game\n{chat_result.cost} \n\n")
print(f"Number of turns taken: {len(chat_result.chat_history)/2}")
print("\nCosts per agent:\n")
pprint(gather_usage_summary([player_white]))
pprint(gather_usage_summary([player_black]))
# Note that proxy has 0 consumption as it has one fixed message (list of tools) andf also makes tool calls and provides results
pprint(gather_usage_summary([board_proxy]))
# 20 turns, stats, not sure about caching, but seems that not pruning chat history might exhaust the context very quickly
# {'usage_including_cached_inference': {'total_cost': 0.006281999999999998, 'gpt-4o-mini': {'cost': 0.006281999999999998, 'prompt_tokens': 31436, 'completion_tokens': 2611, 'total_tokens': 34047}}, 'usage_excluding_cached_inference': {'total_cost': 0.0023118, 'gpt-4o-mini': {'cost': 0.0023118, 'prompt_tokens': 11944, 'completion_tokens': 867, 'total_tokens': 12811}}}
# 100 turns
# {'usage_including_cached_inference': {'total_cost': 0.02926995000000001, 'gpt-4o-mini': {'cost': 0.02926995000000001, 'prompt_tokens': 144953, 'completion_tokens': 12545, 'total_tokens': 157498}}, 'usage_excluding_cached_inference': {'total_cost': 0.02298795000000002, 'gpt-4o-mini': {'cost': 0.02298795000000002, 'prompt_tokens': 113517, 'completion_tokens': 9934, 'total_tokens': 123451}}}
# pprint(chat_result.chat_history)


input("Press any key to continue...")

## Adding chit-chat

# Redefining agents with new system prompts
player_white = ConversableAgent(
    name="Player White",
    system_message="You are a chess player and you play as white. "
    "First call get_legal_moves(), to get a list of legal moves. "
    "Then call make_move(move) to make a move. "
    "After a move is made, chitchat to make the game fun.",
    llm_config=llm_config,
)

player_black = ConversableAgent(
    name="Player Black",
    system_message="You are a chess player and you play as black. "
    "First call get_legal_moves(), to get a list of legal moves. "
    "Then call make_move(move) to make a move. "
    "After a move is made, chitchat to make the game fun.",
    llm_config=llm_config,
)

for caller in [player_white, player_black]:
    register_function(
        get_legal_moves,
        caller=caller,
        executor=board_proxy,
        name="get_legal_moves",
        description="Get legal moves.",
    )

    register_function(
        make_move,
        caller=caller,
        executor=board_proxy,
        name="make_move",
        description="Call this tool to make a move.",
    )

player_white.register_nested_chats(
    trigger=player_black,
    chat_queue=[
        {
            "sender": board_proxy,
            "recipient": player_white,
            "summary_method": "last_msg",
            "silent": True,
        }
    ],
)

player_black.register_nested_chats(
    trigger=player_white,
    chat_queue=[
        {
            "sender": board_proxy,
            "recipient": player_black,
            "summary_method": "last_msg",
            # Do not show the player to baord dialog, only show top level dialog between players
            "silent": True,
        }
    ],
)

board = chess.Board()

chat_result = player_black.initiate_chat(
    player_white,
    message="Let's play chess! Your move.",
    max_turns=2,
)

## Notes
# Not a chess expert, but 100 turns was not enough to complete the game and even with one agent (Player White) given advantage
# This again emphasizes how Gen AI tools are good to start smth and bad to finish. The controversy about Gen AI utility
# is demonstrated here as even the basic example of chess player was not supposed to complete a game, after 100 turns and 45k total tokens
# the LLMs ended up randomly moving figures across the board. After spending couple of hours nudging the LLMs to complete the game
# I saw no reason to proceed - it is not he versatility and top notch performance one might expect from the might LLMs (the consequencies of GenAI hype)
#
# It doesn't seem there's any awareness of the board, showing the current placement of figures, what LLMs know is the history of moves,
# to better play cheess agent can engage in nested chat's inner monolog with a tool giving the current board layout and letting the LLM decide
# where to move next, this can also save on chat tokens.
#
# What would happen if an LLM offers a move that can't be done (it haluscinates)?
# There will be an erorr in tool call, the erorr (e.g. "***** Response from calling tool (call_SCxb3KB2xVxNrGuU7oBMeoEd) *****Error: illegal uci: 'h8g8' in rnbqkNr1/pppp1pp1/4p2n/8/8/8/PPPPPPPP/RNBQKB1R b KQq - 0 4")
# will be relayed back to the player and it will attempt to make another move.
# Nested chats server the purpose of guardrails, tin the first message from player to board proxy the player askes for a tool call (show possible moves) and then picks one of the allowed ones. Yet
# it also demonstrates that LLMs own knowledge of rules and ability to control the board is questioned - the mighty LLM is treated as some retard not knowing/not capable
# of chase moves on it's own
