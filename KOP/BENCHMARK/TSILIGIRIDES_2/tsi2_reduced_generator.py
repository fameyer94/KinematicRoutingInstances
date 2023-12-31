scaling = 0.25
scaling_str = '025'

input_filepath = 'Tsiligirides2_reduced_100.txt'
output_filepath = 'Tsiligirides2_reduced_' + scaling_str + '.txt'

with open(input_filepath, 'r') as original:
    data = original.read()

lines = data.split('\n')

instance = []

# iterate over customer nodes
continue_loop = True
counter = 1
while (continue_loop == True):
    line = lines[counter-1].split()

    if (len(line)== 0):
        continue_loop = False
        break
    else:
        id = str(line[0])  # id
        xPosition = float(line[1])*scaling# x
        yPosition = float(line[2])*scaling# y
        prio = str(line[3])


        instance.append({
            'id': id,
            'xPosition': xPosition,
            'yPosition': yPosition,
            'prio': prio
                        })
        counter = counter + 1
print(instance)

fstream = open(output_filepath, 'w')
for elem in instance:
    fstream.write(str(elem['id']) + ' ' + str(elem['xPosition']) + ' ' + str(elem['yPosition']) + ' ' + str(elem['prio']) + '\n')
fstream.close()