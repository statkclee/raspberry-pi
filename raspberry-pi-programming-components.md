---
layout: page
title: R 파이썬 소프트레이어 클라우드, xwMOOC
subtitle: (파이썬) 프로그래밍 구성요소
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> *  (파이썬) 프로그래밍 구성요소를 이해한다. 
> *  컴퓨터 과학 프로그래밍 구성요소를 학습한다.


### 1. 주석(comment)

프로그램이 커지고 복잡해짐에 따라 가독성은 떨어진다. 형식 언어(formal language)는 촘촘하고 코드 일부분도 읽기 어렵고 무슨 역할을 왜 수행하는지 이해하기 어렵다.

이런 이유로 프로그램이 무엇을 하는지를 자연어로 프로그램에 노트를 달아두는 것은 좋은 생각이다. 
이런 노트를 **주석(Comments)**이라고 하고 `#` 기호로 시작한다.

~~~ {.input}
# 경과한 시간을 퍼센트로 계산
percentage = (minute * 100) / 60
~~~

상기 사례의 경우, 주석 자체가 한줄이다. 주석을 프로그램의 맨 뒤에 놓을 수도 있다.

~~~ {.input}
percentage = (minute * 100) / 60     # 경과한 시간을 퍼센트로 계산
~~~

`\#` 뒤의 모든 것은 무시되기 때문에 프로그램에는 아무런 영향이 없다.

명확하지 않은 코드의 기능을 문서화할 때 주석은 가장 유용하게 된다.
프로그램을 읽는 사람이 코드가 **무엇**을 하는지 이해한다고 가정하는 것은 일리가 있다.
**왜** 그런지를 이유를 설명하는 것은 더욱 유용하다.

다음의 주석은 코드와 중복되어 쓸모가 없다.

~~~ {.input}
v = 5     # assign 5 to v
~~~

다음의 주석은 코드에 없는 유용한 정보가 있다.

~~~ {.input}
v = 5     # velocity in meters/second. 
~~~

좋은 변수명은 주석을 할 필요를 없게 만들지만, 지나치게 긴 변수명은 읽기 어려운 복잡한 표현식이 될 수 있다. 그래서 상충관계(trade-off)가 존재한다.

### 2. 연상되는(mnemonic) 변수명 만들기

변수를 이름 짓는데 단순한 규칙을 지키고 예약어를 피하기만 하다면, 변수이름을 작명할 수 있는 무척이나 많은 경우의 수가 존재한다. 
처음에 이렇게 넓은 선택폭이 오히려 프로그램을 읽는 사람이나 프로그램을 작성하는 사람 모두에게 혼란을 줄 수 있다. 
예를 들어, 다음의 3개 프로그램은 각 프로그램이 달성하려하는 관점에서 동일하지만, 여러분이 읽고 이해하는데는 많은 차이점이 있다.

~~~ {.input}
a = 35.0
b = 12.50
c = a * b
print c

hours = 35.0
rate = 12.50
pay = hours * rate
print pay

x1q3z9ahd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ahd * x1q3z9afd
print x1q3p9afd
~~~

파이썬 인터프리터는 상기 3개 프로그램을 *정확하게 동일하게* 바라보지만, 
사람은 이들 프로그램을 매우 다르게 보고 이해한다. 
사람은 가장 빨리 두 번째 프로그램의 **의도**를 알아차린다. 
왜냐하면 각 변수에 무슨 데이터가 저장될지에 관해서, 프로그래머의 **의도**를 반영하는 변수명을 사용했기 때문이다.

현명하게 선택된 변수명을 *연상기호 변수명("mnemonic variable name")*이라고 한다. 연상되기 좋은 영어 단어 "[mnemonic](http://en.wikipedia.org/wiki/Mnemonic)"은 기억을 돕는다는 뜻으로 자세한 내용은 위키를 참조한다. 
왜 변수를 생성했는지 기억하기 좋게 하기 위해서 연상하기 좋은 변수명을 선택한다.

