# Find the second largest distinct element in an array.
A = []
n = int(input("Enter the array size: "))

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    A.append(value)

largest = float('-inf')
second_largest = float('-inf')

for value in A:
    if value > largest:
        second_largest = largest
        largest = value
    elif value > second_largest and value != largest:
        second_largest = value

print("Second largest element:", second_largest)
print(largest)
### i=0 value=10 sl=0 L=10
### i=1 value=23 sl=10 L=23
### i=2 value=12 sl=12 L=23
### i=3 value=45 sl=23 L=45