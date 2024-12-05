import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])  # Cabin features
y = np.array([250000, 60000, 525000])  # Actual prices
c = np.array([3000, 200 , -50, 5000, 100])  # Coefficients

def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        # Calculate the predicted price using the dot product of xi and c
        prediction = np.dot(xi, c)
        
        # Calculate the squared error (yi - prediction) ** 2
        error = (yi - prediction) ** 2
        
        # Add to the total SSE
        sse += error

    print(sse)

squared_error(X, y, c)
