# Read file into two separata lists
list1 = []
list2 = []

with open('./input/01-input.txt', 'r') as file:
    line = file.readline()
    while line:
        # Split the line into parts
        num1, num2 = map(int, line.split())  # Convert each part to an integer
        list1 += [num1]
        list2 += [num2]
        line = file.readline()

# Sort the lists
list1.sort()
list2.sort()

# Part 1: calculate the distance according to the assignment
distance = 0
for i in range(len(list1)):
    delta = abs(list1[i] - list2[i])
    distance += delta

print(f"\nThe total distance for the given list is {distance}.\n")

# Part 2
# First get the range of values in the second list and store them in a dict
j = occurrence = {}
for i in list2:
    # Skip processing if value has already been counted
    if i == j:
        pass
    n = list2.count(i)
    occurrence[i] = n
    j = i

# Now parse the first list according to the rules to obtain the similarity score
similarity = 0
for i in list1:
    if not i in occurrence:
        j = 0
    else:
        j = occurrence[i]
    similarity += i * j

print(f"The similarity score is {similarity}.\n")