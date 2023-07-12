import time
import sys

binary = "0000000000"
b0, b1, b2, b3, b4, b5, b6, b7, b8, b9 = binary

count = 0
maxnumber = 1023

print("1023.exe\n")
input("Press enter to start")
time.sleep(1)

while count <= maxnumber:
    calc = count

    if calc < 512:
        b0 = "0"
    elif calc >= 512:
        b0 = "1"
        calc = calc - 512

    if calc < 256:
        b1 = "0"
    elif calc >= 256:
        b1 = "1"
        calc = calc - 256

    if calc < 128:
        b2 = "0"
    elif calc >= 128:
        b2 = "1"
        calc = calc - 128

    if calc < 64:
        b3 = "0"
    elif calc >= 64:
        b3 = "1"
        calc = calc - 64

    if calc < 32:
        b4 = "0"
    elif calc >= 32:
        b4 = "1"
        calc = calc - 32

    if calc < 16:
        b5 = "0"
    elif calc >= 16:
        b5 = "1"
        calc = calc - 16

    if calc < 8:
        b6 = "0"
    elif calc >= 8:
        b6 = "1"
        calc = calc - 8

    if calc < 4:
        b7 = "0"
    elif calc >= 4:
        b7 = "1"
        calc = calc - 4

    if calc < 2:
        b8 = "0"
    elif calc >= 2:
        b8 = "1"
        calc = calc - 2

    if calc < 1:
        b9 = "0"
    elif calc >= 1:
        b9 = "1"
        calc = calc - 1

    binprint = b0 + b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9
    sys.stdout.write("\r%s" % str(binprint))
    sys.stdout.flush()

    count = count + 1
    time.sleep(0.1875)

input("\n\nSequence completed.")
