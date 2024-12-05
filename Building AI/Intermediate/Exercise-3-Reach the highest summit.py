import math
import random  # just for generating random mountains

# generate random mountains
w = [random.random() / 3, random.random() / 3, random.random() / 3]
h = [1. + math.sin(1 + x / 6.) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in range(100)]
h[0] = 0.0
h[99] = 0.0  # Set the boundaries to 0 to avoid falling off

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    while not summit:
        summit = True  # Assume we're at the summit unless we find a better place
        
        left_is_higher = x > 0 and h[x - 1] > h[x]  # Check if left is higher
        right_is_higher = x < 99 and h[x + 1] > h[x]  # Check if right is higher
        
        if left_is_higher and right_is_higher:
            # If both sides are higher, choose one randomly
            if random.random() < 0.5:
                x = x - 1  # Go left
            else:
                x = x + 1  # Go right
            summit = False  # Continue climbing

        elif left_is_higher:
            x = x - 1  # Go left if it's higher
            summit = False  # Keep climbing
        elif right_is_higher:
            x = x + 1  # Go right if it's higher
            summit = False  # Keep climbing

    return x

def main(h):
    # start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

main(h)
