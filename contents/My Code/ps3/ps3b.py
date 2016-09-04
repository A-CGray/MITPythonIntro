# Problem set 3b
# Name: Alasdair Gray
# Date: 10th August 2016
# Time Spent: ~2 hours

from ps3a import *
import time
from perm import *

import time
#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    choice_score =0 # Initialise score for computer's word choice
    comp_word = '.' # Set computer's word choice to '.' so that if no words are found the computer will exit the hand
    hand_size = calculate_handlen(hand)
    print 'Computer is thinking',
    for n in range(1, hand_size+1):
        print '.',
        perms = get_perms(hand, n)
        for perm in perms:
            if is_valid_word_comp(perm, hand, word_list) is True:
                if get_word_score(perm,HAND_SIZE) > choice_score:
                    comp_word = perm
    print 'Computer chooses', comp_word
    return comp_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    cumulative_score = 0 # Initialise cumulative hand score
    new_hand = dict(hand)
    while 1 > 0: # Infinite loop to ensure function will keep playing until user inputs '.'
        display_hand(new_hand)
        valid_word = False # Set/reset valid word flag to False to allow word input loop to run
        while valid_word is False:
            word = comp_choose_word(new_hand, word_list)
            if word == '.':
                print "Total hand score: ", cumulative_score, " points."
                return
            valid_word = is_valid_word(word, new_hand, word_list)
        new_hand = update_hand(new_hand, word) # Update hand
        word_score = get_word_score(word, HAND_SIZE)
        cumulative_score += word_score
        print word, 'scored ', word_score, 'points, total: ', cumulative_score, 'points.'
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    hand = {} # Initialise empty hand
    while 1>0:
        mode = raw_input("What would you like to do? Input 'n' to play a new hand, 'r' to replay your last hand or "
                         "'e' to exit the game: ")
        if mode == 'e':
            print 'Awwwwwwww! See you later bich'
            return # Say bye and then exit
        elif mode == 'n' or 'r':
            player = raw_input("Who will play this hand? Enter 'u' to play yourself or 'c' to let the computer play "
                               "the hand")
            if mode == 'n':
                hand = deal_hand(HAND_SIZE)
            elif mode == 'r':
                if hand == {}: # If user hasn't had hand dealt yet (because it's their first turn)
                    print "Dafuq m8?! you don't have a hand to play again, I dealt you a new one dipshit"
                    hand = deal_hand(HAND_SIZE) # Insult the user and deal them a hand
            if player == 'u':
                play_hand(hand, word_list) # User plays hand
            elif player == 'c':
                comp_play_hand(hand, word_list)
            else:
                print "That wasn't any of the options I gave you, try harder now"
        else:
            print "That wasn't any of the options I gave you, try harder now"
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)