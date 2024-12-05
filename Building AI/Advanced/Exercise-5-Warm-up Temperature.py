import math
import random

def accept_prob(S_old, S_new, T):
    # In simulated annealing, the probability of accepting a worse solution
    # depends on the difference in scores and the current temperature.
    if S_new > S_old:
        return 1.0  # Always accept better solutions
    else:
        # Calculate the probability for worse solutions using the formula:
        prob = math.exp(-(S_old - S_new) / T)
        return prob

# Example usage:
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

# Test the accept function
S_old = 150  # current score
S_new = 140  # new score
T = 5        # temperature

accept(S_old, S_new, T)
