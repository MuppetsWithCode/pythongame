
import numpy as np
num = np.random.randint(1,101)
game_guess = 7
total_guesses = 0
chances = game_guess
has_cheats = False
guess = 1200
cheats = input("Any codes?")
if cheats == "Muppet Man 3001":
    has_cheats = "True"
elif cheats == "MOONIE DA BEST":
    has_cheats = "2 lov"
else:
    print("ok")
print("Guess the number in as few guesses as possible")
while total_guesses < chances or total_guesses == chances and int(guess) == num:
    chances = game_guess
    if has_cheats == "True":
        print(num)
    if game_guess == 0:
        print("Wow, you won the entire game!")
        quit()
    while int(guess) != num and total_guesses < chances:
        if has_cheats == "2 lov":
            num = np.random.randint(1,101)
        guess = input()
        if guess == "quit"
            quit()
        total_guesses += 1
        if int(guess) > num and total_guesses < chances:
            print("Your guess was too high")
        if int(guess) < num and total_guesses < chances:
            print("Your guess was too low")
        grumm = chances-total_guesses
        if int(guess) != num and total_guesses < chances:
            print(f"You have {grumm} guesses left")
    if int(guess) == num:
        print(f"""You win! You got it in {total_guesses} guesses""")
    if total_guesses == chances and int(guess) != num and game_guess != 0:
        print(f"""You lose, the number was {num}. You survived {8-game_guess} rounds.""")
        quit()
    if total_guesses < chances or total_guesses == chances and int(guess) == num:
        num = np.random.randint(1,101)
        game_guess -= 1
        total_guesses = 0
        print(f"Now you have {game_guess} guesses to try to win!")

