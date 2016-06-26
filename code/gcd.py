#-*- coding: utf-8 -*-

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(100,46))


# list comprehension을 사용한 함수
def coprimes(c):
    values = [i for i in range(1,c) if gcd(c,i) == 1]
    return values

# list comprehension을 사용하지 않은 함수
##def coprimes(c):
##    values = []
##    for i in range(1,c):
##        if gcd(c,i) == 1:
##            values.append(i)
##    return values

results = coprimes(63)
print("서로수 갯수:",len(results))
