import itertools

# Given data
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]

# CO2 emission factor (in kg per km per metric ton)
co2 = 0.020

# Global variables to keep track of the best route and smallest emissions
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def calculate_emissions(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += D[route[i]][route[i + 1]]
    return total_distance * co2

def permutations(route, remaining_ports):
    global smallest, bestroute
    if not remaining_ports:
        # If no remaining ports, calculate the emissions for the current route
        emissions = calculate_emissions(route)
        if emissions < smallest:
            smallest = emissions
            bestroute = route[:]
    else:
        # Recurse through all remaining ports
        for i in range(len(remaining_ports)):
            next_port = remaining_ports[i]
            new_route = route + [next_port]
            new_remaining_ports = remaining_ports[:i] + remaining_ports[i+1:]
            permutations(new_route, new_remaining_ports)

def main():
    # Start with port 0 (PAN), and explore all permutations of the other ports
    permutations([0], list(range(1, len(portnames))))

    # Print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
