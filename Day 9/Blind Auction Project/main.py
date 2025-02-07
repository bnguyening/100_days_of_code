# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo
      )
auction = { }
winning_bid = 0
winner = []
bidding_active = True
while bidding_active:
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?: \n"))
    if bid > winning_bid:
        winning_bid = bid
        winner = name
    auction.update({name : bid})
    continue_bids = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()

    if continue_bids == "yes":
        print("\n" * 20)

    elif continue_bids == "no":
        bidding_active = False
        print(f'The winner of this auction is {winner} with the winning bid of ${winning_bid}')