import sys

def get_median(data):
    q2 = 0
    sz = len(data)
    if sz%2 == 0:
        q2 = (data[sz//2 - 1] + data[sz//2])//2
    else:
        q2 = data[sz//2]

    return q2

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        in_data = open(args[1], 'r')
    else:
        in_data = sys.stdin

    n = in_data.readline().strip()
    data = list(map(int, in_data.readline().split()))

    data.sort()
    sz = len(data)
    q1 = get_median(data[0:sz//2])
    q2 = get_median(data)

    if sz%2 == 0:
        q3 = get_median(data[sz//2:sz])
    else:
        q3 = get_median(data[sz//2 + 1:sz])

    print(q1)
    print(q2)
    print(q3)