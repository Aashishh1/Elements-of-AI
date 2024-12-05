import numpy as np

def generate(p1):
    # Generate a sequence of 10000 random zeros and ones where the probability of one is p1
    seq = np.random.choice([0, 1], p=[1 - p1, p1], size=10000)
    return seq

def count(seq):
    # Convert the sequence to a string of "0"s and "1"s
    seq_str = ''.join(map(str, seq))
    
    # Count occurrences of "11111" using a sliding window approach
    count_11111 = 0
    for i in range(len(seq_str) - 4):  # Loop to the second-to-last index for a 5-character pattern
        if seq_str[i:i+5] == '11111':  # Check if the substring is "11111"
            count_11111 += 1

    return count_11111

def main(p1):
    seq = generate(p1)
    return count(seq)

# Test with p1 = 2/3
print(main(2/3))
