from array import array
from random import randint
import random
def A(n):
    a = [randint(1,10) for i in range(n)]
    
def A1():
    x = 5
    y = 5
    c = 4
    m = 4
    max = []
    min = 0
    min_i = 0
    array = []
    count = 0

    for i in range(x):
        array.append([])
        max.append(0)
        for j in range(y):
            array[i].append(random.randint(0,10))

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] > max[i]:
                max[i] = array[i][j]
    
    for i in range(len(max)-1):
        if max[i] < max[i+1]:
            min = max[i]
            min_i = i
    print(array)
    array.remove(array[min_i])
    print(array)
    return array


def A2(n):
    ch = []
    array = [randint(0,10) for i in range(n)]

    for i in array:
        if i % 2 == 0 and i != 0:
            ch = i
            break
    
    print(array, ch)

    for i in range(len(array)):
        if array[i] % 2 == 0 and array[i] != 0:
            array[i] += ch

    print(array)


def A3(n):
    a = [randint(0,10) for i in range(n)]
    b = []
    lol = 0
    i = 0

    for k in range(len(a)):
        i = k
        while i != n:
            lol += a[i]
            i += 1
        lol = lol / i
        b.append(lol)
    print(a, b)
A3(5)

