---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: `matplotlib` 그래프 그리기
---

> ### 학습 목표 {.objectives}
>
> * 임의 숫자 리스트 자료를 생성하는데 간단한 `list comprehension` 사용법을 이해한다.
> * `matplotlib`을 사용해서 간단한 그래프를 생성할 수 있다.


정렬 알고리즘 학습이 많은 학생들에게 정말 재미없는 주제다. 학생들로 하여금
다양한 정렬 알고리즘을 작성하게 하고 시각적으로 동작하는 것을 보여줘서
알고리즘이 어떤 작업을 수행하고 있는지 더 잘 파악하도록 이해력을 높여,
조금더 희망을 갖는다면 학습 주제가 학생들에게 좀더 재미있게 다가섰으면 한다.

### 1. `matplotlib` 설치 

`matplotlib` 팩키지를 설치하려면, 리눅스와 맥/윈도우에서 다음을 실행한다.

#### 1.1. 리눅스(데비안 배포판, 라즈비언 포함)

먼저 터미널을 열고 다음 명령어를 실행한다.

~~~ {.shell}
$ sudo apt-get install python3-matplotlib
~~~

#### 1.2. 맥 OSX/윈도우 

1. `pip`로 설치하는 경우 터미널 윈도우에서 `pip3 install matplotlib` 명령어를 실행한다.
1. 혹은, [`matplotlib` 웹사이트](http://matplotlib.org/faq/installing_faq.html#how-to-install)에서 직접 설치한다.


### 2. `list comprehension` 실습

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