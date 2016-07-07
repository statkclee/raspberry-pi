---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 선택 정렬(selection sort)
---

> ### 학습 목표 {.objectives}
>
> * 선택 정렬 알고리즘 작동방식과 성능에 대해 이해한다.
> * 알고리즘 성능을 비판적으로 분석하고 약점을 식별한다.


정렬 알고리즘 학습이 많은 학생들에게 정말 재미없는 주제다. 학생들로 하여금
다양한 정렬 알고리즘을 작성하게 하고 시각적으로 동작하는 것을 보여줘서
알고리즘이 어떤 작업을 수행하고 있는지 더 잘 파악하도록 이해력을 높여,
조금더 희망을 갖는다면 학습 주제가 학생들에게 좀더 재미있게 다가섰으면 한다.

## 1. 수업 계획

### 1.1. 삽입 정렬 

삽입 정렬은 서양카드를 사용해서 쉽게 시각화해서 이해할 수 있다.

<img src="fig/rpi-algo-selection_anim.gif" alt="선택정렬 알고리즘 Gif 애니메이션" width="50%">


1. 첫번째 카드를 꺼내보고 가장 낮은 값으로 가정한다.
1. 모든 카드를 쭉 반복해서 살펴보고, 실제로 가장 낮은 값을 갖는 카드를 저장한다.
1. 가장 낮은 카드 값을 첫번째 카드와 바꾼다.
1. 두번째 카드를 꺼내보고, 가장 낮은 값으로 가정한다.
1. 나머지 모든 카드를 쭉 반복해서 살펴보고, 실제로 가장 낮은 값을 갖는 카드를 저장한다.
1. 남은 카드 중 가장 낮은 값을 갖는 카드를 두번째 카드와 바꾼다.
1. 카드가 정렬될 때까지 이 과정을 반복한다.


### 1.2. 함께 고민하기

학생들이 거품 정렬, 삽입 정렬, 선택 정렬 알고리즘 속도를 비교한다.

`display()` 함수 호출을 제거해서 5000개 원소를 갖는 매우 큰 리스트를 정렬한다.

선택 정렬 알고리즘에 대한 최적화 전략을 연구한다.


## 2. 학생 학습지

### 2.1. 들어가며

선택 정렬 알고리즘은 아마도 가장 이해하기 쉬운 알고리즘 중 하나다. 왜냐하면,
사람들이 리스트에 포함된 원소를 정렬하는 방식과 매우 유사하다.

선택 알고리즘은 정렬되지 않은 리스트를 훑고, 훑는 과정에서 찾은 가장 작은 값을 추적한다.
전체 리스트를 반복해서 훑은 후에 최소값을 리스트 시작부로 이동시킨다.
리스트가 정렬될 때까지 이 과정을 반복한다.

다음과 같은 작은 리스트를 가정하자:

~~~ {.python}
[4,3,6,2]
~~~

첫번째 값 `4`를 가장 작은 값으로 가정한다.
리스트에 다음 원소는 `3`으로 `4`보다 작기 때문에 가장 작은 값이 바뀐다.
다음으로 `6`이 나온다. `3`보다 크기 때문에 `3`이 가장 작은 값으로 남겨진다.
마지막으로 값 `2`가 나온다. `3`보다 작기 때문에, `2`가 최소값이 된다.
알고리즘이 리스트 마지막에 도달했기 때문에, `2`를 `4`와 바꾼다.

~~~ {.python}
[2,3,6,4]
~~~

다음으로, 알고리즘은 `3`을 가장 작은 값으로 상정한다.
`3`을 `6` 그리고 나서 `4`와 비교하지만, 더 작기 때문에 그대로 둔다.

~~~ {.python}
[2,3,6,4]
~~~

마지막으로, `6`을 가장 작은 값으로 둔다. `4`와 비교하는데 `4`가 더 작기 때문에, `4`가
최소값이 된다. 알고리즘이 리스트 마지막에 도달했기 때문에, `6`과 `4`를 바꾼다:

~~~ {.python}
[2,3,4,6]
~~~

