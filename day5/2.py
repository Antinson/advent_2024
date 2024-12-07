with open('2.txt') as file:
    data = file.read().strip().split('\n')

class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

first_part = []
second_split = 0
for idx, x in enumerate(data):
    if not x:
        second_split = idx + 1
        break
    else:
        before, after = x.split('|')
        first_part.append((int(before), int(after)))


second_part = data[second_split:]

nodes = [[]] * 1000


def add_tups(l):


    for value in l:
        
        if not nodes[value]:
            new_node = Node(value)
            nodes[value] = new_node

            for x in first_part:
                if x[0] == value:
                    new_node.children.append(x[1])
    

# for tup in first_part:

#     if nodes[tup[0]]:
#         nodes[tup[0]].children.append(tup[1])
#     else:
#         new_node = Node(tup[0])
#         new_node.children.append(tup[1])
    
#         nodes[tup[0]] = new_node

bad_lines = []
def check_result(new):
        

    for i, num in enumerate(new):
        num = int(num)
        prev = new[0:i]

        if prev:
            current_node = nodes[num]
            
            if [int(x) for x in new] == [75,97,47,61,53]:
                pass
            
   
            
            if not current_node:
                continue
            
            for x in prev:

                if int(x) in current_node.children:
                    bad_lines.append(new)
                    return False
             
    return True


ans = 0
        
for a, line in enumerate(second_part):
   
    new = line.split(',')
    to_do = [int(x) for x in new]

    add_tups(to_do)

    result = check_result(new)



    if result:

        n = int(new[len(new) // 2])

        ans += n




def fix_result(new):
        
    le = len(new)

    new_list = [0] * le

    for i, num in enumerate(new):
        
        place = -1

        for x in new:
            if int(x) in nodes[int(num)].children:
                place -= 1
        
        #print(nodes[int(num)].children)
        new_list[place] = num

    
    return new_list


ans = 0

for line in bad_lines:
    
    nw = fix_result(line)
    
    ans += int(nw[len(nw) // 2])

print(ans)



