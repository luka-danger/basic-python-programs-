bidders = []

def secretAuction():
    newBid = {}
    newBid["name"] = input("What is your name?: ")
    newBid["bid_amount"] = float(input("What is your bid?: ")) 
    bidders.append(newBid) 

def findMaxBid():
    maxBid = max(bid["bid_amount"] for bid in bidders) 
    winners = [bidder["name"] for bidder in bidders if bidder["bid_amount"] == maxBid]
    nameOfWinner = "".join(winners)
    print(f'The winner is {nameOfWinner} with a bid of ${maxBid}!')

secretAuction()
while True:
    moreBidders = input("Are there anymore bidders? Yes or No: ")
    if moreBidders.lower() == "yes":
        secretAuction()
        print(bidders)
    elif moreBidders.lower() == "no": 
        print("No more bidders")
        findMaxBid()
        break 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

