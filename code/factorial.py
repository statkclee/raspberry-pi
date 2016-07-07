#-*- coding: utf-8 -*-

##def factorial(n):                       # 숫자 n에 대한 계승을 구한다.
##    if n == 1:                          # 만약 숫자가 1 이면 기본 사례에 해당
##        return 1                        # 1의 누승은 1이라, 그대로 1을 반환
##    else:                               # 숫자가 1보다 크면,
##        return n * factorial(n-1)       # 숫자를 하나 내려서 그 숫자와 곱한다.
##
##print(factorial(10))                    # 10의 계승을 구하고 출력한다.

def factorial(n):
    print("Finding the factorial of",n)
    if n == 1:
        print(n)
        return 1
    else:
        answer = n * factorial(n-1)
        print("The answer is",answer)
        return answer

print(factorial(10))
