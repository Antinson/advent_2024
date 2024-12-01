with open('2.txt') as file:
    data = file.read().split('\n')

print(data)

left = []
right = []

for pair in data:
    if pair:
        l, r = pair.split()
        left.append(int(l))
        right.append(int(r))


count_dict = {}


for y in right:
    count_dict[y] = count_dict.get(y, 0) + 1

ans = 0
for c in left:
    test = count_dict.get(c, 0)
    if test >= 1:
        print(f"{c} * {test}")
        ans += c * test


print(ans)

