---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 삽입 정렬(insertion sort)
---

> ### 학습 목표 {.objectives}
>
> * 삽입 정렬 알고리즘 작동방식과 성능에 대해 이해한다.
> * 알고리즘 성능을 비판적으로 분석하고 약점을 식별한다.


정렬 알고리즘 학습이 많은 학생들에게 정말 재미없는 주제다. 학생들로 하여금
다양한 정렬 알고리즘을 작성하게 하고 시각적으로 동작하는 것을 보여줘서
알고리즘이 어떤 작업을 수행하고 있는지 더 잘 파악하도록 이해력을 높여,
조금더 희망을 갖는다면 학습 주제가 학생들에게 좀더 재미있게 다가섰으면 한다.

## 1. 수업 계획

### 1.1. 삽입 정렬 

삽입 정렬은 서양카드를 사용해서 쉽게 시각화해서 이해할 수 있다.

<img src="fig/rpi-algo-insertion-anim.gif" alt="삽입정렬 알고리즘 Gif 애니메이션" width="50%">


1. 카드 5장을 쭉 나눠 놓는다; 만약 충분한 카드가 있다면, 학생들에게 나눠주거나 적어도 10개까지 다른 카드를 준비한다.
1. 가장 왼쪽 카드는 무시한다.
1. 다음 번 카드가 더 크다면 그대로 놔두고, 더 작다면 바꿔치기 한다.
1. 카드가 정렬된 순서로 될때는 다음번 카드를 그대로 둔다.
1. 모든 카드가 정랼될 때까지 두번 이상 상기 과정을 반복한다.

### 1.2. 함께 고민하기

학생들이 거품 정렬과 삽입 정렬 알고리즘 속도를 비교한다.

`display()` 함수 호출을 제거해서 5000개 원소를 갖는 매우 큰 리스트를 정렬한다.

삽입 정렬 알고리즘에 대한 최적화 전략을 연구한다.


## 2. 학생 학습지

### 2.1. 들어가며

삽입 정렬은 정렬되지 않는 원소를 갖는 리스트를 정렬하는 방법으로, 리스트로 들어가서, 정렬되지 않는 원소를 제고하고 나서,
제거된 원소에 대해 정렬된 위치로 파악될 때까지 다른 원소를 뒤섞어 나가는 방식이다.

다음과 같은 작은 리스트로 시작해 보자:

~~~ {.output}
[4,3,6,2]
~~~

첫번째 값 `4`는 무시된다. 다음 값 `3`이 대상이 되고, 첫번째 값 `4`와 비교한다.
`4`가 `3` 보다 크기 때문에 위치를 바꾼다:

~~~ {.output}
[3,4,6,2]
~~~

다음으로 `6`이 대상이 된다. `4` 보다 크기 때문에, 제자리에 둔다. 마지막으로 `2`가 대상이 된다.
`6`이 더 크기 때문에, 두 숫자 위치를 바꾼다.

~~~ {.output}
[4,3,2,6]
~~~

`2`가 `4`보다 더 작다. 그래서 서로 위치를 바꾼다: `[3,2,4,6]`

마지막으로 `3`이 `2` 보다 더 크다. 그래서 서로 위치를 바꾼다:

~~~ {.output}
[2,3,4,6]
~~~

### 2.2. 출발

1. 원소가 몇개 없는 리스트를 정렬하면서 삽입 정렬 알고리즘 코딩을 시작한다.

2. 정렬할 리스트를 생성해서 시작한다.

~~~ {.python}
some_list = [4,1,3,2]
~~~

3. 정렬할 원소를 선택한다:

~~~ {.python}
i = 3
~~~

4. 위치 2를 골랐기 때문에 이에 상응되는 값은 리스트 `2`에 해당된다.
`2` 값을 리스트 아래로 이동할 필요가 있다. 이뉴는 좌측 원소가 더 작기 때문이다.
`while` 루프를 사용해서 구현을 한다:

~~~ {.python}
some_list = [4,1,3,2]

i = 3

while some_list[i-1] > some_list[i]:
    some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
~~~

5. 다음으로, `i`를 매번 루프를 돌 때마다 1씩 줄인다.

~~~ {.python}
some_list = [4,1,3,2]

i = 3

while some_list[i-1] > some_list[i]:
    some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
    i -= 1
~~~

6. 코드를 실행하고 나서 인터프리터에 `some_list`를 타이핑해서 원소가 이동했는지 검사한다.

