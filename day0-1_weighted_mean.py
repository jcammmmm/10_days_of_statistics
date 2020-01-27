import sys

def do_weighted_mean(n, X, W):
    pond_sum = 0
    W_sum = 0
    for i in range(n):
        pond_sum = pond_sum + X[i]*W[i]
        W_sum = W_sum + W[i]
    return round(pond_sum/W_sum, 1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        instream = open(sys.argv[1], 'r')
    else:
        instream = sys.stdin
    
    n = int(instream.readline())
    X = list(map(int, instream.readline().split()))
    W = list(map(int, instream.readline().split()))
    print(do_weighted_mean(n, X, W))