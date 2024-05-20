# Display on the amount of Tickets and Buyers
def sell_tickets():
    total_tickets_left = 20
    total_buyers = 0
    
# The whole loop for the Tickets
    while total_tickets_left > 0:
        print("Number of Remaining Tickets:", total_tickets_left)
        number_tickets = int(input("How Many Tickets Would You Like to Buy? (Up to 4): "))
        
# Option if they put something else than 1 through 4
        if number_tickets < 1 or number_tickets > 4:
            print("Invalid Number of Tickets. Make sure to select between 1 and 4 tickets.")
            continue
        
# Another Option if they have no more Tickets
        if number_tickets > total_tickets_left:
            print("Sorry, We Don't Have Enough Tickets Available.")
            continue
        
        total_tickets_left -= number_tickets
        total_buyers += 1
        
# Printing out the Results
    print("All Tickets Have Been Sold.")
    print("Total Number of Buyers:", total_buyers)

sell_tickets()