### 2.3. 범위 밖(Out of Range)

1. 지금까지 코딩한 알고리즘이 원소를 리스트 올바른 위치로 옮긴 듯 보인다.
확실히 하기 위해, 다른 리스트를 가지고 시험을 해본다. 파일을 편집해서 리스트가 이제 다음과 같다.

~~~ {.python}
some_list = [4,2,3,1]
~~~

2. 코드를 실행하고, 무슨 일이 발생했는지 확인한다. 오류 메시지가 산출된다:

~~~ {.output}
IndexError: list index out of range
~~~

3. 왜 이런 일이 발생했을까? 인터프리터에서 `i`를 타이핑하고 값을 살펴본다.

4. `display()` 함수를 사용해서 실제로 무슨 일이 발생했는지 살펴본다.
코드를 편집해서 바뀜일 발생할 때마다 리스트를 출력하도록 한다.

~~~ {.python}
some_list = [4,2,3,1]

i = 3

while some_list[i-1] > some_list[i]:
    some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
    display(some_list)
~~~

5. 너무 코드가 빨리 실행이 되면 `sleep(1)` 명령어를 적어 넣는다.
물론, 코드 상단에 `time` 모듈을 가져와야 된다.

~~~ {.python}
from time import sleep

# 작업 코드

some_list = [4,2,3,1]

i = 3

while some_list[i-1] > some_list[i]:
    some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
    display(some_list)
    i -= 1
    sleep(1)
~~~

6. 값 `1`이 리스트 시작위치로 이동하고 나서, 쭉 이동해서 마지막으로 이동하고, 다시 처음으로 이동되는 것이 보이는가?
마치 두번 정렬되는 것처럼 보인다! 이런 일이 발생하는 것은 파이썬에서 리스트가 색인되는 방식 때문에 그렇다.
원소가 `0`번 위치로 이동하게 되면(`i`가 `0`이 될 때) `i`는 `1`만큼 감소해서 `-1`이 된다.

7. 파이썬에서 리스트 `-1`번째 원소는 마지막 원소가 된다. `i`가 줄어들면, -2번째, -3번째, -4번째 원소를 참조하게 된다.
이번 리스트에서 -4번째 원소는 0번째 원소이기도 하다. 파이썬에서 다시 사이클을 돌 수 없어서, 파이썬 프로그램이 -5번째 원소를 참조하게 될 때, 오류가 발생된다. 이 오류를 회피하기 위해서, `while` 루프가 `i > 0` 일 때만 반복을 돌도록 만든다.

~~~ {.python}
some_list = [4,2,3,1]

i = 3

while i > 0 and some_list[i-1] > some_list[i]:
    some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
    display(some_list)
    i -= 1
    sleep(1)
~~~

### 2.4. 삽입 정렬 마무리

1. 해당 원소보다 더 적은 원소를 마주칠 때까지 오른쪽에서 왼쪽으로 리스트에 어떤 원소도 이동시킬 수 있는 코드를 작성했기 때문에, 쉽게 삽입 정렬을 마무리할 수 있다. 필요한 마무리 작업은 처음에서 마지막까지 리스트의 모든 원소에 작성한 알고리즘을 적용시키는 것이다. `for` 루프가 이런 작업에 제격이다:

~~~ {.python}
some_list = [4,2,3,1]

for i in range(1,len(some_list)):
        while i > 0 and some_list[i-1] > some_list[i]:
            some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
            i -= 1
            display(some_list)
~~~

2. 상기 코드를 동작시키고, 삽입 정렬이 잘 동작하는지 살펴본다.

3. 거품 정렬에서 했던 것과 마찬가지로, 함수로 감싸서 함수 호출을 한다.

~~~ {.python}
def my_insertion_sort(some_list):
    for i in range(1,len(some_list)):
        while i > 0 and some_list[i-1] > some_list[i]:
            some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
            i-=1
            display(some_list)
    return some_list

my_insertion_sort(create_random_list(100))
~~~

4. `display()` 함수 호출을 `for` 루프 외각으로 빼면, 시각화 속도를 증가시킬 수 있다:

~~~ {.python}
def my_insertion_sort(some_list):
    for i in range(1,len(some_list)):
        while i > 0 and some_list[i-1] > some_list[i]:
            some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
            i-=1
        display(some_list)
    return some_list

my_insertion_sort(create_random_list(100))
~~~