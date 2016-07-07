---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 퀵 정렬(quicksort)
---

> ### 학습 목표 {.objectives}
>
> * 퀵정렬 알고리즘 작동방식과 성능에 대해 이해한다.
> * 퀵정렬 알고리즘 작동방식에 대해 구체적으로 기술한다.
> * 알고리즘 성능을 비판적으로 분석하고 약점을 식별한다.


정렬 알고리즘 학습이 많은 학생들에게 정말 재미없는 주제다. 학생들로 하여금
다양한 정렬 알고리즘을 작성하게 하고 시각적으로 동작하는 것을 보여줘서
알고리즘이 어떤 작업을 수행하고 있는지 더 잘 파악하도록 이해력을 높여,
조금더 희망을 갖는다면 학습 주제가 학생들에게 좀더 재미있게 다가섰으면 한다.

## 1. 수업 계획

### 1.1. 들어가며

재귀를 상기시킨다.


### 1.2. 함께 고민하기

학생들에게 본인이 좋아하는 알고리즘을 찾아 리스트를 정렬시킨다. 어떤 학생이 작성한 것이 가장 빠른지 살펴본다.
`display()` 함수 호출을 들어내어 알고리즘 속도를 증가시킨다. 그리고 나서 매우 큰 리스트를 학생들이 정렬하도록 주문한다.

* 피봇으로 중위수를 골라 퀵정렬을 최적화시킨다.
* 피봇을 고를 때 다음 방식이 가능한 해법 중 하나다.

~~~ {.python}
        middle = (stop - start) // 2
        if some_list[start] > some_list[middle] > some_list[stop]:
            pivot = some_list[middle]
        elif some_list[start] > some_list[stop] > some_list[middle]:
            pivot = some_list[stop]
        else:
            pivot = some_list[start]
~~~

## 2. 학생 학습지

### 2.1. 들어가며

퀵정렬은 재귀를 사용하고 리스트를 정렬하는 매우 효율적인 방법이다. 리스트가 다음과 같이 주어졌다고 가정한다:

~~~ {.output}
[39, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 5]
~~~

상기 리스트를 정렬하는데 **분할 정보(divide and conquer)** 기법을 사용한다. 즉, 문제를 더 작은 문제로 쪼갠다.

1. 먼저, 리스트에서 원소를 하나 선택한다. 어느 것이든지 문제가 되지는 않는다. 리스트에 첫번째 원소가 될 수도 있다. 이런 경우 `39`.

2. 다음으로, 리스트를 따라 왼쪽에서 오른쪽으로 이동한다. 피봇보다 크거나 같은 원소를 찾는다.
이번 경우 피봇은 `39`, 첫번째 원소도 `39`로, 바로 찾았다.

3. 그리고 나서, 리스트 가장 우측으로 이동하고, 피봇보다 작은 원소를 찾는데 이번 경우에 `5`가 된다. 그리고 나서 두 원소 위치를 바꾼다:

~~~ {.output}
[5, 30, 45, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 4, 39]
~~~

4. 이 과정이 계속된다. 왼쪽에서 `30`이 피봇보다 더 작아서 그냥 무시하고 넘어간다.
`45`는 피봇보다 크다. 오른쪽에서, `4`는 피봇보다 더 작다. 그래서 두 원소위치를 바꾼다.

~~~ {.output}
[5, 30, 4, 33, 20, 61, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 2, 71, 45, 39]
~~~

5. 계속 진행되면, 다음을 얻게 된다:

~~~ {.output}
[5, 30, 4, 33, 20, 2, 36, 5, 31, 64, 22, 10, 21, 25, 80, 86, 63, 27, 85, 61, 71, 45, 39]
[5, 30, 4, 33, 20, 2, 36, 5, 31, 27, 22, 10, 21, 25, 80, 86, 63, 64, 85, 61, 71, 45, 39]
~~~

6. 이제, 리스트는 정렬이 되었고, 오른쪽에 `39` 보다 크거나 같은 원소가 있고, `39` 보다 작은 것은 왼쪽에 위치하게 된다.

7. 다음으로 재귀가 등장한다. 리스트 왼쪽과 오른쪽 양쪽 모두에 알고리즘을 적용시킨다.

8. 이 과정이 계속되고, 알고리즘을 통해 리스트의 더 작고 더 작은 부분에 적용되어, 리스트 부분이 1 혹은 0이 될때까지 진행된다. 이렇게 되면 리스트가 정렬되게 된다:

~~~ {.output}
[2, 4, 5, 5, 10, 20, 21, 22, 25, 27, 30, 31, 33, 36, 39, 45, 61, 63, 64, 71, 80, 85, 86]
~~~

### 2.2. 파이썬으로 퀵정렬 구현

#### 2.2.1. 시작 -- 기본 사례

피봇을 선정하고 리스트에 원소를 이동시키는 알고리즘을 생성한다. 그렇게 하면 피봇보다 크거가 같은 모든 원소는 오른쪽에 피봇보다 작은 원소는 좌측에 위치하게 된다.

