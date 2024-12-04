import re


with open('1.txt') as file:
    data = file.read()

pattern1 = r'mul\((\d+),(\d+)\)'

conditionals = [r'do\(\)', r'don\'t\(\)']


default = True

# re.finditer(pattern, string, flags=0)


ans = 0

for match in matches:
    num1, num2 = match  # Each match is a tuple of the two numbers
    ans += int(num1) * int(num2)

print(ans)

