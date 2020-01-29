import sys
import math 

def do_mean(data):
    tot = 0
    for d in data:
        tot = tot + d
    return tot/len(data)

def do_sv(data):
    mean = do_mean(data)
    tot = 0
    for d in data:
        tot = tot + (d - mean)*(d - mean)
    return round(math.sqrt(tot/len(data)), 1)


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        in_data = open(args[1], 'r')
    else:
        in_data = sys.stdin

    n = int(in_data.readline())
    data = list(map(int, in_data.readline().split()))
    print(do_sv(data))