---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 거품 정렬(bubble sort)
---

> ### 학습 목표 {.objectives}
>
> * 거품 정렬 알고리즘 작동방식과 성능에 대해 이해한다.
> * 튜플을 풀어(tuple unpacking) 변수를 교환한다.
> * 알고리즘 성능을 비판적으로 분석하고 약점을 식별한다.


정렬 알고리즘 학습이 많은 학생들에게 정말 재미없는 주제다. 학생들로 하여금
다양한 정렬 알고리즘을 작성하게 하고 시각적으로 동작하는 것을 보여줘서
알고리즘이 어떤 작업을 수행하고 있는지 더 잘 파악하도록 이해력을 높여,
조금더 희망을 갖는다면 학습 주제가 학생들에게 좀더 재미있게 다가섰으면 한다.

## 1. 수업 계획

### 1.1. 거품정렬 

거품정렬 알고리즘을 기술하거나, 인터넷에서 볼 수 있는 동영상이나 다음 GiF 애니메이션을 보여준다.

<img src="fig/rpi-algo-bubble-anim.gif" alt="거품정렬 알고리즘 Gif 애니메이션" width="50%">

혹은, *거품정렬 춤* 을 추도록 학생들에게 유도할 수도 있다.

> ### 언플러그드 활동 동영상  {.prereq}
> 
> <iframe width="560" height="315" src="https://www.youtube.com/embed/8vpOOgO-OKQ" frameborder="0" allowfullscreen></iframe>

### 1.2. 함께 고민하기

거품 정렬 알고리즘 효율성에 대해 의견제시를 유도한다. 불필요하게 낭비되는 연산이 있었는지 물어본다.
예를 들어, 정렬된 리스트에 대해 `for` 루프가 항상 실행된다. 

인터넷을 찾아 *최적* 거품정렬에 대한 예제를 찾아서 왜 향상된 알고리즘인지에 대해 설명한다.


## 2. 학생 학습지

### 2.1. 들어가며

거품정렬 알고리즘은 리스트를 파고들어, 만약 정렬되지 않았다면 리스트에 원소를 바꾸는 과정을 반복해서 리스트를 정렬해 나간다. 다음과 같은 작은 리스트가 있다고 가정하자.

~~~ {.output}
[4,3,6,1]
~~~

알고리즘은 첫 두 리스트 원소(`4`와 `3`)를 비교하면서 시작된다. 정렬되지 않았기 때문에,
교환해서 다음과 같이 된다:

~~~ {.output}
[3,4,6,1]
~~~

다음으로 `4`와 `6`이 비교된다. 올바르게 정렬되어 있어 그대로 둔다. 그리고 나서 `6`과 `1`이 비교되어,
순서를 교환해서 다음과 같이 된다:

~~~ {.output}
[3,4,1,6]
~~~

상기 리스트는 아직 정렬이 되지 않았다. 그래서, 알고리즘이 다시 처음으로 돌아간다.
그리고 나서 모든 숫자가 정렬될 때까지, 숫자를 비교하고 더 큰 숫자를 위쪽으로 *거품으로 끓어 올리는 과정(bubble)*  을 반복한다.

### 2.2. 유용한 함수

~~~ {.python}
import matplotlib.pyplot as plt
from random import shuffle

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.draw()
~~~

`create_random_list` 함수는 난수를 갖는 리스트를 생성하고, `display` 함수는 리스트를 인자로 받아 막대그래프로 시각화한다.
상기 코드를 복사해서 `sorting.py` 이름을 갖는 파일로 새로 저장시킨다.

### 2.3. 변수 교환

1. 거품정렬 알고리즘의 핵심은 리스트에 있는 원소를 교환하는데 있다.
서로 다른 값을 갖는 두 변수를 갖고 생각해보자. 다음 코드를 파이썬 인터프리터에 타이핑한다.

~~~ {.python}
>>> foo = 'first'
>>> bar = 'second'
~~~

