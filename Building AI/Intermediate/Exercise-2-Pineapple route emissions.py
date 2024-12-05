from itertools import permutations

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # Distance matrix in kilometers
    D = [
        [0, 8943, 8019, 3652, 10545],
        [8943, 0, 2619, 6317, 2078],
        [8019, 2619, 0, 5836, 4939],
        [3652, 6317, 5836, 0, 7825],
        [10545, 2078, 4939, 7825, 0]
    ]

    # CO2 emissions rate in kg per km per metric ton
    co2 = 0.020

    # Generate all valid routes starting from "PAN" (index 0)
    starting_point = 0
    remaining_ports = list(range(1, len(portnames)))
    all_routes = permutations(remaining_ports)

    # Calculate and print emissions for each route
    for route in all_routes:
        full_route = [starting_point] + list(route)  # Add "PAN" to the start
        distance = sum(D[full_route[i]][full_route[i + 1]] for i in range(len(full_route) - 1))
        emissions = distance * co2
        print(' '.join([portnames[i] for i in full_route]) + " %.1f kg" % emissions)

# Run the program
main()
