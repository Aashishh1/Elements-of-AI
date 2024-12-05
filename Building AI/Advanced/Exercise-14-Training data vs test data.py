import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading
    
    # Read in the training data and separate it into x_train and y_train
    train_data = np.genfromtxt(StringIO(train_string), delimiter=' ')
    x_train = train_data[:, :-1]  # All columns except the last one (features)
    y_train = train_data[:, -1]   # Only the last column (price)

    # Fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train, rcond=None)[0]

    # Read in the test data and separate x_test from it
    test_data = np.genfromtxt(StringIO(test_string), delimiter=' ')
    x_test = test_data[:, :-1]  # All columns except the last one (features)

    # Print out the linear regression coefficients
    print(c)

    # Print out the predicted prices for the two new cabins in the test data set
    predicted_prices = x_test @ c
    print(predicted_prices)

main()
