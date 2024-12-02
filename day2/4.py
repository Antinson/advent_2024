ans = 0

with open('2.txt') as file:
    data = file.read().splitlines()


def safe(line):

    increasing = all(1 <= line[i + 1] - line[i] <= 3 for i in range(len(line) - 1))
    decreasing = all(1 <= line[i] - line[i + 1] <= 3 for i in range(len(line) - 1))

    return increasing or decreasing

def is_really_safe(line):

    if safe(line):
        return True
    
    for i in range(len(line)):
        modified_report = line[:i] + line[i+1:]
        if safe(modified_report):
            return True
    return False


for line in data:
    new_data = [int(x) for x in line.split(' ')]
    if is_really_safe(new_data):
        ans += 1

print(ans)



