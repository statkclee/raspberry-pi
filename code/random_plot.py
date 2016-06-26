#-*- coding: utf-8 -*-

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
