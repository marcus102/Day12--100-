import random
from art import logo

print(logo)

max_attempt = 10
final_attempt = 0

correct_answer = random.randint(1,100)

print("Welcome to the Number Guessing Game!")

game_level=input( """
I'm thinking of a number betweem 1 to 100.
Choose a difficulty. Type 'easy' or 'hard': """ )

if game_level == 'easy':
    max_attempt
else:
    max_attempt -= 5
print(f"You have {max_attempt} remaining to guess the number")

while final_attempt != max_attempt:
    
    max_attempt -= 1
    number_guessed = int(input("Make a guess: "))
    if number_guessed == correct_answer:
        print(f"You got it! The answer was {correct_answer} ")
        final_attempt = max_attempt
    else:
        if number_guessed < correct_answer:
            if max_attempt ==0 :
                print("You've run out of guess, you lose!")
            else:
                print("Too low.\nGuess again: ")
                print(f"You have {max_attempt} remaining to guess the number") 
                
        elif number_guessed > correct_answer:
            if max_attempt ==0 :
                print("You've run out of guess, you lose!")
            else:
                print("Too high.\nGuess again: ")
                print(f"You have {max_attempt} remaining to guess the number") 
                    