import random
import sys
if len(sys.argv) > 1:
    for _ in range(int(sys.argv[1])):  # quantity of numbers to sort
        print(str(random.randint(-2147483648, 2147483647)) + " ")  # full int range
        #print(str(random.randint(-9000000, 9000000)) + " ")  # small range