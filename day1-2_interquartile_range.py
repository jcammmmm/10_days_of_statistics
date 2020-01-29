import sys

# assumes data already sorted
def get_median(data):
    q2 = 0
    sz = len(data)
    if sz%2 == 0:
        q2 = (data[sz//2 - 1] + data[sz//2])/2
    else:
        q2 = data[sz//2]

    return q2 + 0.0

# assumes data already sorted
def get_quartiles(data):
    sz = len(data)
    q1 = get_median(data[0:sz//2])
    q2 = get_median(data)

    if sz%2 == 0:
        q3 = get_median(data[sz//2:sz])
    else:
        q3 = get_median(data[sz//2 + 1:sz])
    
    return q1, q2, q3

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        in_data = open(args[1], 'r')
    else:
        in_data = sys.stdin

    n = int(in_data.readline().strip())
    X = list(map(int, in_data.readline().split()))
    F = list(map(int, in_data.readline().split()))
    data = []

    for i in range(n):
        for j in range(F[i]):
            data.append(X[i])

    data.sort()                
    q1, q2, q3 = get_quartiles(data)
    print(round(q3 - q1, 1))
