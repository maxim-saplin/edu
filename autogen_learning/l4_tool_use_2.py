# flake8: noqa: 266
# This one made a full game with white winning in 62 turns
# Change the original version to clear the nested chat history and provide there a repreenttion of a chess board
# positions of all pieces
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
        global made_move
        made_move = True
        return "You won!"
    return "Possible moves are: " + ",".join([str(move) for move in board.legal_moves])


def get_current_board() -> (
    Annotated[str, "A text representation of the current board state"]
):
    return board.unicode()


def make_move(
    move: Annotated[str, "A move in UCI format."]
) -> Annotated[str, "Result of the move."]:
    move = chess.Move.from_uci(move)
    board.push_uci(str(move))
    global made_move
    made_move = True

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

player_white = ConversableAgent(
    name="Player_White",
    # Quite rigid, having all tool calls specified in specific order...
    system_message="You are a professional chess player and you play as white. "
    "First call get_current_board(). "
    "Next call get_legal_moves(), to get a list of legal moves. "
    "Then call make_move(move) to make a move. ",
    llm_config=llm_config,
)

player_black = ConversableAgent(
    name="Player_Black",
    system_message="You are a beginner chess player and you play as black. "
    "Although you know well the rules you are bad at chess and lose quickly. "
    "First call get_current_board(). "
    "Next call get_legal_moves(), to get a list of legal moves. "
    "Then call make_move(move) to make a move. ",
    llm_config=llm_config,
    is_termination_msg=lambda msg: "you won" in msg["content"].lower(),
)

board_proxy = ConversableAgent(
    name="Board_Proxy",
    llm_config=False,
    is_termination_msg=did_make_move,
    human_input_mode="NEVER",
)

## Register tools

for caller in [player_white, player_black]:

    register_function(
        get_current_board,
        caller=caller,
        executor=board_proxy,
        name="get_current_board",
        description="Get current state of the board.",
    )

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

pprint(player_black.llm_config["tools"])

## Nested Chats

player_white.register_nested_chats(
    trigger=player_black,
    chat_queue=[
        {
            "sender": board_proxy,
            "recipient": player_white,
            "summary_method": "last_msg",
            "clear_history": True,
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
            "clear_history": True,
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
pprint(gather_usage_summary([board_proxy]))

input("Press any key to continue...")

# {'usage_including_cached_inference': {'total_cost': 0.03302040000000003, 'gpt-4o-mini': {'cost': 0.03302040000000003, 'prompt_tokens': 187384, 'completion_tokens': 8188, 'total_tokens': 195572}}, 'usage_excluding_cached_inference': {'total_cost': 0.03302040000000003, 'gpt-4o-mini': {'cost': 0.03302040000000003, 'prompt_tokens': 187384, 'completion_tokens': 8188, 'total_tokens': 195572}}}

# Number of turns taken: 62.0
