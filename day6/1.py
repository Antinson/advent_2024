guard = '^'
obstacle = "#"

new_dict = {}

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
location_history = []


with open('1.txt') as file:
    data = file.read().strip().split('\n')



m = [list(x) for x in data]
guard_location = None


for y, row in enumerate(m):
    for x, value in enumerate(row):
        if value == '^':
            guard_location = [x, y]


y_len = len(m)
x_len = len(m[0])
d_count = 0
current_direction = directions[0]


print(f"Starting at {guard_location}")

while True:

    guard_x = guard_location[0]
    guard_y = guard_location[1]

    new_location = [guard_x + current_direction[0], guard_y + current_direction[1]]



    if new_location[0] < 0 or new_location[1] > x_len - 1:
        print("End X")
        break

    if new_location[1] < 0 or new_location[1] > y_len - 1:
        print('End Y')
        break
    

    if m[new_location[1]][new_location[0]] == "#":
        d_count += 1
        current_direction = directions[d_count % len(directions)]
        continue
    
    
    
    # Next postion is good record location & go next
    location_history.append((guard_x, guard_y))

    guard_location[0] = new_location[0]
    guard_location[1] = new_location[1]




print(len(set(location_history)) + 1)
print(d_count)
