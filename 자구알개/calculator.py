def display_stations(stations):
    print("\nAvailable Bus Stations:")
    for idx, station in enumerate(stations, 1):
        print(f"{idx}. {station}")

def find_bus_route(routes, start, end):
    for route in routes:
        if start in route and end in route:
            start_index = route.index(start)
            end_index = route.index(end)
            if start_index < end_index:
                return route[start_index:end_index + 1]
    return None

def simulate_user_inputs():
    return [
        ("Central Park", "River Side"),
        ("Green Field", "Hilltop"),
        ("City Hall", "Maple Street"),
        ("Central Park", "Central Park"),
        ("Nowhere", "River Side"),
        ("Central Park", "Nowhere"),
        ("exit", "")
    ]

def run_simulation():
    stations = ["Central Park", "Maple Street", "City Hall", "River Side", "Green Field", "Hilltop"]
    routes = [
        ["Central Park", "Maple Street", "City Hall", "River Side"],
        ["Green Field", "Maple Street", "City Hall", "Hilltop"]
    ]

    print("Bus Station Route Finder")
    print("-------------------------")

    inputs = simulate_user_inputs()
    for start, end in inputs:
        display_stations(stations)
        print(f"\nStart station: {start}")
        if start.lower() == 'exit':
            print("Goodbye!")
            break
        print(f"Destination station: {end}")

        if start not in stations or end not in stations:
            print("Invalid station name. Please try again.")
            continue

        if start == end:
            print("Start and destination stations are the same.")
            continue

        route = find_bus_route(routes, start, end)
        if route:
            print("\nRoute found:", " -> ".join(route))
        else:
            print("\nNo direct route available between the selected stations.")

if __name__ == "__main__":
    run_simulation()