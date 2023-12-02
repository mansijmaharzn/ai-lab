def main():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    initial_location = input("Enter location of vaccum: (A or B): ").upper()[0]
    initial_location_status = int(input(f"Enter '0' for clean or '1' for dirty, for room {initial_location}: "))
    initial_location_complement_status = int(input("Enter '0' for clean or '1' for dirty, for next room: "))

    if initial_location == "A":
        print("Cleaner is in location A.")
        if initial_location_status == 1:
            print("Room is dirty. Started Cleaning...")
            goal_state["A"] = '0'
            cost += 1
            print("Room cleaned.")

            if initial_location_complement_status == 1:
                print("Moved to location B.")
                cost += 1
                print("Room is dirty. Started Cleaning...")
                goal_state["B"] = '0'
                cost += 1
                print("Room cleaned.")
            
            else:
                print("Room B is already cleaned.")
        
        else:
            print("Room A is already cleaned.")
            if initial_location_complement_status == 1:
                print("Moved to location B.")
                cost += 1
                print("Room is dirty. Started Cleaning...")
                goal_state["B"] = '0'
                cost += 1
                print("Room cleaned.")
            
            else:
                print("Room B is already cleaned.")


    else: # initial location B
        print("Cleaner is in location B.")
        if initial_location_status == 1:
            print("Room is dirty. Started Cleaning...")
            goal_state["B"] = '0'
            cost += 1
            print("Room cleaned.")

            if initial_location_complement_status == 1:
                print("Moved to location A.")
                cost += 1
                print("Room is dirty. Started Cleaning...")
                goal_state["A"] = '0'
                cost += 1
                print("Room cleaned.")
            
            else:
                print("Room A is already cleaned.")
        
        else:
            print("Room B is already cleaned.")
            if initial_location_complement_status == 1:
                print("Moved to location A.")
                cost += 1
                print("Room is dirty. Started Cleaning...")
                goal_state["A"] = '0'
                cost += 1
                print("Room cleaned.")
            
            else:
                print("Room A is already cleaned.")

    print(f"Total cost: Rs. {cost}.")
    print(f"Final goal state: {goal_state}")


main()