매우 훌륭하게 들리고, 연상하기 좋은 변수명을 만드는게 좋은 아이디어 같지만, 
기억하기 좋은 변수명은 초보 프로그래머가 코드를 파싱(parsing)하고 이해하는데 걸림돌이 되기도 한다. 
왜냐하면 31(파이썬 2.7), 33(파이썬 3.x)개 밖에 되지 않지만 예약어도 기억하지 못하고,
변수명이 때때로 너무 서술적이라 마치 일반적으로 사용하는 언어처럼 보이고 잘 선택된 변수명처럼 보이지 않기 때문이다.

어떤 데이터를 반복하는 다음 파이썬 코드를 살펴보자. 
곧 반복 루프를 살펴보겠지만, 다음 코드가 무엇을 의미하는지 알기 위해서 퍼즐을 풀어보자.

~~~ {.input}
for word in words:
    print word
~~~

무엇이 일어나고 있는 것일까?
for, word, in 등등 어느 토큰이 예약어일까? 
변수명은 무엇일까? 
파이썬은 기본적으로 단어의 개념을 이해할까? 
초보 프로그래머는 어느 부분 코드가 이 예제와 동일해야만 \emph{하는지} 그리고, 
어느 부분 코드가 프로그래머 선택에 의한 것인지 분간하는데 고생을 한다.

다음의 코드는 위의 코드와 동일하다.

~~~ {.input}
for slice in pizza:
    print slice
~~~

초보 프로그래머가 이 코드를 보고 어떤 부분이 파이썬 예약어이고 어느 부분이 프로그래머가 선택한 변수명인지 알기 쉽다. 
파이썬이 피자와 피자조각에 대한 근본적인 이해가 없고, 피자는 하나 혹은 여러 조각으로 구성된다는 근본적인 사실을 알지 못한다는 것은 자명하다.

하지만, 작성한 프로그램이 데이터를 읽고 데이터에 있는 단어를 찾는다면 `피자(pizza)`와 `피자조각(slice)`은 연상하기 좋은 변수명이 아니다. 이것을 변수명으로 선핸하게 되면 프로그램의 의미를 왜곡시킬 수 있다.

좀 시간을 보낸 후에 가장 흔한 예약어에 대해서 알게 될 것이고, 이들 예약어가 어느 순간 여러분에게 눈에 띄게 될 것이다.

**for** word **in** words**:**
    **print** word 

파이썬에서 정의된 코드 일부분(`for`, `in`, `print`, `:`)은 예약어로 굵게 표시되어 있고, 
프로그래머가 생성한 변수명(`word`, `words`)는 굵게 표시되어 있지 않다. 
대다수 텍스트 편집기는 파이썬 구문을 인지하고 있어서, 
파이썬 예약어와 프로그래머가 작성한 변수를 구분하기 위해서 색깔을 다르게 표시한다. 


### 3. try와 catch를 활용한 예외 처리

함수 `raw_input`과 `int`을 사용하여 사용자가 타이핑한 숫자를 읽어 정수로 파싱하는 프로그램 코드가 다음에 나와 있다.

~~~ {.input}
>>> speed = raw_input(prompt)
~~~
~~~ {.output}
What...is the airspeed velocity of an unladen swallow?
What do you mean, an African or a European swallow?
~~~ {.input}
>>> int(speed)
~~~
~~~ {.output}
ValueError: invalid literal for int()
>>>
~~~

파이썬 인터프리터에서 상기 문장을 실행하면, 인터프리터에서 새로운 프롬프트로 되고, "이런(oops)" 잠시 후에, 다음 문장 실행으로 넘어간다.

하지만, 만약 코드가 파이썬 스크립트로 실행이 되어 오류가 발생하면,
역추적해서 그 지점에서 즉시 멈추게 된다. 다음에 오는 문장은 실행하지 않는다.

