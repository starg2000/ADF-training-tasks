
try:
    c = input()
    print("The ASCII value of '" + c + "' is", ord(c))
except TypeError:
    print("type error")
    
