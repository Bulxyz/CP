import math

# Define functions to differentiate
def func_cos(t):
  return math.cos(t)

def func_exp(t):
  return math.exp(t)

# Numerical differentiation method
def numerical_diff(func, t, h):

  # Forward difference
  fd = (func(t+h) - func(t)) / h   

  # Central difference 
  cd = (func(t+h/2) - func(t-h/2)) / h  

  # Calculate points for extrapolated difference
  th4 = t + h/4 
  tmh4 = t - h/4
  th2 = t + h/2
  tmh2 = t - h/2

  # Extrapolated difference
  ed = (8*(func(th4)-func(tmh4)) - (func(th2)-func(tmh2))) / 3/h

  # Return derivatives as tuple
  return fd, cd, ed

# Step size  
h = 0.1

# Differentiate cos(t) at sample points
print("cos(t) results:")
for t in [0.1, 1, 100]:
  print(numerical_diff(func_cos, t, h))

# Differentiate exp(t)  
print("\nexp(t) results:")  
for t in [0.1, 1, 100]:
  print(numerical_diff(func_exp, t, h))
######################################################################################



