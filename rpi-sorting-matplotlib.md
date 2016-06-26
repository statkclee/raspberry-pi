---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: matplotlib 그래프 그리기
---

> ### 학습 목표 {.objectives}
>
> * 임의 숫자 리스트 자료를 생성하는데 간단한 `list comprehension` 사용법을 이해한다.
> * `matplotlib`을 사용해서 간단한 그래프를 생성할 수 있다.


정렬 알고리즘 학습이 많은 학생들에게 정말 재미없는 주제다. 학생들로 하여금
다양한 정렬 알고리즘을 작성하게 하고 시각적으로 동작하는 것을 보여줘서
알고리즘이 어떤 작업을 수행하고 있는지 더 잘 파악하도록 이해력을 높여,
조금더 희망을 갖는다면 학습 주제가 학생들에게 좀더 재미있게 다가섰으면 한다.

## 1. 수업 계획

### 1.1. `matplotlib` 설치 

`matplotlib` 팩키지를 설치하려면, 리눅스와 맥/윈도우에서 다음을 실행한다.

#### 1.1.1. 리눅스(데비안 배포판, 라즈비언 포함)

먼저 터미널을 열고 다음 명령어를 실행한다.

~~~ {.shell}
$ sudo apt-get install python3-matplotlib
~~~

#### 1.1.2. 맥 OSX/윈도우 

