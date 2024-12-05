import numpy as np

# Define the probabilities for the normal and loaded die
p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]  # normal die (equal probability for each face)
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]  # loaded die (higher probability for 6)

# Function to simulate the dice rolls
def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2  # Loaded die probabilities
    else:
        print("rolling a normal die")
        p = p1  # Normal die probabilities

    # Roll the dice 10 times and add 1 to the result (to get values from 1 to 6)
    sequence = np.random.choice(6, size=10, p=p) + 1
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

# Function to apply Bayes' theorem to decide which die is more likely
def bayes(sequence):
    odds = 1.0  # Start with odds 1:1, meaning both dice are equally likely
    for roll in sequence:
        if roll == 6:
            # If the roll is 6, update the odds in favor of the loaded die
            odds *= 0.5 / 0.167  # Likelihood ratio for 6: (P(6|loaded) / P(6|normal))
        else:
            # If the roll is not 6, update the odds in favor of the normal die
            odds *= 0.1 / 0.167  # Likelihood ratio for other numbers: (P(non-6|loaded) / P(non-6|normal))
    
    # If the odds are greater than 1, it suggests the loaded die is more likely
    if odds > 1:
        return True  # Loaded die is more likely
    else:
        return False  # Normal die is more likely

# Roll the dice and analyze the sequence
sequence = roll(True)  # True means the loaded die
if bayes(sequence):
    print("I think it's the loaded die")
else:
    print("I think it's the normal die")
