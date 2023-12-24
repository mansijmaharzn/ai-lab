from itertools import permutations

def is_solution(puzzle, mapping):
    sum1 = sum3 = 0
    for word in puzzle[0:len(puzzle)-1]:
        value = 0
        for letter in word:
            value = value * 10 + mapping[letter]
        sum1 += value
    for letter in puzzle[len(puzzle)-1]:
        sum3 = sum3 * 10 + mapping[letter]
    return sum1 == sum3

def solve_cryptarithmetic(puzzle):
    letters = set()
    for word in puzzle:
        for letter in word:
            letters.add(letter)
    letters = sorted(list(letters))
    for perm in permutations(range(10), len(letters)):
        mapping = {letters[i]: perm[i] for i in range(len(letters))}
        if all(mapping[word[0]] != 0 for word in puzzle) and is_solution(puzzle, mapping):
            return mapping
    return None

# Example usage:
puzzle = ['TWO', 'TWO', 'FOUR']
solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution:")
    for word in puzzle:
        value = 0
        for letter in word:
            value = value * 10 + solution[letter]
        print(word, '=', value)
else:
    print("No solution found.")