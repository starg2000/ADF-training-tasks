import sys
try:
    dec = int(sys.argv[1])

    print("The decimal value of", dec, "is:")
    print(bin(dec), "in binary.")
    print(oct(dec), "in octal.")
    print(hex(dec), "in hexadecimal.")
except ValueError:
    print(" error in value")
