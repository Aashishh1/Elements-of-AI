def count11(seq):
    count = 0
    # Iterate through the sequence, checking each pair of consecutive elements
    for i in range(len(seq) - 1):  # Loop up to second-to-last element
        if seq[i] == 1 and seq[i+1] == 1:  # Check if current and next element are both 1
            count += 1
    return count

# Test cases
print(count11([0, 0, 1, 1, 1, 0]))  # this should print 2
