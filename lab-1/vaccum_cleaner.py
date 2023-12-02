def clean_room(location, status, goal_state, cost):
    print(f"Cleaner is in location {location}.")
    
    if status == 1:
        print("Room is dirty. Started Cleaning...")
        goal_state[location] = '0'
        cost += 1
        print("Room cleaned.")
    else:
        print(f"Room {location} is already cleaned.")
    
    return cost, goal_state


def main():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    initial_location = input("Enter location of vaccum: (A or B): ").upper()[0]
    complement_location = 'B' if initial_location == 'A' else 'A'

    initial_location_status = int(input(f"Enter '0' for clean or '1' for dirty, for room {initial_location}: "))
    initial_location_complement_status = int(input(f"Enter '0' for clean or '1' for dirty, for room {complement_location}: "))

    cost, updated_goal_state = clean_room(initial_location, initial_location_status, goal_state, cost)
    goal_state = updated_goal_state

    print(f"Moved to location {complement_location}.")
    cost += 1

    cost, updated_goal_state = clean_room(complement_location, initial_location_complement_status, goal_state, cost)
    goal_state = updated_goal_state

    print(f"Total cost: Rs. {cost}.")
    print(f"Final goal state: {goal_state}")


main()
