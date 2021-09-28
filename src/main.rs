use rand::prelude::*;
use std::io;

fn main() {
    guess_game();
}

fn guess_game() {
    let secret_number = rand::thread_rng().gen_range(1..101);

    println!("I'm thinking of a number between 1 and 100...");
    println!("Guess the number:");
    loop {
        let mut guess = String::new();
        if io::stdin().read_line(&mut guess).is_err() {
            println!("Wrong input, try again...");
            continue;
        }

        let guess: u32 = match guess.trim().parse() {
            Ok(v) => v,
            Err(_) => {
                println!("Wrong input, try again...");
                continue;
            }
        };

        if guess > secret_number {
            println!("\n{} is too high! Guess lower:", guess);
        } else if guess < secret_number {
            println!("\n{} is too low! Guess higher:", guess);
        } else {
            println!("\nYou got it! The secret number was {}.", secret_number);
            break;
        }
    }
}
