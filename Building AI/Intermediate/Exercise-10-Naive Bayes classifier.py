def flip(n):
    odds = 1.0  # start with 50% chance of the magic coin, which is the same as odds = 1:1
    likelihood_ratio = 2  # each head doubles the odds (since P(heads | magic) / P(heads | normal) = 2)

    for i in range(n):
        odds *= likelihood_ratio  # multiply the odds by 2 for each head
    
    print(odds)

n = 1  # After 1 head, the odds should be 2.0
flip(n)  # Expected output: 2.0
