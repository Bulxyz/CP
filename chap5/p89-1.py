import numpy as np

def forward_diff(f, t, h=1e-7):
    return (f(t + h) - f(t)) / h

def central_diff(f, t, h=1e-7):
    return (f(t + h/2) - f(t - h/2)) / h

def extrapolated_diff(f, t, h=1e-7):
    return (8 

*(f(t + h/4) - f(t - h/4)) - (f(t + h/2) - f(t - h/2))) / (3*

 h)

# Define the functions
functions = [np.cos, np.exp]  # cos(t), exp(t)
t_values = [0.1, 1, 100]  # Values of t

# Implement the differentiation algorithms for each function at each value of t
for func in functions:
    for t in t_values:
        print(f"Function: {func.__name__}, t: {t}")
        print(f"Forward Diff: {forward_diff(func, t)}")
        print(f"Central Diff: {central_diff(func, t)}")
        print(f"Extrapolated Diff: {extrapolated_diff(func, t)}")
        print()