화씨 온도를 섭씨 온도로 변환하는 간단한 프로그램이 있다.

~~~ {.input}
inp = raw_input('Enter Fahrenheit Temperature:')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print cel
~~~

이 코드를 실행해서 적절하지 않은 입력값을 넣게 되면, 다소 불친절한 오류 메시지와 함께 간단히 작동을 멈춘다.

~~~ {.input}
python fahren.py
~~~
~~~ {.output} 
Enter Fahrenheit Temperature:72
22.2222222222
~~~
~~~ {.input}
python fahren.py
~~~
~~~ {.output} 
Enter Fahrenheit Temperature:fred
Traceback (most recent call last):
  File "fahren.py", line 2, in <module>
    fahr = float(inp)
ValueError: invalid literal for float(): fred
~~~

이런 종류의 예측하거나, 예측하지 못한 오류를 다루기 위해서 파이썬에는 **try / except**로 불리는 조건 실행 구조가 내장되어 있다.
`try`와 `except`의 기본적인 생각은 일부 명령문에 문제가 있다는 것을 사전에 알고 있고, 
만약 그 때문에 오류가 발생하게 된다면 대신 프로그램에 추가해서 명령문을 실행한다는 것이다. 
`except` 블록의 문장은 오류가 없다면 실행되지 않는다.

문장 실행에 대해서 파이썬 `try`, `except` 기능을 보험으로 생각할 수도 있다.

온도 변환기 프로그램을 다음과 같이 재작성한다.

~~~ {.input}
inp = raw_input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print cel
except:
    print 'Please enter a number'
~~~

파이썬은 `try` 블록 문장을 우선 실행한다. 
만약 모든 것이 순조롭다면, `except` 블록을 건너뛰고, 다음 코드를 실행한다.
만약 `try` 블록에서 `except`이 발생하면, 
파이썬은 `try` 블록에서 빠져 나와 `except`블록 문장을 수행한다.

~~~ {.input}
python fahren2.py
~~~
~~~ {.output} 
Enter Fahrenheit Temperature:72
22.2222222222
~~~

~~~ {.input}
python fahren2.py
~~~
~~~ {.output} 
Enter Fahrenheit Temperature:fred
Please enter a number
~~~

`try`문으로 예외사항을 다루는 것을 **예외 처리한다(catching an exception)**고 부른다.
예제에서 `except` 절에서는 단순히 오류 메시지를 출력만 한다. 
대체로, 예외 처리를 통해서 오류를 고치거나, 재시작하거나, 최소한 프로그램이 정상적으로 종료될 수 있게 한다.

### 4. 논리 연산식의 단락(Short circuit) 평가

`x >= 2 and (x/y) > 2`와 같은 논리 표현식을 파이썬에서 처리할 때, 왼쪽에서부터 오른쪽으로 표현식을 평가한다.
`and` 정의 때문에 `x` 가 2보다 작다면, `x >= 2`은 `거짓(False)`으로, 
전체적으로 `(x/y) > 2` 이 `참(True)` 혹은 `거짓(False)` 이냐에 관계없이 `거짓(False)`이 된다. 

나머지 논리 표현식을 평가해도 나아지는 것이 없다고 파이썬이 자동으로 탐지할 때,
평가를 멈추고 나머지 논리 표현식에 대한 연산도 중지한다. 
최종값이 이미 결정되었기 때문에 더 이상의 논리 표현식의 평가가 멈출 때, 이를 **단락(Short-circuiting) 평가**라고 한다.

좋은 점처럼 보일 수 있지만, 단락 행동은 **가디언 패턴(guardian pattern)**으로 불리는 좀 더 똑똑한 기술로 연계된다.
파이썬 인터프리터의 다음 코드를 살펴보자.

~~~ {.input}
>>> x = 6 
>>> y = 2
>>> x >= 2 and (x/y) > 2
True
>>> x = 1 
>>> y = 0
>>> x >= 2 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and (x/y) > 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 
~~~

