def predict(X, c):
    # Loop through each cabin in the input data
    for cabin in X:
        # Calculate the predicted price by taking the dot product of the cabin's data and the coefficients
        price = sum([a*b for a, b in zip(cabin, c)])
        print(price)

# Cabin details: size, sauna size, distance to water, number of bathrooms, proximity to neighbors
X = [
    [66, 5, 15, 2, 500],  # Cabin 1
    [21, 3, 50, 1, 100],  # Cabin 2
    [120, 15, 5, 2, 1200] # Cabin 3
]

# Coefficients: c1 for size, c2 for sauna size, c3 for distance to water, etc.
c = [3000, 200, -50, 5000, 100]

# Call the function to predict prices
predict(X, c)
