bidders = []

def secretAuction():
    newBid = {}
    newBid["name"] = input("What is your name?: ")
    newBid["bid_amount"] = input("What is your bid?: ")
    bidders.append(newBid) 

secretAuction()
while True:
    moreBidders = input("Are there anymore bidders? Yes or No: ")
    if moreBidders.lower() == "yes":
        secretAuction()
    elif moreBidders.lower() == "no": 
        print("No more bidders")
        break 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

