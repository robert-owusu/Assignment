print("Welcome to Aura lottery Enterprise\nDear Valued customer, you stand a chance of winning GHC 5000 if you guess the token number correctly\n* INSTRUCTIONS *\n Choose a number between 1 and 99, a clue is provided for you and note that only 10 attempts will be accepted, any further attempts shall be considered invalid.")
print("* CLUE *\nI am a number, obtained by multiplying (the number for perfection) with a (prime number)\nWhat number am i?\n")

Correct_Number = 21
Guess = int(input("Guess a number between 1 and 99: "))
while Guess != Correct_Number:
    if Guess < Correct_Number:
        print("you need to guess higher, Try again")
        Guess = int(input("\nGuess a number between 1 and 99: "))
    if Guess > Correct_Number:
        print("you need to guess lower, Try again")
        Guess = int(input("\nGuess a number between 1 and 99: "))

print("Congratulations, You guessed the number correctly")
