# Image Bifurcation Diagram for a.png was made using a_values = np.arange(0, 0.38, 0.001)
# Image Bifurcation Diagram for b.png was made using b_values = np.arange(0.001, 1.8, 0.001)
# Image Bifurcation Diagram for c.png was made using c_values = np.arange(1, 45, 0.01)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar

# Plot and iteration of points
def main(a, b):
    c_values = np.arange(1, 45, 0.1)
    pts = [point for c in c_values for point in iterate(c, a, b)]

    plt.figure(figsize=(8, 7))
    plt.scatter(*zip(*pts), s=1, c='darkred')
    plt.xlabel('c', fontstyle='italic')
    plt.ylabel('x', fontstyle='italic')
    plt.title('Bifurcation Diagram')
    plt.grid(True)
    plt.show()

# Iteration function which calls the ODE solver function
def iterate(c, a, b):
    fsol = solve_system(c, a, b)
    return [(c, find_max_x(fsol, i)) for i in range(200, 301, 10)]

# ODE solver using solve_ivp
def solve_system(c, a, b):
    sol = solve_ivp(system, [0, 310], [-1, 0, 0], args=(a, b, c), dense_output=True)
    return sol

# Finding maximum value of x-coordinate (minimize_scalar is used since I don't know a function to find maximum, hence the negative sign in the return call)
def find_max_x(sol, start_t):
    result = minimize_scalar(lambda t: sol.sol(t)[0], bounds=(start_t, start_t + 10), method='bounded')
    return -result.fun

# Strange attractor equation (Rössler attractor in the current case)
def system(t, u, a, b, c):
    x, y, z = u
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + x * z - c * z
    return [dxdt, dydt, dzdt]

# Define variables a and b
a_value = 0.1
b_value = 0.1
main(a_value, b_value)
