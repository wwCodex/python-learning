import art
import random

print(art.logo)
bidders = {}
def input_bidder():
    name=input("What is your name?\n")
    bid=int(input("What is your bid?'\n$ "))
    bidders[name]=bid
def highest_bidder(bids):
    higher_bid=0
    name=""
    
    for key in bids:
        if bids[key] > higher_bid:
            higher_bid = bidders[key]
            name=key
        elif bids[key] == higher_bid:
            print(f"Draw between {name} and {key} at a bid of {higher_bid}")
            draw=[name,key]
            print(f"Random drawing the winner to break the tie....the winner is {random.choice(draw)}")
            exit(0)

    print(f"Highest bidder is {name} with bid: $ {higher_bid}")

while True:
    input_bidder()
    if input("Are there any more bidders? 'Yes' or 'No'").lower() =="yes":
       print("\n" * 50)
    else:
        break

highest_bidder(bidders)