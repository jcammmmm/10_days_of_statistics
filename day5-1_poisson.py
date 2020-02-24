import sys
import math

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        in_data = open(args[1], 'r')
    else:
        in_data = sys.stdin

    lambd = float(in_data.readline())
    K     = int(in_data.readline())

    P     = ((math.e**-lambd)*(lambd**K))/math.factorial(K)
    print(round(P, 3))
