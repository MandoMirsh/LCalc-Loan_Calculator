duration = int(input())
food_cost = int(input())
oneway_flight = int(input())
night_cost = int(input())
flight_cost = 2 * oneway_flight
stay_cost = duration * (food_cost + night_cost) - night_cost
print(flight_cost + stay_cost)
