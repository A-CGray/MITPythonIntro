# 6.00 Problem Set 3
# Name: Alasdair Christison gray
# Time Spent: 2 hr
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# your code begins here!

def blankify(word,guesses):
    # This function takes a string "word" and a string of guessed letters "guesses"
    # it outputs a string which is the input word with blanks in place of any letters not contained in guesses
    # It also outputs the number of spaces remaining in the word which will be used by the game to check if the word has
    #  been correctly guessed. Note that this is the number of spaces remaining NOT the number of unique letters left,
    #  number of spaces will always be equal to or greater than the number of unique letters remaining
    spaces = 0 #initialise the number of letters missing from the word
    out = '' # initialise the output as an empty string
    if type(word) is not str:
        print 'Word not input as string, try again.'
        return False, False
    if type(guesses) is not str:
        print 'Guesses not input as string, try again.'
        return False, False
    for ind, char in enumerate(word.lower()): # Iterate over the characters in word, ind is the index of each letter,
        # char is the
        # character itself
        if char in guesses.lower(): # If the current character of word is in guesses
            out += word[ind] # Add the current character to the output string, use word[ind] rather than char to
            # retain any capitalisation from word
        else:
            out += '_'
            spaces += 1
        out += ' ' # Add a space between characters, this makes the blanks discernable
    return out, spaces

def unblankify(word,guesses):
    # This function does the opposite of blankify, it takes the same inputs but outputs a string with all occurences
    # of the letters in guesses blanked out. This will be used to display the remaining letters during the game.
    spaces = 0 #initialise the number of letters missing from the word
    out = '' # initialise the output as an empty string
    if type(word) is not str:
        print 'Word not input as string, try again.'
        return False, False
    if type(guesses) is not str:
        print 'Guesses not input as string, try again.'
        return False, False
    for ind, char in enumerate(word.lower()): # Iterate over the characters in word, ind is the index of each letter,
        # char is the
        # character itself
        if char in guesses.lower(): # If the current character of word is in guesses
            out += '_'
            spaces += 1
        else:
            out += word[ind] # Add the current character to the output string, use word[ind] rather than char to
            # retain any capitalisation from word
        out += ' ' # Add a space between characters, this makes the blanks discernable
    return out, spaces
#######################################START OF GAME#############################################
# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
Play_Again = True # Variable which controls the rerunning of game, set true for now so that game plays at least once.
# Initialise the scores of the computer and the player, these will be updated and displayed after each game
comp_score = 0
player_score = 0
print 'WELCOME TO HANGMAN!'
print "Let's begin"
while Play_Again:
    word = choose_word(wordlist) # Randomly choose word to be guessed by user
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # initialise the alphabet, this string will be used to display the
    # remaining guesses
    guesses = '' # Initialise the string of guesses made by the player
    lives = 8 # Initialise the number of lives the player has left
    Rem_Letters = unblankify(alphabet, guesses)[0] # Initialise the letters remaining to be guessed
    state, spaces = blankify(word, guesses) # Initialise the display to be guessed with blanks and the number of
    # blanks remaining
    print "I'm thinking of a word ", len(word), " letters long."
    print '________________________________'
    while lives>0 and spaces>0: # Loop until word is guessed (spaces = 0) or user runs out of lives (lives = 0)
        print "You have ", lives, " lives remaining"
        print "Available letters: ", Rem_Letters
        print state
        guess = str(raw_input("Make your guess: "))
        while len(guess)>1 or guess.lower() not in alphabet: # If user's guess is more than one character or not
            # in the english alphabet then display message and retake input.
            guess = str(raw_input("Whoops, your guess is either too long or not in the remaining letters, try again: "))
        while guess.lower() in guesses: # If user has already guessed that letter display a slightly more insulting
            # message and retake input
            guess = str(raw_input("You already guessed that numbnuts, try again: "))
        guesses += guess # Add the current guess to the list of guesses made so far
        if guess.lower() in word.lower(): # If guess is correct
            print "Good guess!"
        else: # If guess is incorrect
            print "Unlucky, that letter's not in my word"
            lives += -1 # Lose a life
        state, spaces = blankify(word, guesses) # Update the display state of the word and the number of spaces
        # remaining
        Rem_Letters = unblankify(alphabet, guesses)[0] # Update the remaining letters
        print'________________________________'
    if spaces == 0: # If game ended because player guessed word correctly
        player_score +=1 # Add a point to the player's score
        print "Congratualtions! You guessed my word, ", word
    else: # If the game ended because the player ran out of lives
        comp_score += 1 # Add a point to the computer's score
        print "Haha you lose!"
        print "The word I was thinking of was ", word
    print "Current score:"
    print "You: ", player_score, ' : ', comp_score, 'The computer'
    rematch = str(raw_input("Would you like to play again? (yes or no): "))
    print'________________________________'
    if rematch[0].lower() in 'y':
        print "OK, game on!"
        print'________________________________'
    else:
        Play_Again = False
        if player_score > comp_score:
            print "OK, I'll try harder next time"
        elif comp_score > player_score:
            print "Better luck next time loser!"
        else:
            "OK, good game!"