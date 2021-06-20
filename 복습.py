def sum_another(a):
    global n
    n = a*(a+1)//2
    return n

n = 0
print(sum_another(5))

