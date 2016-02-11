from .state import *

def parser(str_filename):
    state = None
    numWarehouses = 0
    file_in = open(str_filename, 'r')
    
    strArr_lines = file_in.readlines():
    for (str_line, i) in zip(strArr_lines, range(0, len(strArr_lines))):
        intArr_values = int(line.split())

        if(i == 0):
            state = State((intArr_values[0], intArr_values[1]), 
                    intArr_values[2], intArr_values[3], intArr_values[4])
        elif(i == 1):
            continue
        elif(i == 2):
            state.add_weights(intArr_values)
        elif(i == 3):
            numWarehouses = intArr_values[0]
        elif(i > 4 && numWarehouses):
            if(!i%2):
                intTup_warehouseLoc = (intArr_values[0], intArr_values[1])
            else:
                intList_items = []
                for item in intArr_values:
                    if !item:
                        break
                    intList_items.append(Item()

        

    fileIn.close()
