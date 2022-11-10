
import numpy as np
num = np.random.randint(1,101)
game_guess = 7
total_guesses = 0
chances = game_guess
has_cheats = False
guess = 1200
def print_banner():

    print("""
    ________00000000000___________000000000000_________
    ______00000000_____00000___000000_____0000000______
    ____0000000_____________000______________00000_____
    ___0000000_______________0_________________0000____
    __000000____________________________________0000___
    __00000_____________________________________ 0000__
    _00000______________________________________00000__
    _00000_____________________________________000000__
    __000000_________________________________0000000___
    ___0000000______________________________0000000____
    _____000000____________________________000000______
    _______000000________________________000000________
    __________00000_____________________0000___________
    _____________0000_________________0000_____________
    _______________0000_____________000________________
    _________________000_________000___________________
    _________________ __000_____00_____________________
    ______________________00__00_______________________
    ________________________00_________________________
    """)
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
        print_banner()
        quit()
    while int(guess) != num and total_guesses < chances:
        if has_cheats == "2 lov":
            num = np.random.randint(1,101)
        guess = input()
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

