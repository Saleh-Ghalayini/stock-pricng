#defining a function to calculate the highest profit possible and return it
def max_profit(prices):

    #assigning the needed variables to do the operation
    minimum = prices[0]
    highest_profit = 0

    #in this loop we check to see where the lowest value in the stock is 
    #and we search for the highest margin value which is the highest profit we will return
    for i in range(1, len(prices)):
        if(minimum > prices[i]):
            minimum = prices[i]
        elif(highest_profit < prices[i] - minimum ):
            highest_profit = prices[i] - minimum

    return highest_profit

#assigning the highest profit we will get from the function max_profit to the variable named profit_result
profit_result = max_profit([5,2,7,3,10,9])

#printing the highest profit obtained from the function
print(f"the highest profit obtained is {profit_result}")

#if the project was bigger and more complex it would've taken more steps and git pushes to complete