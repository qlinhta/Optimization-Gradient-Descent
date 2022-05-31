import numpy as np
import matplotlib.pyplot as plt


# Loss function
def loss(a):
    return a ** 2 - 4 * a + 10


theta = np.arange(-4, 8, 0.1)
loss_value = loss(theta)
plt.plot(theta, loss_value, lw=2)


# Derivative loss
def derivative(a):
    return 2 * a - 4


# Parameters
theta = -4
alpha = 0.01
epsilon = 0.0001

while True:
    theta = theta - alpha * derivative(theta)
    plt.plot(theta, loss(theta), 'b*')
    plt.pause(0.1)
    if abs(derivative(theta)) < epsilon:
        break
plt.show()
print("Minimum loss function: ", loss(theta))
print("Minimum loss function when theta equals: ", theta)
