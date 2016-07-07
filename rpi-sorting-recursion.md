---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 재귀(recursion)
---

> ### 학습 목표 {.objectives}
>
> * 용어 '재귀(recursion)' 의미를 이해한다.
> * 계승(factorial)과 최대공약수를 재귀적으로 구현한다.
> * 파이썬으로 단순한 재귀 알고리즘을 구현한다.


정렬 알고리즘 학습이 많은 학생들에게 정말 재미없는 주제다. 학생들로 하여금
다양한 정렬 알고리즘을 작성하게 하고 시각적으로 동작하는 것을 보여줘서
알고리즘이 어떤 작업을 수행하고 있는지 더 잘 파악하도록 이해력을 높여,
조금더 희망을 갖는다면 학습 주제가 학생들에게 좀더 재미있게 다가섰으면 한다.

## 1. 수업 계획

### 1.1. 삽입 정렬 

다음 Gif 애니메이션을 학생들에게 보여주거나, 아래 파이썬 코드를 실행시킨다.

<img src="fig/rpi-algo-tree-anim.gif" alt="재귀 나무 Gif 애니메이션" width="50%">

~~~ {.python}
import turtle
t = turtle.Turtle()
win = turtle.Screen()

t.pu()
t.bk(300)
t.pd()

def tree(length,t):
    if length < 5:
        return None
    else:
        t.forward(length)
        t.right(60)
        tree(length-30,t)
        t.left(120)
        tree(length-30,t)
        t.right(60)
        t.backward(length)

tree(180,t)
~~~

* 거북이가 나무를 그려나가면서 어떤 작업을 수행했는지 학생들이 설명하게 만든다.
* 학생들에게 코딩해서 거북이가 나무를 어떻게 그려나갈 것인지 묻는다.
* 알고리즘에서 가장 작은 부분을 인지하게 한다.

### 1.3. 해답

#### 서로소(co-primes)

서로소는 여러 개의 수들 사이에 1 이외의 공약수가 없다.

~~~ {.python}
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# list comprehension을 사용한 함수
def coprimes(c):
    values = [i for i in range(1,c) if gcd(c,i) == 1]
    return values

# list comprehension을 사용하지 않은 함수
def coprimes(c):
    values = []
    for i in range(1,c):
        if gcd(c,i) == 1:
            values.append(i)
    return values

results = coprimes(63)
~~~

#### 회문(Palindrome)

회문(Palindrome)은 madam이나 nurses run처럼 앞에서부터 읽으나 뒤에서부터 읽으나 동일한 단어나 구를 일컫는다. 

~~~ {.python}
def find_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return find_palindrome(word[1:-1])
    else:
        return False

if find_palindrome('abcdefedcba'):
    print('Yep')
~~~

### 피보나치 수

피보나치 수는 수열 1, 1, 2, 3, 5, 8, 13 …처럼 1로 시작하고, 앞 두 수의 합이 그 다음 수로 이뤄진 수열을 말한다.

~~~ {.python}
def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)

print(fib(20))
~~~

### 1.2. 함께 고민하기

시작 부분에서 학생들에게 보여준 파이썬 코드에서 재귀 호출과 함수 기본(base case)을 식별하도록 한다.

~~~ {.python}
import turtle
t = turtle.Turtle()
win = turtle.Screen()

t.pu()
t.bk(300)
t.pd()

def tree(length,t):
    if length < 5:
        return None
    else:
        t.forward(length)
        t.right(60)
        tree(length-30,t)
        t.left(120)
        tree(length-30,t)
        t.right(60)
        t.backward(length)

tree(180,t)
~~~


## 2. 학생 학습지

최종 정렬 알고리즘을 학습하기 전에, 컴퓨터 과학에 있어 **재귀(recurssion)** 라는 강력한 개념을 학습한다.

### 2.1. 계승(factorial) 구하기 

매우 단순한 알고리즘으로 시작한다.
숫자 10 계승을 구한다고 상상하자. 결과는 $10 \times 9 \times 8 \times  7 \times  6 \times 5 \times 4 \times 3 \times 2 \times 1 = 3628800$이 된다.
간단한 루프를 사용해서 문제를 해결할 수도 있지만,
재귀적으로 문제를 같은 유형의 더 작은 문제로 쪼개고 나서 일반적인 해법을 적용시킨다.

'10의 계승을 구하라' 문제를 다시 표현하면, '9의 계승을 구하고 10을 곱하라' 혹은 심지어
'(10-1)의 계승을 구하고 10을 곱하라'와 같이 표현할 수 있다.
물론, 기존 문제 대신에 '(10-1)의 계승을 구하라'라는 새로운 문제가 있지만, 동일한 방식으로 문제를 해결할 수 있다.
8의 계승을 구하고 9를 곱하고 나서 10을 곱한다. 이런 방식으로 계속 진행되면 1의 계승을 구하는 곳까지 다다르게 된다.
이 지점에서 알고리즘은 정지된다. 이 지점을 **기본 사례(base case)** 라고 부른다.

1. 코드로 다음과 같이 작성한다:

~~~ {.python}
def factorial(n):                       # 숫자 n에 대한 계승을 구한다.
    if n == 1:                          # 만약 숫자가 1 이면 기본 사례에 해당
        return 1                        # 1의 누승은 1이라, 그대로 1을 반환
    else:                               # 숫자가 1보다 크면,
        return n * factorial(n-1)       # 숫자를 하나 내려서 그 숫자와 곱한다.

print(factorial(10))                    # 10의 계승을 구하고 출력한다.
~~~

