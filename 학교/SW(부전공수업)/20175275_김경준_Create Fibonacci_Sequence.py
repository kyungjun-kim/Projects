# 피보나치 수열 (반복 기법, Iterative)

def fibo(n) : 
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    L = []
    for i in range(0, n):
        if i <= 1:
            L.append(1)
        else : 
            L.append(L[i-1] + L[i-2])
    return L[n-1]


while True : 
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("iterFibo (%d) = %d, time %.6f" % (nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() -ts
    print("Fibo (%d) = %d, time %.6f" % (nbr, fibonumber, ts))
