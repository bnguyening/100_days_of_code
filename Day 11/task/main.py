import random
import art
def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    computer_hand = []
    play_blackjack = True
    play_game = True
    player_blackjack = False
    print(art.logo)
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' \n").lower()

    if start == "y":
        player_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
        player_ace_count = player_hand.count(11)
        if player_hand[-1] == 11 and player_ace_count > 1:
            player_hand[-1] = 1
        player_total = sum(player_hand)
        print(f' Your cards: {player_hand}, current score: {player_total}.')
        computer_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
        computer_ace_count = computer_hand.count(11)
        if computer_hand[-1] == 11 and computer_ace_count > 1:
            computer_hand[-1] = 1
        print(f" Computer's first card: {computer_hand[0]}")
        if player_total == 21:
            player_blackjack == True
            play_game == False
            print("You win with a Blackjack!")
            blackjack()

        else:
            add_card = input("Do you want another card? Type 'y' or 'n') \n").lower()
            while play_game == True:
                if add_card == 'y':
                    player_hand.append(random.choice(cards))
                    player_ace_count = player_hand.count(11)
                    if player_hand[-1] == 11 and player_ace_count > 1:
                        player_hand[-1] = 1
                    player_total = sum(player_hand)
                    print(f' Your cards: {player_hand}, current score: {player_total}.')
                    while add_card == "y":
                        add_card = input("Do you want another card? Type 'y' or 'n') \n").lower()
                        if add_card == 'y':
                            player_hand.append(random.choice(cards))
                            player_ace_count = player_hand.count(11)
                            if player_hand[-1] == 11 and player_ace_count > 1:
                                player_hand[-1] = 1
                            player_total = sum(player_hand)
                            print(f' Your cards: {player_hand}, current score: {player_total}.')
                            if player_total >= 21:
                                print("Bust. You lose.")
                                blackjack()


                elif add_card == 'n' and player_blackjack == False:
                    computer_total = sum(computer_hand)
                    comp_hit_cards = True
                    while comp_hit_cards == True:
                        if computer_total >= 17:
                            comp_hit_cards = False
                            computer_total = sum(computer_hand)
                            print(f"Computer's final hand: {computer_hand}, final score: {computer_total}")
                            if computer_total > player_total and 21 >= computer_total:
                                print("You Lose")
                                play_game == False
                            elif computer_total > player_total and computer_total >= 22:
                                print("You Win")
                                play_game == False
                            elif player_total > computer_total and 21 >= player_total:
                                print("You Win")
                                play_game == False
                            elif player_total > computer_total and player_total >= 22:
                                print("You Lose")
                                play_game == False
                            elif player_total == computer_total:
                                print("You Lose")
                                play_game == False
                            blackjack()

                        elif 16 >= computer_total:
                            computer_hand.append(random.choice(cards))
                            computer_ace_count = computer_hand.count(11)
                            if computer_hand[-1] == 11 and computer_ace_count > 1:
                                computer_hand[-1] = 1
                            computer_total = sum(computer_hand)
    else:
        print("Ok.")
        blackjack()


blackjack()

