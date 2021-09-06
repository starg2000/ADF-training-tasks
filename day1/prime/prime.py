import time
import random
try:
    for i in range(1,random.randint(1,1000)):
        c=0
        for j in range(2,i//2+1):
            if i%j==0:
                c+=1
        if c==0 and i!=1:
            print(i)
            time.sleep(5)
except:
    print("error")
