import sys

def geom(p, trials):
    return ((1 - p)**(trials - 1))*p

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        in_data = open(args[1], 'r')
    else:
        in_data = sys.stdin

    num_den = list(map(int, (in_data.readline().split())))
    t = int(in_data.readline().strip())
    p = num_den[0]/num_den[1]

    tot = 0
    for i in range(1, 6):
        tot = tot + geom(p, i)

    print(round(tot, 3))