이제 리스트가 정렬되었다.

### 3. 시작

1. 이전 학습에서 사용한 **sorting.py** 파일을 적재한다.
2. 이전 학습에서 사용한 모든 함수를 주석처리 한다.

~~~ {.python}
#my_bubble_sort(create_random_list(20))
#my_insertion_sort(create_random_list(20))
~~~

### 4. 원소 하나 정렬

1. 이전 학습에서 했듯이, 작은 리스트로 시작한다:

~~~ {.python}
some_list = [4,3,6,2]
~~~

2. 수작업으로 시작 위치를 `0`에 두고 선택 정렬 알고리즘을 시작한다.

~~~ {.python}
some_list = [4,3,6,2]

i = 0
~~~

3. 다음으로, 처음 시작값을 `smallest_value`로 만든다:

~~~ {.python}
some_list = [4,3,6,2]

i = 0
smallest_value = i
~~~

4. 이제, `for` 루프를 사용해서 전체 리스트를 반복돌려(단, 0번째 원소는 제외), 가장 작은 원소를 찾는다:

~~~ {.python}
some_list = [4,3,6,2]

i = 0
smallest_value = i

for j in range(i+1,len(some_list)):
    if some_list[j] < some_list[smallest_value]:
        smallest_value = j
~~~ 

5. 스크립트를 돌려보고 가장 작은 값을 올바르게 추적하고 있는지, 인터프리터에서 `smallest_value`를 타이핑해서 확인한다.
리스트가 위와 같이 주어진 상태에서, 리스트에 3번째 원소를 지칭하는 위치값 `3`이 반환되어야 한다.
`some_list[smallest_value]` 명령어로 실제값을 볼 수 있다.

6. 가장 작은 값을 알게 되었기 때문에, 이제 이전 정렬에서 사용한 것과 동일한 작동방법을 사용한다.

~~~ {.python}
some_list = [4,3,6,2]

i = 0
smallest_value = i

for j in range(i+1,len(some_list)):
    if some_list[j] < some_list[smallest_value]:
        smallest_value = j

some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
~~~

7. 스크립트에 `display()`와 `sleep()` 호출을 넣어, 원소 바뀜을 시각적으로 확인한다.

~~~ {.python}
some_list = [4,3,6,2]

display(some_list)

i = 0
smallest_value = i

for j in range(i+1,len(some_list)):
    if some_list[j] < some_list[smallest_value]:
        smallest_value = j

some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
sleep(1)    
display(some_list)  
~~~

### 5. 전체 리스트 실행

위치 0 에서 출발해서 리스트 길이까지 전체 리스트를 반복돌린다.
`for` 루프에 앞서 작성한 모든 코드를 넣고, `i` 를 `0`으로 지정한 것을 삭제한다:

~~~ {.python}
some_list = [4,3,6,2]

for i in range(len(some_list)):
    smallest_value = i

    for j in range(i+1,len(some_list)):
        if some_list[j] < some_list[smallest_value]:
            smallest_value = j

    some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
    sleep(1)    
    display(some_list)
~~~

### 6. 정리

1. 앞에서와 마찬가지로, 함수 내부에 작성한 코드를 넣고, 임의 원소가 포함된 리스트를 함수 인자에 넣어 정렬한다.
`sleep()` 함수도 제거하는 것이 아마도 좋을 것이다:

~~~ {.python}
def my_selection_sort(some_list):
    for i in range(len(some_list)):
        smallest_value = i

        for j in range(i+1,len(some_list)):
            if some_list[j] < some_list[smallest_value]:
                smallest_value = j

        some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
        display(some_list)  

    return some_list

my_selection_sort(create_random_list(20))
~~~

2. 선택정렬은 매우 빠르기 때문에, 리스트 크기를 100으로 조정한다:

~~~ {.python}
my_selection_sort(create_random_list(100))
~~~

3. 산점도로 선택정렬을 시각화하는 것도 매우 좋다.

~~~ {.python}
def display(some_list):
    plt.clf()
    plt.scatter(range(len(some_list)),some_list)
    plt.draw()
~~~