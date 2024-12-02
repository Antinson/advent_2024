with open('1.txt') as file:
    data = file.read().splitlines()





ans = 0

orderings = {'D': 0, 'I': 1}


# Order is 0 decreasing 1 increasing

def pair_check(a, b, new_data, previous_order, state, special=None):

    current_order = None

    if new_data[a] == new_data[b]:
        return False, False
    
    if new_data[0] - new_data[1] > 0:
        current_order = 0
    else:
        current_order = 1
    
    if current_order != previous_order:
        return False, True
    

    if abs(new_data[a] - new_data[b]) > 3:
        return False, False
    
    if new_data[a] == new_data[b]:
        return False, False

    return True, False



for line in data:
    new_data = [int(x) for x in line.split(' ')]
    previous_order = None
    state = True


    for i in range(len(new_data) - 1):

        if i == 0:
            if new_data[0] - new_data[1] > 0:
                previous_order = 0
            else:
                previous_order = 1
    

        curr = i
        n = curr + 1

        result, _ = pair_check(curr, n, new_data, previous_order, state)

        if not result:

            # Next check
            curr = i + 1
            n = curr + 1

            if n < len(new_data):

                result, ordering_v  = pair_check(curr, n, new_data, previous_order, state, True)

                if not result:

                    # Check with original next removed
                    result = pair_check(curr - 1, n - 1, new_data, previous_order, state)
                    
                
                    if not result:
                        state = False
                        break
                    else:
                        i = n - 1
    
    if state:
        ans += 1

print(ans)

            




        






