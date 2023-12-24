def water_jug_problem(capacity_jug1, capacity_jug2, target):
    visited_states = set()
    queue = [((0, 0), [])]

    last_state = None  # Variable to store the last state where the target is achieved

    while queue:
        current_state, steps = queue.pop(0)
        jug1, jug2 = current_state

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        # Check if target is reached
        if jug1 == target or jug2 == target:
            last_state = current_state
            continue  # Skip further exploration, as we only want the last state

        # Fill jug1
        queue.append(((capacity_jug1, jug2), steps + [(jug1, jug2, "Fill Jug 1")]))

        # Fill jug2
        queue.append(((jug1, capacity_jug2), steps + [(jug1, jug2, "Fill Jug 2")]))

        # Empty jug1
        queue.append(((0, jug2), steps + [(jug1, jug2, "Empty Jug 1")]))

        # Empty jug2
        queue.append(((jug1, 0), steps + [(jug1, jug2, "Empty Jug 2")]))

        # Pour water from jug1 to jug2
        pour_to_jug2 = min(jug1, capacity_jug2 - jug2)
        queue.append(((jug1 - pour_to_jug2, jug2 + pour_to_jug2), steps + [(jug1, jug2, "Pour Jug 1 to Jug 2")]))

        # Pour water from jug2 to jug1
        pour_to_jug1 = min(jug2, capacity_jug1 - jug1)
        queue.append(((jug1 + pour_to_jug1, jug2 - pour_to_jug1), steps + [(jug1, jug2, "Pour Jug 2 to Jug 1")]))

    return last_state, steps


def main():
    jug1_capacity = int(input("Enter jug1 capacity: ")) # 4
    jug2_capacity = int(input("Enter jug2 capacity: ")) # 3
    target_capacity = int(input("Enter target capacity: ")) # 2

    last_state, solution_steps = water_jug_problem(jug1_capacity, jug2_capacity, target_capacity)

    if last_state:
        print("Solution Steps:")
        for step in solution_steps:
            print(step)
        
        print("Final State: ", last_state)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()