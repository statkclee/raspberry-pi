#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt

y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]

## 1. 산점도
##plt.scatter(x,y)
##plt.show()

## 2. 선 그림
##plt.plot(x,y)
##plt.show()

## 3. 산점도 + 선 그림
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