1. `pip`로 설치하는 경우 터미널 윈도우에서 `pip3 install matplotlib` 명령어를 실행한다.
1. 혹은, [`matplotlib` 웹사이트](http://matplotlib.org/faq/installing_faq.html#how-to-install)에서 직접 설치한다.


### 1.2. `list comprehension` 실습

다음 출력값을 생성하는 파이썬 코드를 `list comprehension`을 사용하여 작성하시오.

~~~ {.output}
[0,1,2,3,4,5,6,7,8,9]            # 1.번 문제 

[5,6,7,8,9]                      # 2.번 문제 

[-9,-8,-7,-6,-5,-4,-3,-2,-1,0]   # 3.번 문제 

[0,2,4,6,8,10]                   # 4.번 문제 

[[0,0,0],[1,1,1],[2,2,2]]        # 5.번 문제 
~~~

~~~ {.python}         
>>> [i for i in range(10)]       # 1.번 문제 
>>> [i for i in range(5,10)]     # 2.번 문제 
>>> [i for i in range(-9,1)]     # 3.번 문제 
>>> [i for i in range(0,11,2)]   # 4.번 문제 
>>> [i for i in range(0,12,2)]   # 4.번 문제 
>>> [[i] * 3 for i in range(3)]  # 5.번 문제 
~~~

### 1.3. 함께 고민하기

시각화 작업을 대부분의 학생들이 마무리한 뒤에, 다음 그래프를 어떻게 생성할 수 있는지 학생들에게 
숙제 혹은 5분 시간을 주고 작업결과를 공유한다.

|                       |                            |                            |
|-----------------------|----------------------------|----------------------------|
|<img src="fig/rpi-algo-figure_6.png" alt="연습문제 1" width="100%">|<img src="fig/rpi-algo-figure_7.png" alt="연습문제 2" width="100%">|<img src="fig/rpi-algo-figure_8.png" alt="연습문제 8" width="100%">|

## 2. 학생 학습지

### 2.1. 들어가며

수학, 과학, 인문학 분야에서 실험 혹은 연구결과로 나온 데이터를 시각하해서 흔히 발표한다.
많은 학문분야에서 사용되는 주요 도구로 `matplotlib` 라이브러리와 함께 파이썬 프로그래밍 언어가 사용된다.
실제로, `matplotlib`은 과학 출간에 사용되는 표준 그래프 도구로 빠르게 자리잡아가고 있다.

이번 학습에서, 파이썬을 사용해서 숫자 리스트를 생성하는 방법을 학습하고 나서, 생성한 숫자를 `matplotlib` 그래프로 시각화하는 방법을 학습한다.

### 2.2. 숫자 리스트 생성하기

리스트는 자료구조로, 자료구조는 데이터를 저장하는 한 방법이다.
파이썬에서 `0`에서 `9`까지 숫자를 저장하고자 한다면 다음과 같이 리스트를 작성한다:

~~~ {.python}
numbers = [0,1,2,3,4,5,6,7,8,9]
~~~

작은 리스트에 대해서 상당히 간단하고 좋지만, `0`에서 `9999`까지 모든 숫자를 리스트에 저장하려면 자료입력 타이핑에 상당한 시간이 소요된다.
프로그래밍할 때 반복적인 작업을 본인 스스로 할 때 아마도 더 쉬운 방식이 있다.
이런 경우에, 10,000 숫자 리스트를 생성하는 간단한 방법은 루프를 사용하는 것이다.

1. 파이썬 IDE를 열고, 다음 명령어를 타이핑하고 `lists.py` 이름으로 새로 파일을 생성한다.

~~~ {.python}

numbers = []
for i in range(100000):
    numbers.append(i)
~~~

2. 코드를 실행시키고, 인터프리터 화면에서 `numbers`를 타이핑하면, 생성한 리스트를 볼 수 있다.

### 2.3. `list comprehension`

루프를 돌려 리스트를 생성하는 것도 꽤 간단하지만, 많은 언어에 **list comprehension** 으로 불리는 더 강력한 방식으로 리스트를 생성시킬 수 있다.
상기 리스트 생성은 다음과 같이 단순화 된다:

~~~ {.python}
numbers = [i for i in range(10000)]
~~~

첫번째 `i`는 리스트에 저장될 값을 지정한다; 두번째 `i`는 0에서 10000 사이 모든 값을 표현한다.

`list comprehension`을 사용해서 다음 리스트를 생성하시오.

~~~ {.output}
[0,1,2,3,4,5,6,7,8]                     # 1번 연습

[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # 2번 연습
~~~

`list comprehension`에 `range()` 함수에 모수 범위를 잘 이용할 수도 있다.
만약 `[5,6,7,8,9]` 리스트를 생성하려면 다른 값에서 시작하면 된다. 예를 들어, 다음과 같이 코드를 작성하면 된다.

~~~ {.python}
numbers = [i for i in range(5,10)
~~~

`list comprehension`을 사용해서 다음 리스트를 생성하시오.

~~~ {.output}
[10,11,12,13,14,15,16,17,18,19]       # 1번 연습

[-5,-6,-7,-8,-9,0]                    # 2번 연습
~~~

`range()` 함수에 건너뛰기 값을 전달해서 `[0,2,4,6,8]` 처럼 건너뛰는 숫자 리스트를 생성할 수도 있다.

~~~ {.python}
numbers = [i for i in range(0,10,2)]
~~~

아래 리스트를 생성하는데 `list comprehension`을 사용해서 파이썬 코드를 작성해본다.

~~~ {.output}
[0,3,6,8,12]                # 1번 연습

[10,8,6,4,2,0]              # 2번 연습 

[0,-1,-2,-3,-4,-5]          # 3번 연습
~~~

### 2.4. 숫자 리스트를 그래프 그리기

1. 표준 그래프를 생성하려면, 두 집합의 값이 필요하다. 새로운 파이썬 코드 파일을 열고 `graphing.py`로 이름 짓고 저장한다.

2. 그래프로 도식화하는데 두 숫자 리스트를 생성하고서 시작한다.
어떤 숫자가 리스트에 담길지는 그다지 문제가 되지 않지만, 두 숫자 리스트 길이는 같아야 된다.
숫자 리스트 길이를 같도록 하는데 파이썬 내장함수 `len()`를 사용한다. 리스트를 `y`, `x`로 부르기로 한다:

~~~ {.python}
y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]
~~~

3. 숫자가 준비되어서, 숫자 데이터를 그래프로 생성할 수 있다.
이 작업을 위해서 `matplotlib` 라이브러리를 사용한다. 파일 상단에 다음 코드를 작성해서 적어 놓는다.

~~~ {.python}
import matplotlib.pyplot as plt
~~~

4. 숫자를 간단한 산점도로 표현하는데, 파일 하단에 다음 두 줄을 적어놓기만 하면 된다.

~~~ {.python}
plt.scatter(x,y)
plt.show
~~~

5. 전체 파일은 다음과 같아보이면 된다.

~~~ {.python}
import matplotlib.pyplot as plt

y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]

plt.scatter(x,y)
plt.show()
~~~

6. 윈도우가 팝업되면서 다음 그래프가 담겨져 나타난다.

<img src="fig/rpi-algo-figure_1.png" alt="연습문제 1" width="50%">

7. 그래프가 담긴 윈도우를 닫고, 다른 스타일 그래프를 그려보자. 산점도를 선형 그래프를 갖도록 변경한다.

~~~ {.python}
plt.scatter(x,y)
plt.show()
~~~

상기 코드부분을 다음과 같이 변경한다.

~~~ {.python}
plt.plot(x,y)
plt.show()
~~~

위와 같이 코드를 변경하고 코드를 재실행한다.

8. 점과 선을 함께 산점도로 표현하려면, `plot`과 `scatter`를 조합한다:

~~~ {.python}
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
~~~

<img src="fig/rpi-algo-figure_2.png" alt="연습문제 2" width="50%">

9. `list comprehension` 에서 `y` 값을 변경해서, 다음 그래프 세개를 생성시키시오.
    * `plt.bar` 사용해서 막대그래프를 생성한다.

|                       |                            |                            |
|-----------------------|----------------------------|----------------------------|
|<img src="fig/rpi-algo-figure_3.png" alt="연습문제 3" width="100%">|<img src="fig/rpi-algo-figure_4.png" alt="연습문제 4" width="100%">|<img src="fig/rpi-algo-figure_5.png" alt="연습문제 5" width="100%">|

### 2.5. 인터랙티브, 임의 랜덤 그래프 그리기

이번 학습을 마치게 되면, 값이 변경될 때 자동으로 갱신되는 인터랙티브 그래프를 생성하는 방법을 학습할 것이다.

1. `random_plot.py` 로 불리는 파일을 새롭게 생성하시오.

2. `matplotlib` 팩키지 외에 추가로 라이브러리 몇개가 더 필요하다. 파일 상단에 다음 세줄을 추가한다:

~~~ {.python}
import matplotlib.pyplot as plt
from time import sleep
from random import shuffle
~~~

3. 그리고 나서, 프로그램에 `인터랙티브 그래프 그리기(interactive plotting)` 기능을 활성화 시킨다.

~~~ {.python}
plt.ion()
~~~

4. `x`, `y` 리스트를 지정한다:

~~~ {.python}
x = [i for i in range(100)]
y = [i for i in range(len(y))]
~~~

5. 루프를 사용해서 그래프를 갱신하고, `y` 리스트를 뒤섞어서 값이 계속해서 변경하도록 한다.
매번 그래프를 새로 시작해서 이전 그래프가 겹쳐지지 않도록 한다. 다음 코드 각 줄에 주석이 달려있어 어떤 역할을 수행하는지 확인한다.

~~~ {.python}
for i in range(50): # 50 회 반복한다.
    plt.clf()       # 그래프를 초기화한다.
    plt.bar(x,y)    # 막대 그래프를 그린다.
    plt.show()      # 막개 그래프를 화면에 표시한다.
    sleep(0.5)      # 0.5초 프로그램 실행을  멈춘다.
    shuffle(y)      # 데이터를 뒤섞는다.
~~~

6. 라이브 그래프를 보려면 다음 코드를 실행시킨다. 오류가 발생되면, 다음 코드와 비교해서 동일한지 확인한다.

~~~ {.python}
import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

plt.ion()

y = [i for i in range(100)]
x = [i for i in range(len(y))]

for i in range(50): # 50 회 반복한다.
    plt.clf()       # 그래프를 초기화한다.
    plt.bar(x,y)    # 막대 그래프를 그린다.
    plt.show()      # 막개 그래프를 화면에 표시한다.
    sleep(0.5)      # 0.5초 프로그램 실행을  멈춘다.
    shuffle(y)      # 데이터를 뒤섞는다.
~~~

<img src="fig/rpi-algo-anim.gif" alt="임의 인터랙티브 그래프" width="50%">

### 2.6. `matplotlib` 심화

`matplotlib` 을 사용해서 정교한 과학 그래프를 생성할 수 있는데 그래프 제목과 
각축에 표식도 포함시킬 수 있다. 인터넷을 찾아 그래프에 제목과 축표식을 추가하는 방법을 찾아 적용시킨다.