2. 어떻게 하면 두변수를 쉽게 교환할 수 있을까? 즉, `foo`는 `second`가 되고, `bar`는 `first`가 된다.
이 작업을 달성하는 첫번째 방법은 *보관 변수(hold variable)* 를 사용하는 것이다. 파이썬 인터프리터에 다음을 타이핑한다.

~~~ {.python}
>>> hold = foo
>>> foo = bar
>>> bar = hold
~~~

3. `foo`와 `bar`를 인터프리터에 타이핑한다. 그러면 두 변수 값이 바뀐것을 확인할 수 있다.

4. 파이썬에, 변수값을 바꾸는 더 쉬운 방식이 있다. `foo`와 `bar` 변수에 다시 값을 대입시키고 출발해 봅시다:

~~~ {.python}
foo = 'first'
bar = 'second'
~~~

5. 이제 변수값을 바꾸는데, 명령어가 단 한줄이면 된다:

~~~ {.python}
foo, bar = bar, foo
~~~

6. `foo`와 `bar` 값을 인터프리터에서 점검한다. 그러면, 두 변수값이 교환된 것을 확인할 수 있다.


### 2.4. 리스트에 원소 교환

1. 동일한 과정이 리스트에 저장된 원소를 교환하는데 사용된다. `sorting.py` 파일 하단에 다음 코드를 타이핑하여 저장한다.

~~~ {.python}
some_list = [3,2,1]
~~~

2. 리스트를 정렬하는데, 각 원소를 교환할 필요가 있다:

~~~ {.python}
some_list = [3,2,1]
some_list[0], some_list[1] = some_list[1], some_list[0]
some_list[1], some_list[2] = some_list[2], some_list[1]
some_list[0], some_list[1] = some_list[1], some_list[0]
print(some_list)
~~~

3. `display()` 함수를 사용해서 전체 과정을 시각화해서 볼 수 있다.

~~~ {.python}
some_list = [3,2,1]
display(some_list)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
some_list[1], some_list[2] = some_list[2], some_list[1]
display(some_list)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
~~~

4. 너무 빨라서 볼 수 없다면, 교환 연산작업이 진행되는 사이 `sleep(1)` 명령어를 추가한다. 
이를 위해 파일 상단에 `from time import sleep` 라이브러리를 추가할 필요는 있다.

5. 상기 방법을 사용해서, 다음 리스트를 정렬해본다. 시각화를 통해 어떤 작업이 진행되는지 살펴본다:

~~~ {.output}
[2,1,5,3,]
~~~

6. 상기 작업을 수행한 뒤에, 코드를 삭제하거나 주석 처리한다.

### 2.5. 루프를 사용해서 교환

리스트 원소를 비교하고 해당 원소를 교환하는 과정을 자동화할 필요가 있다.
이 작업을 착수하는데, 리스트 전체를 한번만 훑어 정렬이 되지 않는 경우,
원소를 교환한다.

1. 리스트에 있는 원소를 비교하는 것은 매우 쉽다. 인터프리터에서 다음 명령어를 실행한다.

~~~ {.python}
i = 0
some_list = [3,1,4]
some_list[i] > some_list[i+1]
~~~

2. 상기 명령어 실행결과는 `True`로 떨어지는데 이유는 리스트 0번째 원소가 첫번째 원소보다 값이 크기 때문이다.
`i`를 다른 값으로 재설정하고 다음 명령어를 시도한다:

~~~ {.python}
i = 1
some_list[i] > some_list[i+1]
~~~

상기 명령어 실행결과는 `False`로 떨어지는데, 이유는 리스트 1번째 원소가 두번째 원소값보다 더 크지 않기 때문이다.

#### 2.5.1. `for` 루프 사용

1. `for` 루프 내부에서 비교작업을 수행해서 리스트에 존재하는 모든 원소쌍을 비교한다.
**sorting.py** 파일에 다음 행을 추가한다. 작게 시작해본다. 각 원소 바로 옆에 있는 것만 비교한다.

~~~ {.python}
some_list = [6,2,5,1,7,4,9,3]
for i in range(len(some_list)-1):
    if some_list[i] > some_list[i+1]
        print(some_list[i], 'is greater than', some_list[i+1])
