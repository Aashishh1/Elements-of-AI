def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)

    # Calculate and print the conditional probabilities
    for country, fisher in zip(countries, fishers):
        probability = (fisher / total_fishers) * 100
        print(f"{country} {probability:.2f}%")

main()
