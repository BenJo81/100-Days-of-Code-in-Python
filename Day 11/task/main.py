from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def final_hand():
    print(f"    Your final hand: {player_hand}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_hand}, final score: {computer_score}")


def check_score():
    if user_score > 21:
        final_hand()
        print("You went over. You lose 😭")
        return False
    elif computer_score > 21 and user_score <= 21:
        final_hand()
        print("Dealer busts. You win! 🤩")
        return False
    elif computer_score > user_score and computer_score <= 21:
        final_hand()
        print("Computer wins. You lose 😤")
        return False
    elif computer_score == user_score:
        final_hand()
        print("It's a draw 🙃")
        return False
    else:
        return True


choice2 = "n"
blackjack = True

while blackjack:
    print(logo)
    game_on = True
    if choice2 == "n":
        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    else:
        choice = "y"
    if choice == "y":
        user_score = 0
        computer_score = 0
        player_hand = []
        computer_hand = []
        for card in range(2):
            player_hand.append(random.choice(cards))
            computer_hand.append(random.choice(cards))
        user_score = sum(player_hand)
        computer_score = sum(computer_hand)
        if sum(player_hand) == 21:
            print(f"Blackjack! You win!")
            final_hand()
            game_on = False
        if sum(computer_hand) == 21:
            print("Computer Blackjack. You lose. 😡")
            final_hand()
            game_on = False

        while game_on:
            user_score = sum(player_hand)
            if user_score > 21 and 11 in player_hand:
                ace = player_hand.index(11)
                player_hand[ace] = 1
            computer_score = sum(computer_hand)
            print(f"    Your cards: {player_hand}, current score: {user_score}")
            print(f"    Computer's first card: {computer_hand[0]}")

            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                player_hand.append(random.choice(cards))
                user_score = sum(player_hand)
                if user_score > 21:
                    game_on = check_score()
            elif another_card == "n":
                while sum(computer_hand) < 17:
                    computer_hand.append(random.choice(cards))
                    computer_score = sum(computer_hand)
                game_on = check_score()
        choice2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if choice2 == "y":
            blackjack = True
            print("\n" * 20)
        else:
            blackjack = False
    else:
        blackjack = False
