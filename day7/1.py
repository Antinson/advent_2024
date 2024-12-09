import copy


with open('2.txt') as file:
    data = file.read().strip().split('\n')


def make_combo_list(n):
    p = ['+', '*']
    combos = []
    
    def generate_combos(current_combo, length):
        
        if length == 0:
            combos.append(current_combo)
            return
        
        for symbol in p:
            generate_combos(current_combo + symbol, length - 1)
    
    for length in range(n, n + 1):
        generate_combos('', length)
    
    return combos


def get_result(numbers):

    n = len(numbers) - 1
    combo_list = make_combo_list(n)

    return combo_list


ans = 0

for line in data:
    result, numbers = line.split(':')
    numbers = [int(x) for x in numbers.split(' ') if x]
    
    combo_list = get_result(numbers)

    for combo in combo_list:

        current_numbers = copy.deepcopy(numbers)

        for i in range(len(numbers) - 1):

            
            if combo[i] == "+":
                #print(f"Should be {current_numbers[i]} + {current_numbers[i + 1]}: {current_numbers[i] + current_numbers[i + 1]}")
                current_numbers[i+1] = current_numbers[i] + current_numbers[i + 1]
            
            else:
                #print(f"Should be {current_numbers[i]} * {current_numbers[i + 1]}: {current_numbers[i] * current_numbers[i + 1]}")
                current_numbers[i+1] = current_numbers[i] * current_numbers[i + 1]
        
        #print(f"Current numbers after: {current_numbers}")
        
        print(f"{current_numbers[-1]} vs {int(result)}")

        
        if current_numbers[-1] == int(result):
            ans += int(result)
            break

print(ans)


            



