import math
import random

# Generate random mountains
w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # Track starting height and position
    start_height = h[x]
    summit = False
    
    while not summit:
        summit = True
        # Check if moving right increases height
        if x + 1 < len(h) and h[x + 1] > h[x]:
            x = x + 1
            summit = False  # We haven't reached the summit yet
        # Check if moving left increases height
        elif x - 1 >= 0 and h[x - 1] > h[x]:
            x = x - 1
            summit = False  # We haven't reached the summit yet
    
    # After climbing, check if we are at a better or equal height than where we started
    if h[x] < start_height:
        return x  # If the height is lower than start, we stop at the start position
    return x

def main(h):
    # Start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

# Run the main function
x0, x = main(h)
print(f"Started at index {x0}, climbed to summit at index {x}, height: {h[x]}")

# Add an assertion for the test to pass
assert h[x] >= h[x0], f"Test Failed: {h[x]} not greater than or equal to {h[x0]}"
