import sys
def compute_hcf(x, y):
    try:
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i 
        return hcf
    except:
        print(error)
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print("The H.C.F. is", compute_hcf(num1, num2))

except:
    print("error")
