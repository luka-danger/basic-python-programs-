from operator import itemgetter

bidders = []

def secretAuction():
    newBid = {}
    newBid["name"] = input("What is your name?: ")
    newBid["bid_amount"] = input("What is your bid?: ")
    bidders.append(newBid) 

def findMaxBid():
    maxBid = max(map(itemgetter('bid_amount'), bidders)) 
    print(f'The max bid is {maxBid} ')

secretAuction()
while True:
    moreBidders = input("Are there anymore bidders? Yes or No: ")
    if moreBidders.lower() == "yes":
        secretAuction()
    elif moreBidders.lower() == "no": 
        print("No more bidders")
        findMaxBid()
        break 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

