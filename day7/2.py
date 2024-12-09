import copy
from itertools import product


with open('2.txt') as file:
    data = file.read().strip().split('\n')


def make_combo_list(n):
    return product("*+|", repeat=len(numbers) - 1)

ans = 0

found_match = False

for x, line in enumerate(data):
    
    result, numbers = line.split(':')
    numbers = [int(x) for x in numbers.split(' ') if x]
    
    combo_list = make_combo_list(len(numbers) - 1)

    for combo in combo_list:

        previous = None

        for i in range(len(numbers) - 1):

            if i == 0:
                if combo[i] == "+":
                    previous = numbers[i] + numbers[i + 1]
                
                elif combo[i] == "*":
                    previous = numbers[i] * numbers[i + 1]
                else:
                    previous = int(str(numbers[i]) + str(numbers[i + 1])) 
            
            if combo[i] == "+":
                previous += numbers[i + 1]
            
            elif combo[i] == "*":
                previous *= numbers[i + 1]
            else:
                previous = int(str(previous) + str(numbers[i + 1])) 

            


        
        if previous == int(result):
            print(f"[{x:02}/{len(data)}] WORKS", combo, previous)
            ans += int(result)
            break
        

print(ans)


            