1. 퀵정렬 알고리즘은 전체 리스트와 리스트 일부에 동작한다. 그래서 알고리즘이 리스트 시작과 끝 지점을 알아야 한다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
~~~

2. **기본 사례** 를 먼저 정의힌다. 만약 시작지점과 끝지점이 1 보다 적게 되면(즉, 1개보다 적은 원소를 포함하는 리스트를 정렬하려고 함), 함수는 멈춘다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
    if stop - start < 1:
        return some_list
~~~

#### 2.2.2. 원소 이동

1. 피봇을 선정하고, 비교하려는 리스트에서 원소도 선정한다.
`pivot`이 리스트 일부분에 있는 첫번째 원소다. 가장 왼쪽 `left`, 오른쪽 `right` 원소는 리스트 일부분에 위치한 시작지점과 끝지점이다:

~~~ {.python}
def my_quicksort(some_list, start, stop):
  if stop - start < 1:
      return some_list
  else:
      pivot = some_list[start]
      left = start
      right = stop
~~~

2. 수행해야 되는 첫번째 작업은 가장 왼쪽편에 위치한 원소로 시작해서, 만약 피봇보다 더 작은지를 검사하고 피봇보다 더 큰 것을 찾을 때까지 쭉 진행해 나간다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
    if stop - start < 1:
        return some_list
    else:
        pivot = some_list[start]
        left = start
        right = stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
~~~      

3. 피봇보다 크거가 같은 첫번째 원소를 좌측에서 우측방향으로 찾아가게 된다.

4. 피봇보다 더 큰 값을 찾아, 동일한 작업을 오른편에서도 수행할 수 있다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
  if stop - start < 1:
      return some_list
  else:
      pivot = some_list[start]
      left = start
      right = stop
      while left <= right:
          while some_list[left] < pivot:
              left += 1
          while some_list[right] > pivot:
              right -= 1
~~~

5. 그렇게 하면, 알고리즘이 오른편에서 피봇보다 작은 원소를 찾게되고 왼편에서 피봇보다 크거나 같은 원소를 찾게 된다.
이제 둘의 위치를 바꿔 다음 원소를 살펴보게 된다:

~~~ {.python}
def my_quicksort(some_list, start, stop):
    if stop - start < 1:
        return some_list
    else:
        pivot = some_list[start]
        left = start
        right = stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1
            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                left += 1
                right -= 1
~~~

6. 알고리즘이 지금까지 잘 동작하는지 `print` 문을 사용해서 검사한다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
  if stop - start < 1:
      return some_list
  else:
      pivot = some_list[start]
      print('The pivot is:',pivot)
      left = start
      right = stop
      while left <= right:
          while some_list[left] < pivot:
              left += 1
          while some_list[right] > pivot:
              right -= 1
          if left <= right:
              some_list[left], some_list[right] = some_list[right], some_list[left]
              print("Swapping", some_list[left], "with", some_list[right])
              left += 1
              right -= 1
              print('So the list becomes:')
              print(some_list)

my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]
my_quicksort(my_list, 0, len(my_list) - 1)
~~~

7. `display` 함수를 사용해서 초기부분을 시각화한다. 아마도 막대그래프가 적합한 것으로 보인다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
    if stop - start < 1:
        return some_list
    else:
        pivot = some_list[start]
        print('The pivot is:',pivot)
        left = start
        right = stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1
            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                print("Swapping", some_list[left], "with", some_list[right])
                left += 1
                right -= 1
                print('So the list becomes:')
                print(some_list)
                display(some_list)

my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]
my_quicksort(my_list, 0, len(my_list) - 1)
~~~

#### 2.2.3. 재귀 추가

1. 리스트가 두부분으로 정렬이 되었기 때문에, 양쪽 부분을 `my_quicksort()` 함수로 실행시킨다.

2. 리스트 좌측부분을 정렬하는데 `start`에서 시작해서 `right` 지점에서 종료한다.
리스트 오른쪽편을 정렬하려면, `left` 지점에서 시작해서 `stop`에서 종료한다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
    if stop - start < 1:
        return some_list
    else:
        pivot = some_list[start]
        left = start
        right = stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1
            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                print("Swapping", some_list[left], "with", some_list[right])
                left += 1
                right -= 1

        my_quicksort(some_list, start, right)
        my_quicksort(some_list, left, stop)
~~~

3. 마지막으로, `display`와 `create_random_list` 함수를 사용해서 큰 리스트에서도 잘 동작하는지 살펴본다.

~~~ {.python}
def my_quicksort(some_list, start, stop):
    if stop - start < 1:
        return some_list
    else:
        pivot = some_list[start]
        left = start
        right = stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1
            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                print("Swapping", some_list[left], "with", some_list[right])
                left += 1
                right -= 1

        display(some_list)

        my_quicksort(some_list, start, right)
        my_quicksort(some_list, left, stop)

my_list = create_random_list(200)
my_quicksort(my_list, 0, len(my_list) - 1)
~~~
