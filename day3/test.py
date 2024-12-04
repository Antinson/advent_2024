import re


with open('2.txt') as file:
    text = file.read()


mul_pattern = r'mul\((\d+),(\d+)\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"


current_mode = "scan_mul"
combined_pattern = rf"{mul_pattern}|{dont_pattern}|{do_pattern}"


ans = 0

for match in re.finditer(combined_pattern, text):
    matched_text = match.group()

    if current_mode == "scan_mul":

        if matched_text == "don't()":
            current_mode = "scan_do"
        elif re.match(mul_pattern, matched_text):
            
            num1, num2 = re.match(mul_pattern, matched_text).groups()
            num1, num2 = int(num1), int(num2)
            ans += num1 * num2
            print(f"Extracted: {num1}, {num2}")

    
    if current_mode == "scan_do":

        if re.match(do_pattern, matched_text):
            current_mode = "scan_mul"


print(ans)