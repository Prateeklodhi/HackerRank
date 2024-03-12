evan_count = []
three_div = []
five_div = 0
drones = []
for i in range(1,101):
    drones.append(i)

def pop_drone_by_two(drones):
    for drone in drones:
        if drone % 2 == 0:
            evan_count.append(drone)
            drones.remove(drone)
    return evan_count

def pop_drone_by_three(drones):
    for drone in drones:
        if drone % 3 == 0:
            three_div.append(drone)
            drones.remove(drone)
    return three_div

print(len(pop_drone_by_two(drones)))
print(len(pop_drone_by_three(drones)))
print(len(drones))