import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(L, l, u, target):
    if l > u:
        return -1
    else:
        middle = int((l + u) // 2)
        if L[middle] == target:
            idx = middle
            return idx
        elif L[middle] < target:
            return recbinsearch(L, middle + 1, u, target)
        elif L[middle] > target:
            return recbinsearch(L, l, middle - 1, target)


# recbinsearch(numbers, 0, len(numbers), target)

numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]
    ##numbers += [random.randint(0, 10)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]
    ##targets += [random.randint(0, 10)]

ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
