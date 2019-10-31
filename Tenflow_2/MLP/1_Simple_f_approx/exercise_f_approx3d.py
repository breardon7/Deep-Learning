# %% -------------------------------------------------------------------------------------------------------------------

# -------------------------------------
# Approximate a 3D Function using a MLP
# -------------------------------------

# 1. Define the function y = x1**2 - x2**2 you will train the MLP to approximate. A 3D plot can be found at:
# # http://www.livephysics.com/tools/mathematical-tools/online-3-d-function-grapher/

# 2. Define a helper function to plot the real function and the MLP approximation. Hint:
# from mpl_toolkits.mplot3d import Axes3D, use ax.contour3D on 3 inputs with shapes (sqrt(n_examples), sqrt(n_examples))
# You may do 4. first to get the data and figure out why the shapes are like this

# 3. Define a MLP class to approximate this function using some data you will generate later in 4.
# Play with the number of layers, neurons and hidden activation functions (tanh, ReLu, etc.)
# You may do 4. first to get the data and figure out the right input and output shapes on the MLP

# 4. Generate the data to train the network. Hint:
# Use np.meshgrid() and then reshape the input to (n_examples, 2) and the target to (n_examples, 1)

# 5. Use Adam or another optimizer and train the network. Find an appropriate learning rate and number of epochs.

# 6. Use the function you defined in 2. to visualize how well your MLP fits the original function

# %% -------------------------------------------------------------------------------------------------------------------
