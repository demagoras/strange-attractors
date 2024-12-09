import matplotlib.pyplot as plt
import numpy as np

# Strange attractor equations
def attractor(xyz, sigma = 10, rho = 28, beta = 8/3):
    x, y, z = xyz
    return np.array(
        [
            sigma*(y - x), # dx/dt
            x*(rho - z) - y, # dy/dt
            x*y - beta*z # dz/dt
        ]
    )

# Time step
dt = 0.01
steps = 10000

# Initial values
xyz = np.zeros((steps + 1, 3))
xyz[0] = [0, 1, 1.05]

'''
# Euler method
for i in range(steps):
    xyz[i + 1] = xyz[i] + attractor(xyz[i]) * dt
'''

# Runge-Kutta method
for i in range(steps):
    k1 = attractor(xyz[i])
    k2 = attractor(xyz[i] + k1 * dt/2)
    k3 = attractor(xyz[i] + k2 * dt/2)
    k4 = attractor(xyz[i] + k3 * dt)
    xyz[i + 1] = xyz[i] + dt * (k1 + 2*k2 + 2*k3 + k4) / 6

# Display figure
ax = plt.figure().add_subplot(projection='3d').plot(*xyz.T, lw=0.5)
plt.show()
