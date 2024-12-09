with open('2.txt') as file:
    data = file.read().strip()

# Parse the disk map
data = [int(x) for x in data]

# Generate the disk layout with IDs and free spaces
current = []
tracking = {}
c_id = 0

for i in range(0, len(data), 2):
    
    file_length = data[i]
    free_space = data[i + 1] if i + 1 < len(data) else 0

    tracking[c_id] = file_length  

    current.extend([c_id] * file_length)  # Add file blocks with their ID
    current.extend(['.'] * free_space)  # Add free spaces
    c_id += 1



left = 0
right = len(current) - 1


while True:

    

    while current[left] != ".":
        left += 1
    
    while current[right] == ".":
        right -= 1
    

    if left > right:
        break

    # Swap
    current[left], current[right] = current[right], current[left]



checksum = 0
for pos, block in enumerate(current):
    if block != '.':  # Skip free spaces
        checksum += pos * block

print("Final checksum:", checksum)
