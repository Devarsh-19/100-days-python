import os
import logo


print(logo.logo)
bidders = []

while True:

    nm  = input("ENTER YOUR NAME: ")
    bid = int(input("ENTER BID AMOUNT: "))

    bidders.append({
        nm:bid
    })
    
    next = input("ADD ANOTHER BIDDER? ")
    if next in ["Y","y"]:
        continue
    else:
        break

highest = 0
winner = ""
for bid in bidders:
    for x  in bid:
        amt = bid[x]
        if amt > highest:
            highest = amt
            winner = x
            
            
print(f"WINNER - {winner} BID AMOUNT : ${highest}")
        

        

    