~~~

2. 코드를 실행해서 무슨 일이 루프를 돌면서 발생했는지 살펴본다.
리스트 길이보다 왜 하나 작게(`len(some_list)-1`) 사용했는지 설명할 수 있나?
`for` 루프에 `for i in range(len(some_list))` 로 설정하면 무슨 일이 발생하나?
직접 시도해보고 결과를 살펴보라.

3. 바로 지금, 루프는 리스트에 있는 원소만 비교하고, 특정 원소가 바로 옆 원소보다 더 큰지만 알려준다.
하지만, 정렬되지 않는 원소를 바굴 필요도 있다. `display()` 함수를 사용해서 무슨 일이 진행되고 있는지 살펴본다.

~~~ {.python}
some_list = [6,2,5,1,7,4,9,3]
for i in range(len(some_list)-1):
    if some_list[i] > some_list[i + 1]:
        some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
        display(some_list)
~~~

4. 코드를 실행하고 나서 원소가 바뀌었는지 살펴본다. 실행속도가 너무 빨라 늦출 필요가 있는 경우, `sleep()`
함수를 `display()` 함수 호출 다음에 추가한다.

5. `create_random_list()` 함수를 사용해서 훨씬 더 긴 리스트로 상기 코드를 실행할 수 있다.

~~~ {.python}
some_list = create_random_list(100)
for i in range(len(some_list)-1):
    if some_list[i] > some_list[i + 1]:
        some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
        display(some_list)
~~~

칼럼이 왼쪽에서 오른쪽으로 이동한 것이 보인다. 
칼럼보다 더 큰 값을 만나면, 멈추고 나서 더 큰 칼럼이 옮겨가게 된다.

### 2.6. 리스트 정렬

1. 분명히, 리스트는 아직 정렬되지 않았다.
전체 정렬과정은 여러번 반복될 필요가 있다. 반복작업을 수행하기 위해서, 
`while` 루프 내부에 전체 반복 `for` 루프를 위치시킨다.

~~~ {.python}
some_list = create_random_list(10)
while True:
    for i in range(len(some_list)-1):
        if some_list[i] > some_list[i + 1]:
            some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
            display(some_list)
~~~

2. 상기 프로그램은 리스트를 정렬시키지만, 프로그램이 절대로 종료되지 않는다.
질문은... 리스트가 정렬되었는지 어떻게 알 수 있을까?
문제의 핵심은 리스트에 원소가 프로그램이 도는 중에 바뀌었는지를 살펴보는 것이다.
만약 프로그램이 도는 중 리스트에 어떤 원소가 바뀌게 되면, 
리스트는 아직 정렬이 되지 않았다고 가정할 수 있다. 만약 루프를 도는 중에 어떤 원소도 바뀌지 않게 되면,
리스트는 정렬된 것으로 판단한다.

~~~ {.python}
some_list = create_random_list(10)
swapped = True
while swapped:
    swapped = False
    for i in range(len(some_list)-1):
        if some_list[i] > some_list[i + 1]:
            some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
            display(some_list)
            swapped = True
~~~

3. 마무리로, 작성한 정렬 알고리즘을 함수로 감싸 정리한다:

~~~ {.python}
def my_bubble_sort(some_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                display(some_list)
                swapped = True
    return some_list
~~~

4. 다음과 같이 함수를 호출해서 사용한다.

~~~ {.python}
my_bubble_sort(create_random_list(20))
~~~

5. 다소 늦게 돌아간다는 것이 보이는데, 특히 리스트에 원소 갯수를 증가 시키면 그렇다.
`display()` 함수 호출을 `for` 루프 외각으로 빼면, 시각화 속도를 증가시킬 수 있다:

~~~ {.python}
def my_bubble_sort(some_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                swapped = True
        display(some_list)

    return some_list

my_bubble_sort(create_random_list(100))
~~~

6. 막대 그래프를 산점도 그래프로 변경시키면, 좀더 시각적으로 확인이 쉽다.

