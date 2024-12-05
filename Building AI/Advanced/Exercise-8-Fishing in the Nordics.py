def guess(winner_gender):
    # Data
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    male_fishers = [1822, 2575, 3400, 11291, 1731]
    female_fishers = [69, 77, 400, 320, 26]
    total_male_fishers = sum(male_fishers)
    total_female_fishers = sum(female_fishers)

    # Choose the relevant list based on the gender of the winner
    if winner_gender == 'female':
        fishers = female_fishers
        total_fishers = total_female_fishers
    else:
        fishers = male_fishers
        total_fishers = total_male_fishers

    # Find the country with the highest number of fishers of the given gender
    biggest = 0
    guess = None
    for country, fisher in zip(countries, fishers):
        if fisher > biggest:
            biggest = fisher
            guess = country

    # Calculate the probability
    country_index = countries.index(guess)
    probability = (fishers[country_index] / total_fishers) * 100

    return (guess, probability)

def main():
    country, fraction = guess("male")
    print(f"if the winner is male, my guess is he's from {country}; probability {fraction:.2f}%")
    
    country, fraction = guess("female")
    print(f"if the winner is female, my guess is she's from {country}; probability {fraction:.2f}%")

main()
