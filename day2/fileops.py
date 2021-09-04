import sys
import re

try:
    file = open(sys.argv[1], 'r')
    string = file.read()
    words = re.split('[ \n]', string)
    unique = []
    c_to,c_ing=0,0
    count_dict={}
    word_dict={}
    palindromes=[]
    index=0
    for x in words:
        unique.append(x)
    for x in unique:
        if x.startswith('To'):
            c_to+=1
        if x.endswith('ing'):
            c_ing+=1
        count_dict[x]=unique.count(x)
        word_dict[index]=x
        index+=1
        if x==x[::-1]:
            palindromes.append(x)
    str_max=list(sorted(count_dict.items(),key=lambda x:x[1], reverse=True))[0][0]
    print("count 'To':",c_to,"\ncount 'ing':",c_ing)
    print("repeted string:",str_max)
    print("palindromes:",palindromes)
    print("word dict:",word_dict)
        

    
        

    file.close()

except IOError:
    print('Error')
