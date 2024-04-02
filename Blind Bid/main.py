from os import system, name

bids = {}


def bid_comparison(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of the auction is {winner} with a winning bid of ${highest_bid}")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


more_bidders = True
while more_bidders:
    name = input("What is the name of the bidder? \n")
    amount = int(input("What is the amount you would like to bid? \n$"))

    bids[name] = amount

    other_bidders = input("Are there other bidders like you? 'Yes' or 'No' \n")
    if other_bidders == "Yes":
        clear()
        print(f"Total number of bids {len(bids)}")
        more_bidders = True
    else:
        clear()
        bid_comparison(bids)
        more_bidders = False
