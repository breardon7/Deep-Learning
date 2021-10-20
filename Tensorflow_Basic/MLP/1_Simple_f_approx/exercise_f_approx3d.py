# %% -------------------------------------------------------------------------------------------------------------------

# -------------------------------------
# Approximate a 3D Function using a MLP
# -------------------------------------

# 1. Define the function y = x1**2 - x2**2 you will train the MLP to approximate. A 3D plot can be found at:
# # http://www.livephysics.com/tools/mathematical-tools/online-3-d-function-grapher/

def f(x1, x2):
   return x1**2 - x2**2

# 2. Define a helper function to plot the real function and the MLP approximation. Hint:
# from mpl_toolkits.mplot3d import Axes3D, use ax.contour3D on 3 inputs with shapes (sqrt(n_examples), sqrt(n_examples))
# You may do 3. first to get the data and figure out why the shapes are like this

def plot(X1, X2, f):
    import matplotlib.pyplot as plt
    Z = f(X1, X2)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X1, X2, Z, 50, cmap='binary')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('y')
    ax.set_title('3D contour')
    plt.show()


# 3. Generate the data to train the network using the function you defined in 1. Hint:
# Use np.meshgrid() and then reshape the input to (n_examples, 2) and the target to (n_examples, 1)

import numpy as np
x1 = np.linspace(-5,5,100)
x2 = np.linspace(-5,5,100)

X1, X2 = np.meshgrid(x1, x2)

# 4. Define a MLP to approximate this function using the data you just generated.
# Play with the number of layers, neurons and hidden activation functions (tanh, ReLu, etc.)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

LR = 0.1
N_NEURONS = 10
N_EPOCHS = 500

model = Sequential([Dense(N_NEURONS, input_dim=1)])

# 5. Use Adam or another optimizer and train the network. Find an appropriate learning rate and number of epochs.

# 6. Use the function you defined in 2. to visualize how well your MLP fits the original function

# %% -------------------------------------------------------------------------------------------------------------------
