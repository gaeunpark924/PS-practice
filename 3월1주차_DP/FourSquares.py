import math
def fourSquares(n):
    num = math.sqrt(n)
    if num.is_integer():
        return 1
    max_square = int(num)
    for i in range(1,max_square+1):
        if math.pow(i,2) > n:
            break
        elif math.sqrt(n - math.pow(i,2)).is_integer():  #제곱수인지 판별
            return 2

    for i in range(1,max_square+1):
        if math.pow(i,2) > n:
            break
        for j in range(i,max_square+1):
            if math.pow(i,2) + math.pow(j,2)> n:
                break
            elif math.sqrt(n - math.pow(i,2) - math.pow(j,2)).is_integer():
                return 3
    return 4    
n = int(input())
print(fourSquares(n))
