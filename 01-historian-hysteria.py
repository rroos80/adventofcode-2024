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

# Now calculate the distance according to the assignment
distance = 0
for i in range(len(list1)):
    delta = abs(list1[i] - list2[i])
    distance += delta

print(f"\nThe total distance for the given list is {distance}.\n")