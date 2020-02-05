import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1)*n

def combine(n, r):
    return factorial(n)//(factorial(r)*factorial(n - r))

def pow(n, p):
    f = 1;
    for i in range(p):
        f = f*n;
    return f;

if __name__ == '__main__':
    M = 1.09
    F = 1
    n = 6
    s = 3
    Ptot = 0
    pM = M/(M + F)
    pF = F/(M + F)

    for i in range(n - s + 1):
        x = s + i
        Ptot = Ptot + (combine(n, x)*pow(pM, x)*pow(pF, n - x))

    print(round(Ptot, 3))