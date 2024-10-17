import random


words = ["fortnite", 
        "sigma", 
        "skibiti", 
        "fanum", 
        "roblox", 
        "tacobell", 
        "fullboxed", 
        "whatthesigma", 
        "rizzler",
        "coding"]


def get_guess(previous_guesses, random_word, guess, letter):
    letter = random_word.find(guess)
    while True:
        user_guess = input("Guess the word that is blanked out: ") #get a guess from the user
        if user_guess == letter and user_guess != previous_guesses: #if the guess is a letter and not in the previous list
            return start_game(user_guess) #return the guess
        


def print_gallows(strikes):
    if strikes == 0:
        print(" ________")
        print(" |/     |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
        return start_game()
    elif strikes == 1:
        print(" _______")
        print(" |/    |")
        print(" |    (_)")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
        return start_game()
    elif strikes == 2:
        print(" _______")
        print(" |/    |")
        print(" |    (_)")
        print(" |     |")
        print(" |     |")
        print(" |")
        print(" |")
        print("_|___")
        return start_game()
    elif strikes == 3:
        print(" _______")
        print(" |/    |")
        print(" |    (_)")
        print(" |    \|")
        print(" |     |")
        print(" |")
        print(" |")
        print("_|___")
        return start_game()
    elif strikes == 4:
        print(" _______")
        print(" |/    |")
        print(" |    (_)")
        print(" |    \|/")
        print(" |     |")
        print(" |")
        print(" |")
        print("_|___")
        return start_game()
    elif strikes == 5:
        print(" _______")
        print(" |/    |")
        print(" |    (_)")
        print(" |    \|/")
        print(" |     |")
        print(" |    /")
        print(" |")
        print("_|___")
        return start_game()
    elif strikes == 6:
        print(" _______")
        print(" |/    |")
        print(" |    (_)")
        print(" |    \|/")
        print(" |     |")
        print(" |    / \ ")
        print(" |")
        print("_|___")
        return start_game()


def start_game(words, lettter, user_guess) -> None:
    strikes = 0
    previous_guesses = []
    while strikes < 6:
        random_word = random.choice(list(words))
        length = len(random_word)
        print("_" * length)
        
        #check if the full word has been guessed and break out if it was
        
        guess = get_guess(previous_guesses, random_word, guess)
        previous_guesses.append(guess) #add guess to previous_guesses
        if guess != len(random_word): #if guess is not in word, add 1 to strikes
            strikes + 1
            print(f"Wrong guess. You have {strikes} strikes")
        #if previous_guesses contains all letters in the word, print you won
        
        strikes += 1
    if strikes >= 6:
        print("You lost")
    else:
        print("You guessed the word!")


def play_game():
    while True:
        print("Welcome to hangman! \nWould you like to play?")
        print("1. Yes")
        print("2. No")
        user_choice = input("Enter your choice (1 or 2): ")
        
        if user_choice == "1":
            start_game(words)
        elif user_choice == "2":
            print("Goodbye.")
            exit()
        else:
            print("Invalid response, try again")
        return play_game()


if __name__ == '__main__':
    play_game()


#letter = random_word.find(guess)