2. 코드를 돌려보고, 화면에 표시된 해답을 확인한다.

3. 알고리즘이 어떻게 돌고 있는지 내부를 살펴보는데, `print` 문을 넣으면 도움이 된다.

~~~ {.python}
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
~~~

상기 코드를 실행시키면, **기본 사례** 까지 도달할 때까지 실제 정답이 제공되지 않는 점을 알아채야만 된다.
다른 모든 함수 호출은 **콜스택(call stack)** 에 저장된다. 기본 사례가 식별되면,
최종 정답에 도달할 때까지 콜스택을 따라 정답이 도출된다.

### 2.2. 최대 공약수 찾기

재귀를 사용하는 또다른 알고리즘은 최대공약수를 찾아내는 것이다. 이 알고리즘은 기원전 300년 경에 유클리드라는 그리스 수학자가 실제로 발견한 것이다.

숫자 두개가 있다고 가정하고, 두 숫자(정확하게 100과 46)를 나울 수 있는 가장 큰 숫자를 찾아보자.
더 작은 숫자가 더 큰 숫자를 정확하게 나눌 수 있다면, 작은 숫자가 최대공약수가 된다.
이것이 **기본 사례** 에 해당된다. 만약 그렇지 않다면, 나눗셈 나머지를 찾아야 된다.
파이썬에서, 나머지 연산자(`%`)를 사용해서 나눗셈 나머지를 찾아낸다.

~~~ {.python}
100 % 46
~~~

인터프리터에 상기 식을 타이핑하면 정답이 `8` 이 나온다. `46` 을 `8` 로 나눠서 나머지를 찾아낸다.

~~~ {.python}
46 % 8
~~~

상기 명령어를 실행시키면 `6` 이 정답니다. 다시 한번 나머지를 찾아본다:

~~~ {.python}
8 % 6
~~~

이제 정답은 `2`가 된다:

~~~ {.python}
6 % 2
~~~

이제 정답은 `0`이 된다. 따라서 `2`는 `6` 을 정확히 나누게 된다.
**기본 사례** 에 도달했기 때문에, `2` 가 `100`과 `46`의 최대공약수로 말할 수 있게 된다.

앞선 계산결과를 사용해서 동일한 계산을 여러번 수행한 것을 알 수 있다.
따라서, 이런 유형의 문제가 재귀로 풀 수 있는 완벽한 후보다:

~~~ {.python}
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
~~~

본 알고리즘은 암호학에서 엄청나게 중요하다. 두 숫자의 최대공약수가 1을 갖는 서로소인 두 숫자를 찾아내는 것이 암호학에서 흔히 필요하다.

~~~ {.python}
gcd(1022,2011)
~~~

`gcd()` 함수를 사용해서 임의 숫자가 포함하는 서로수 숫자를 세는 알고리즘을 작성할 수 있나요? 숫자 `63`은 얼마나 많은 서로수가 있나요?


### 2.3. 회문인가?

회문은 뒤에서 읽어도 앞에서부터 읽는 것과 같이 읽히는 단어다. 예를 들어, 단어 `hannah`는 회문이다.

단어가 회문인지 아닌지 검사하는 것은 단순한 과정이다.
첫번째 단어와 마지막 단어가 같은지 검사한다. 그리고 처음과 끝 단어를 제거하고 나서, 다시 처음과 끝 단어를 검사한다. 이를 계속 반복한다. 만약 단어가 1 혹은 그보다 적은 단어만 갖게 되면, 해당 단어는 회문이다. 회문에서 재귀를 적용할 가능성이 보이는가?

문자열이 회문인지 아닌지를 판단하는 회문 알고리즘을 작성할 수 있는 살펴보자.

다음에 파이썬 유사코드(pseudocode)가 있어 도움을 될 것이다:

~~~ {.python}
function find_palindrome(word)
if 단어 길이가 1 혹은 0, 그렇다면 회문.
if 첫번째와 마지막 문자가 같다면, find_palindrome(첫번째와 마지막 문자는 제거된 단어)
그렇지 않는 경우, 회문이 아님.
~~~

도움이 될 수 있는 코드가 다음에 나와 있다:

~~~ {.python}
'my string'[0] # 문자열 첫번째
'my string'[-1] # 문자열 마지막
'my string'[1:-1] # 첫번째와 마지막 문자열 제거
~~~

### 2.4. 피보나치 수열

피보나치 수열은 `1,1`로 시작하고 나서 마지막 숫자와 앞선 숫자를 더해 나가는 수열이다.

~~~ {.output}
1, 1, 2, 3, 5, 8, 13, 21...
~~~

`n` 번째 피보나치 숫자를 찾고자 한다고 상상하자. 어떻게 작업을 완수할 수 있을까?

희망적으로, 이 문제 대한 재귀적 해법이 존재한다는 것이 보이기 시작한다.
필요로하는 작업은 `n-1` 번째 피보나치 숫자를 찾아 `n-2` 번째 피보나치 숫자와 더하게 되면 `n`번째 피보나치 숫자가 된다.

재귀 알고리즘을 작성해서 `n` 번째 피보나치 숫자를 찾아낸다. 아래 숫자를 사용해서 작성한 알고리즘을 검증한다.

~~~ {.output}
The 10th Fibonacci number is 55
The 2nd Fibonacci number is 1
The 20th Fibonacci number is 6765
~~~

*주의:* 재귀적인 해법이 항상 최선의 해법은 아니다. 재귀 알고리즘으로 너무 큰 숫자를 처리하려고 하면 상당한 시간이 소요된다. 


