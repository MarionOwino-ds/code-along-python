#) Create variables to store:
#    - customer name
customer_name = input("Enter Customer name:")
#    - number of passes
number_of_passes = int(input("Enter number of passes: "))
#    - tokens per pass
tokens_per_pass = int(input("Enter the number of tokens per pass :"))
#    - price per pass
price_per_pass= float(input ("Enter the price per pass:"))

#    - tokens required per game
tokens_required_per_game= int(input("Enter the number of tokens required per game:"))
# 2) Calculate:
#    - total tokens
total_tokens=number_of_passes * tokens_per_pass
#    - total cost
total_cost=number_of_passes * price_per_pass
#    - games available  (use 'floor division' to get a whole number)
games_available=total_tokens // tokens_required_per_game  #  floor division  
# 3) Print a summary with:
#    - customer name
print ("customer name:", customer_name)
#    - passes bought
print ("passes bought:", number_of_passes)
#    - total tokens
print ("total tokens:", total_tokens)
#    - total cost
print ("total cost:", total_cost)
#    - games available
print ("games available:", games_available)