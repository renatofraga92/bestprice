from scipy.optimize import minimize

# Ask for input data: prices and sales

print("Enter the number of sales and prices for two different time periods")
print(" ")

price1 = int(input("Enter the first price: "))
sales1 = int(input("Enter the number of sales at this price: "))

price2 = int(input("Enter the second price: "))
sales2 = int(input("Enter the number of sales at this price: "))

# Calculate the angular coefficient of the line that connects the two data points

M = ((price2 - price1)/(sales2 - sales1))

# Define a function that represents the revenue as a function of the price
# Note that we multiply the function by -1 so that the minimize function will find the maximum instead of the minimum

def R(x):
    return -(x*(M*(x-sales2) + price2))

# Find the optimal price that maximizes revenue
# The minimize function is used to maximize the R function

maxsales = minimize(R,1)

# Calculate the optimal price and expected sales and revenue

Pmaxrevenue = M*(int(maxsales.x)-sales2) + price2

print(" ")
print("Best price:")
print(float(Pmaxrevenue))
print(" ")
print("Expected number of sales:")
print(int(maxsales.x))
print(" ")
print("Expected revenue:")
print(float(Pmaxrevenue*maxsales.x))
