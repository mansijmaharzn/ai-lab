import random


# list of words for the game
WORD_LIST = ['mansij', 'is', 'a', 'good', 'boy']


def get_word():
    return random.choice(WORD_LIST).upper()


def check_valid(chosen_word, user_choice):
    index = 0
    valid = False
    valid_index_list = []
    for letter in chosen_word:
        if letter == user_choice:
            valid_index_list.append(index)
            valid = True

        index += 1

    return valid, valid_index_list


def update_remaining_list(remaining_list, valid_index_list, user_choice):
    for index in valid_index_list:
        remaining_list[index] = user_choice


def main():
    print("Welcome to Hangman!")
    chosen_word = get_word()
    # print(chosen_word) # TODO: remove later ;)

    remaining_list = list("_" * len(chosen_word)) # list to store the guessed letters
    print(f"The word has {len(chosen_word)} letters!")

    user_alive = True
    lives = 5


    while user_alive:
        remaining_letters = ' '.join(remaining_list)
        print(remaining_letters) 
        
        user_choice = input("Guess a letter: ")[0].upper()

        valid, valid_index_list = check_valid(chosen_word, user_choice)
        
        if valid:
            update_remaining_list(remaining_list, valid_index_list, user_choice)

        else:
            lives -= 1
            print(f"Wrong guess! Lives remaining: {lives}")
        

        # check if user still alive
        if lives <= 0:
            print("Oops! You lose")
            print(f"The word was {chosen_word}.")
            user_alive = False
        
        # check if there's still more to guess
        if "_" not in remaining_list:
            remaining_letters = ' '.join(remaining_list)
            print(remaining_letters)
            print("Moye Moye! You Won.")
            user_alive = False


main()