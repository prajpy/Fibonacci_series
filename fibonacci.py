#generating fibonacci series  0 1 1 2 3 5 8 13 21

def fibonacci(n):
    fbseries = []
    for i in range(1,n+1):
        if i==1:
            fbseries.append(0)
        elif i<=3:
            fbseries.append(1)
        elif i>3:
            result = (fbseries[i-2])+(fbseries[i-3])
            fbseries.append(result)
    return fbseries

print(fibonacci(9))