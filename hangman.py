import random
from collections import defaultdict

player_names = []
player_scores = []
# word_to_guess = None
letters_missed = []

def players():
    print("----------------------")
    print("Welcome to Hangman!")
    print("----------------------") 

    while(True):
        try:
            players = int(input("\nHow many players are going to play?")) 
        except ValueError:
            print("That's not a number. Please input a number")
            continue
        else:
            print()
            break
            
    add_player_to_list(players)

    more_players = None

    while(True):
        more_players = input("\nThere are currently " + str(players) + " players. Is that correct? (Yes/No) ").lower()
        
        if (more_players != "yes" and more_players != "no"):
            print("Wrong input. Please input yes or no")
        elif (more_players == "no"): 
            how_many = int(input("How many more players will join? "))
            add_player_to_list(how_many)
            break
        elif (more_players == "yes"):
            break

    print_player_names(len(player_names))
    hangman()
    # print("The current players are: {}".format(player_names))
    
def hangman():
    word_to_guess = random_words()
    print("Word to guess: {}" .format(word_to_guess))
    word_length = len(word_to_guess)
    guess = ['_' for i in range(word_length)]
    lives = 6
    flag = None
    number_of_players = len(player_names)
    current_player = 0

    print("====================================================")
    print("\nLet us begin the game!")
    print("You will have 6 lives as a group to guess the word.")
    print("The current word is {} letters long\n" .format(word_length))
    
    while(True):        
        check_win_condition(lives, guess, word_to_guess)

        print("Word: ", end='')
        for i in guess:
            print(i,' ', end='')
        
        print("")

        print("Lives: {}" .format(lives))
        print("Misses: ", end = '')
        for i in letters_missed:
            print(i,' ',end='')

        input_guess = input("\nWhat is your guess {}? " .format(player_names[current_player]))
        print("")
        if (len(input_guess) > 1):
            print("Please only input 1 letter")
            continue
        elif (input_guess.isalpha()):
            flag = check_letter(input_guess.upper(), word_to_guess.upper())

        if (flag == 1):
            for i in range(word_length):
                if(word_to_guess[i] == input_guess):
                    guess[i] = input_guess.upper()
                    player_scores[current_player] += 1
        elif (flag == 0):
            lives = lives - 1

        print("===============")
        print("Current Scores")
        print_player_names(len(player_names))
        print("===============")

        if (current_player >= (number_of_players - 1)):
            current_player = 0
        elif (current_player <= (number_of_players - 1)):
            current_player += 1
  
def add_player_to_list(players):
    for name in range(players):
        name = (input("What is your name Player: "))
        player_names.append(name)
        player_scores.append(0)

def random_words():
    words = ["headline", "soup", "filter", "command", "mass", "truck", "tumble", "flourish", "squash", "mouth"]
    return random.choice(words)

def check_letter(letter, word_to_guess):
    flag = 0
    
    if (letter in word_to_guess): 
            flag = 1
    if (flag == 0):
        if (not letter in letters_missed):
            letters_missed.append(letter.upper())
    
    return flag

def check_win_condition(lives, guess, word_to_guess):

        if (lives == 0):
            print("You have run out of lives. Better luck next time!")
            print("The correct word was {}\n" .format(word_to_guess.upper()))
            
            while(True):
                play_again = input("Would you like to play again? (Yes/No) ").lower()
                if (play_again != "yes" and play_again != "no"):
                    print("Wrong input. Please input yes or no")
                elif (play_again == "yes"):
                    print("\n")
                    
                    del player_names[:]
                    del player_scores[:]
                    del letters_missed[:]

                    game()
                elif (play_again == "no"):
                    print("")
                    exit()
        
        if (not '_' in guess):
            print("")
            print("Congratulations! You figured out the word.")
            print("The word was {}" .format(word_to_guess.upper()))
            check_higher_score()
            print("")

            while(True):
                play_again = input("Would you like to play again? (Yes/No) ").lower()
                if (play_again != "yes" and play_again != "no"):
                    print("Wrong input. Please input yes or no")
                elif (play_again == "yes"):
                    print("\n")
                    
                    del player_names[:]
                    del player_scores[:]
                    del letters_missed[:]
                    
                    game()
                elif (play_again == "no"):
                    print("")
                    exit()

def check_higher_score():
    # if (len(player_scores != len(set(player_scores)))):
    #     print("More than 1 person ")

    duplicates = defaultdict(list)
    for i,item in enumerate(player_scores):
        duplicates[item].append(i)
    duplicates = {k:v for k,v in duplicates.items() if len(v)>1}

    if not duplicates:
        max_score = max(player_scores)
        max_score_index = player_scores.index(max_score)

        print("{} got the highest score with {} points!" .format(player_names[max_score_index], max_score))
    else:
        max_score = max(player_scores)
        print("Multiple players achieved a high score of {}!" .format(max_score))

    # dups = defaultdict(list)
    # for i, e in enumerate(player_scores):
    #     dups[e].append(i)
    # for k, v in sorted(dups.items()):
    #     if len(v) >= 2:
    #         print('K:%s: V:%r' % (k, v))
    #     for values in v:
    #         print("Players {} " .format(player_names[values]), end='')

    #         print("got: ", end='')

def print_player_names(players):
    print("\nThe current players are: ")
    for item in range(players):
        print(player_names[item],end=': ') 
        print(player_scores[item])
        

def game():
    players()

game()

