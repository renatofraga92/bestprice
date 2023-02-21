# Lets import scipy library to use the minimize (in this case, maximize)
from scipy.optimize import minimize



print("Inform the number of sales on two diferent periods of time")
print(" ")


# Input the historical data: prices and sales

preco1 = int(input("Inform first price  "))
publico1 = int(input("Inform the number of sales for this price  "))

preco2 = int(input("Inform the second price  "))
publico2 = int(input("Inform the number of sales for this price  "))


# Now we look for the angular coefficient

M = ((preco2 - preco1)/(publico2 - publico1))

# Define a function using the equation of a line

def R(x):
  return -(x*(M*(x-publico2) + preco2))

# Apply optimization, the scipy library brings only the minimize option of optimization, so we must multiply the function by minus one

maxpublico = minimize(R,1)



Pmaxreceita = M*(int(maxpublico.x)-publico2) + preco2

print(" ")
print("Best Price:")
print(float(Pmaxreceita))
print(" ")
print("Expected Sales:")
print(int(maxpublico.x))
print(" ")
print("Expected Revenue:")
print(float(Pmaxreceita*maxpublico.x))


