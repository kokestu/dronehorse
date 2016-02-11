from state import *

def parser(str_filename):
    state = None
    numWarehouses = 0
    file_in = open(str_filename, 'r')
    
    strArr_lines = file_in.readlines()
    int_numWeights = 0
    int_numOrders = -1
    for (str_line, i) in zip(strArr_lines, range(0, len(strArr_lines))):
        intArr_values = int(line.split())

        if i == 0:
            state = State((intArr_values[0], intArr_values[1]), 
                    intArr_values[2], intArr_values[3], intArr_values[4])
        elif i == 1:
            int_numWeights = 0
        elif i == 2:
            state.add_weights(intArr_values)
        elif i == 3:
            numWarehouses = intArr_values[0]
        elif i >= 4 && numWarehouses:
            if !i%2:
                warehouse_tmp = Warehouse((intArr_values[0], intArr_values[1]),
                        int_numWeights)
            else:
                warehouse_tmp.add_items(intArr_values)
                state.add_warehouse(warehouse_tmp)
                numWarehouses-=1
        else:
            if int_numOrders == -1:
                int_numOrders = intArr_values[0]
            elif i%2:
                order = Order(
            else
                num = dict()
                for value in intArr_values:
                    if value in num.keys():
                        num[value] += 1
                    else:
                        num[value] = 1
                for key in num.keys():
                    order.add_item((0, num[key]))    
    fileIn.close()
