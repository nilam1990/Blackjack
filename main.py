# Black Jack Requirement
# Our Blackjack House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random


def deal_card():
    """ return random cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    """ Return the sum(cards) """
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    # Hint 8: Inside calculate_score() check for an 11 (ace).
    # If the score is already over 21, remove the 11 and replace it with a 1.
    # You might need to look up append() and remove().
    score = sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return score


def compare(score_of_user, score_of_computer):
    # Hint 13: Create a function called compare() and
    # pass in the user_score and computer_score.
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses.
    # If the user has a blackjack (0), then the user wins.
    # If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses.
    # If none of the above, then the player with the highest score wins.
    if score_of_user == score_of_computer:
        return "Its a Draw"
    elif score_of_computer == 0:
        return " You lose"
    elif score_of_user == 0:
        return "You win! "
    elif score_of_user > 21:
        return "Computer Win. User Burst!"
    elif score_of_computer > 21:
        return "You win. Computer Burst!"
    elif score_of_user > score_of_computer:
        return "You win"
    elif score_of_computer > score_of_user:
        return "You lost"


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def play_game():

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    # Hint 9: Call calculate_score().
    # If the computer or the user has a blackjack (0)
    # or if the user's score is over 21, then the game ends.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" User card is: {user_cards} and User score is {user_score}")
        print(f" Computer first card is: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Hint 10: If the game has not ended, ask the user if they want to draw another card.
            # If yes, then use the deal_card()
            # function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type y to get another card or Type n to no: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

        # Hint 11: The score will need to be rechecked
        # with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand {user_cards},final score {user_score}")
    print(f"Computer final hand{computer_cards},computer score {computer_score}")
    # Hint 12: Once the user is done, it's time to let the computer play.
    # The computer should keep drawing cards as long as it has a score less than 17.
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
