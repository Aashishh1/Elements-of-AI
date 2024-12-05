import numpy as np

# Generate random training data and test data
x_train = np.random.rand(10, 3)   # 10 random vectors of dimension 3
x_test = np.random.rand(3)        # One more random vector of the same dimension

# Function to calculate the Euclidean distance between two vectors
def dist(a, b):
    return np.sqrt(np.sum((a - b)**2))

# Function to find the nearest neighbor
def nearest(x_train, x_test):
    nearest_index = -1
    min_distance = np.inf
    
    # Loop through all the vectors in x_train
    for i, train_point in enumerate(x_train):
        # Calculate the distance between the test point and the current train point
        distance = dist(train_point, x_test)
        
        # Check if this distance is smaller than the smallest distance found so far
        if distance < min_distance:
            min_distance = distance
            nearest_index = i
    
    # Print the index of the nearest neighbor
    print(nearest_index)

# Call the nearest function
nearest(x_train, x_test)
