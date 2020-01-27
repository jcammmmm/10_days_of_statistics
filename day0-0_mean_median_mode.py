import sys


INPUT_PATH = "/home/jcamilo/repo/10_days_of_statistics/day0.in"

def do_mean(data, size):
    sum = 0
    for d in data:
        sum = sum + d
    return round(sum/size, 2)

def do_median(data, size):
    sorted_data = sorted(data)
    if size%2 == 0:
        return (sorted_data[size//2] + sorted_data[size//2 - 1])/2
    else:
        return sorted_data[size//2]

def do_mode(data, size):
    counts = {}
    for d in data:
        if d in counts:
            counts[d] = counts[d] + 1
        else:
            counts[d] = 1
    mode_list = []
    max_count = 0
    for k in counts:
        if counts[k] == max_count:
            mode_list.append(k)
        elif counts[k] > max_count:
            max_count = counts[k]
            mode_list = []
            mode_list.append(k)

    return min(mode_list)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    else:
        fin = sys.stdin
    n = int(fin.readline())
    data = list(map(int, fin.readline().split()))
    print(do_mean(data, n))
    print(do_median(data, n))
    print(do_mode(data, n))