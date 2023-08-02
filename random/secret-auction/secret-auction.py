bidders = []

# Ask users for name and bid amount 
def secretAuction():
    newBid = {}
    newBid["name"] = input("What is your name?: ")
    newBid["bid_amount"] = float(input("What is your bid?: ")) 
    # Add new bid to the bidders list 
    bidders.append(newBid) 

def findMaxBid():
    # Find max bid_amount in list of bidders
    maxBid = max(bid["bid_amount"] for bid in bidders) 
    # Find name of bidder associated with maxBid 
    winners = [bidder["name"] for bidder in bidders if bidder["bid_amount"] == maxBid]
    # Change list item to string 
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

