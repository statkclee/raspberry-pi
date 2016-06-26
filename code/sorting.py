#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import shuffle
from time import sleep

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.draw()

### 1. 리스트 정렬
##some_list = [3,2,1]
##some_list[0], some_list[1] = some_list[1], some_list[0]
##some_list[1], some_list[2] = some_list[2], some_list[1]
##some_list[0], some_list[1] = some_list[1], some_list[0]
##print(some_list)
##
### 2. 리스트 정렬 시각화
##some_list = [3,2,1]
##display(some_list)
##sleep(0.5)
##some_list[0], some_list[1] = some_list[1], some_list[0]
##display(some_list)
##sleep(0.5)
##some_list[1], some_list[2] = some_list[2], some_list[1]
##display(some_list)
##sleep(0.5)
##some_list[0], some_list[1] = some_list[1], some_list[0]
##display(some_list)
##sleep(0.5)

# 3. 리스트 비교
##some_list = [6,2,5,1,7,4,9,3]
##for i in range(len(some_list)-1):
##    if some_list[i] > some_list[i+1]:
##        print(some_list[i], 'is greater than', some_list[i+1])

# 4. 리스트 비교, 바꿈, 시각화
##some_list = [6,2,5,1,7,4,9,3]
##for i in range(len(some_list)-1):
##    if some_list[i] > some_list[i + 1]:
##        some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
##        display(some_list)

# 5. 리스트 정렬 : 무한루프
##some_list = create_random_list(10)
##while True:
##    for i in range(len(some_list)-1):
##        if some_list[i] > some_list[i + 1]:
##            some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
##            display(some_list)

# 6. 리스트 정렬: 종료조건 추가
##some_list = create_random_list(10)
##swapped = True
##while swapped:
##    swapped = False
##    for i in range(len(some_list)-1):
##        if some_list[i] > some_list[i + 1]:
##            some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
##            display(some_list)
##            swapped = True

# 7. 거품정렬 함수 시각화
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

# my_bubble_sort(create_random_list(100))

# 8. 삽입정렬
def my_insertion_sort(some_list):
    for i in range(1,len(some_list)):
        while i > 0 and some_list[i-1] > some_list[i]:
            some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
            i-=1
        display(some_list)
    return some_list

my_insertion_sort(create_random_list(100))
