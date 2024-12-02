with open('1.txt') as file:
    data = file.read().splitlines()





ans = 0


# Order is 0 decreasing 1 increasing

def pair_check(a, b, new_data, bad_pairs):

    
    if abs(new_data[a] - new_data[b]) > 3:
        bad_pairs.append([a, b])
        return False
    
    if new_data[a] == new_data[b]:
        bad_pairs.append([a, b])
        return False



def order_check(new_data, bad_pair):

    

    if len(new_data) >= 2:

        if new_data[0] - new_data[1] > 0:
            order = 0
        else:
            order = 1
    
    for i in range(len(new_data) - 1):
        curr = new_data[i]
        n = new_data[i + 1]

        if curr - n > 0 and order == 1:
            return False
        elif curr - n < 0 and order == 0:
            return False





for line in data:
    new_data = [int(x) for x in line.split(' ')]

    state = True
    strikes = 0
    order = 0
    bad_pairs = []

    for i in range(len(new_data) - 1):

        curr = i
        next = i + 1


        result = pair_check(curr, next, new_data, bad_pairs)

        if result == False:
            strikes += 1
        
        if strikes >= 2:
            state = False
    



    print(bad_pairs)

        






