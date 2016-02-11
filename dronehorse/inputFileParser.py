import state

def parser(str_filename):
    state = None
    file_in = open(str_filename, 'r')
    
    strArr_lines = file_in.readlines():
    for (str_line, i) in zip(strArr_lines, range(0, len(strArr_lines))):
        intArr_values = int(line.split())

        if(str_line == 0):
            state = State((intArr_values[0], intArr_values[1]), intArr_values[2],  
            
        

    fileIn.close()
