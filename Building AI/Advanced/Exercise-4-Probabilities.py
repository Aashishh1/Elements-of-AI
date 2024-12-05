import random

def main():
    # Define the words and their corresponding probabilities
    options = ['dogs', 'cats', 'bats']
    probabilities = [0.80, 0.10, 0.10]

    # Randomly choose one word based on the probabilities
    favourite = random.choices(options, probabilities)[0]

    # Print the result
    print("I love " + favourite)

main()
