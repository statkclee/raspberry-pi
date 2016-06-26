def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Function using list comprehensions
##def coprimes(c):
##    values = [i for i in range(1,c) if gcd(c,i) == 1]
##    return values

# Function without list comprehensions
def coprimes(c):
    values = []
    for i in range(1,c):
        if gcd(c,i) == 1:
            values.append(i)
    return values

results = coprimes(7)
print(results)
