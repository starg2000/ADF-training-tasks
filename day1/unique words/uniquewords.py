import re

try:
    file = open('input.txt', 'r')
    string = file.read()
    words = re.split('[ \n]', string)
    unique = list(set(words))
    
    unique.sort(key=len)
    file.close()
    file_out = open('output.txt', 'w')
    for x in unique:
        file_out.write(x+" ")
        file_out.write(str(len(x))+'\n')
    file_out.close()

except IOError:
    print('Error')