세번째 연산은 실패하는데 이유는 `(x/y)` 연산을 평가할 때 `y` 가 0 이어서 실행오류 발생한다.
하지만, 두 번째 예제의 경우 실패하지 않는데 이유는 `x >= 2` 이 `거짓(False)` 으로, 
전체가 `거짓(False)`이 되어 단락(Short-circuiting) 평가 규칙에 의해 `(x/y)` 평가는 실행되지 않아 오류도 발생하지 않는다.

평가 오류를 발생하기 전에 **가디언(gardian)** 평가식을 전략적으로 배치해서 논리 표현식을 다음과 같이 구성한다. 

~~~ {.input}
>>> x = 1
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x = 6 
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x >= 2 and (x/y) > 2 and y != 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>>
~~~

첫 번째 논리 표현식은 `x >= 2` 이 `거짓(False)` 이라 `and`에서 멈춘다.
두 번째 논리 표현식은 `x >= 2` 이 `참(True)`, `y != 0`은 `거짓(False)` 이라 `(x/y)`까지 갈 필요가 없다.
세 번째 논리 표현식은 `(x/y)` 연산이 끝난 후에 `y != 0` 이 수행되어서 오류가 발생한다.

두 번째 표현식에서 `y` 가 0 이 아닐 때만, `(x/y)`을 실행하도록 `y != 0` 이 **가디언(gardian)** 역할을 수행한다고 말할 수 있다.


> #### 왜 함수를 사용하는가? {.callout}
> 
> 프로그램을 함수로 나누는 고생을 할 가치가 있는지 명확하지 않을 수 있다. 다음에 여기 몇 가지 이유가 있다.
> 
> * 문장을 그룹으로 만들어 새로운 함수로 명명하는 것이 프로그램을 읽고, 이해하고, 디버그하기 좋게한다. 
> * 함수는 반복 코드를 제거해서 프로그램을 작고 콤팩트하게 만든다. 나중에 프로그램에 수정사항이 생기면, 단지 한 곳에서만 수정을 하면 된다.
> * 긴 프로그램을 함수로 나누어 작성하는 것은 작은 부분에서 버그를 수정할 수 있게 하고, 이를 조합해서 전체적으로 동작하는 프로그램을 만들 > 수 있다.
> * 잘 설계된 함수는 종종 많은 프로그램에서 유용하게 사용된다. 잘 설계된 프로그램을 작성하고 디버그를 해서 오류가 없이 만들게 되면, 나중에 > 재사용도 용이하다.


#### 5. 재귀 (Recursion)

재귀는 기본 사례를 하나 두고, 가장 간단한 것을 패턴을 반복하여 문제를 해결하는 기법이다.

##### 5.1 숫자 재귀(Recursion)

~~~ {.input}
## 숫자 재귀(recursion)
def sumRecursion(inputNum):
    if inputNum == 1:
        return 1
    else:
        return inputNum + sumRecursion(inputNum-1)

print("합계 : ", sumRecurrsion(10))
~~~

~~~ {.output}
합계 :  55
~~~

##### 5.2 문자 재귀(Recursion): 회문(Palindrome) 

회문은 *madam*이나 *race car*처럼 앞에서 읽는 것이나 뒤에서 읽는 것이 동일한 것을 의미한다.

~~~ {.input}
def wordPalindrome(inputWord):
    if len(inputWord) == 1:
        return True
    else:
        if inputWord[0] == inputWord[-1]:
            return wordPalindrome(inputWord[1:-1])
        else:
            return False

print("회문인가요? ", wordPalindrome("madam"))
print("회문인가요? ", wordPalindrome("a"))
print("회문인가요? ", wordPalindrome("race car"))
print("회문인가요? ", wordPalindrome("hello"))
~~~

~~~ {.output}
회문인가요?  True
회문인가요?  True
회문인가요?  False
회문인가요?  False
~~~

