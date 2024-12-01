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

left.sort()
right.sort()

ans = 0
for x, y in zip(left, right):
    print(f"{x} + {y}")
    ans += abs(x - y)

print(ans)