def bot8(pbot, p8_bot, p8_human):
    # Calculate P(8-digits)
    phuman = 1 - pbot
    p_8_digits = (p8_bot * pbot) + (p8_human * phuman)
    
    # Use Bayes' Rule to calculate P(bot | 8-digits)
    p_bot_8 = (p8_bot * pbot) / p_8_digits
    
    # Print the result without rounding it
    print(p_bot_8)

# Test with example values
pbot = 0.1    # Probability of a follower being a bot
p8_bot = 0.8  # Probability of a bot having 8 digits in their username
p8_human = 0.05  # Probability of a human having 8 digits in their username

bot8(pbot, p8_bot, p8_human)
