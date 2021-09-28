#![allow(dead_code)] // crate or file (not sure) level ignore

use rand::prelude::*;
use std::io;
use std::env;
use std::fs;
use std::collections::HashMap; // HashMap is not part of std prelude
use std::iter::FromIterator;

fn main() {
    count_words();
    //vectors();
    //guess_game();
}

fn count_words() {
    

    if env::args().len() != 2 {
        println!("File name must be provided. Terminating...");
        return;
    }

    let file_name = env::args().nth(1).unwrap();
    println!("Reading file {} and counting words...", file_name);

    let file = match fs::read_to_string(file_name) {
        Ok(v) => v,
        Err(_) => {
            println!("Can't read file. Terminating...");
            return;
        }
    };

    let mut words = HashMap::<String, i32>::new();
    let mut total = 0;

    for word in file.split_whitespace() {
        let w = word.to_lowercase();
        let kv = words.entry(w).or_insert(0);
        *kv += 1;
        total += 1;
    }

    println!("Counted {} total words and {} unique words. \n Top 10 words by frequency:", total, words.len());
    
   
    let mut sorted = Vec::from_iter(words);
    sorted.sort_by(|&(_, a), &(_, b)| b.cmp(&a));

    let mut i = 0;

    for (word, count) in sorted {
        println!("{} : {}", word, count);
        i += 1;
        if i > 9 {break}
    }
}

fn vectors() {
    let mut strings = Vec::<Option<String>>::new(); // use Option to allow None values

    strings.push(Option::Some("One".to_string()));
    strings.push(Option::Some("Two".to_string()));
    strings.push(Option::None);
    strings.push(Option::Some("Three".to_string()));
    //strings.push(None);

    let two = (&strings.get(1).unwrap().as_ref()).unwrap();
    println!("Two: {}", two);

    println!("Length: {}", strings.len());
    let last = strings.pop().unwrap().unwrap();
    println!("Last: {}, Length: {}", last, strings.len());

    let last = strings.pop().unwrap();
    println!("Last: {:?}, Length: {}", last, strings.len());

    let countdown = vec![5, 4, 3, 2, 1];
    println!("");
    for i  in countdown {
        print!("{}", i);
    }
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
