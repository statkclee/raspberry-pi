---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 감각모자로 주변 감지
---

> ### 학습 목표 {.objectives}
>
> * 감각모자(Sense HAT)를 이해한다.
> * 파이썬 프로그래밍 환경 IDEL을 사용해서 감각모자로 의사소통하는 방법을 학습한다. 
> * 감각모자 입출력을 프로그램하는 방법을 학습한다.
> * 감각모자 라이브러리를 사용해서 메시지와 이미지를 화면에 출력하고, 방향을 제어하고, 센서 데이터를 수집하고, 움직임에 반응한다.
> * 변수를 사용해서 센서 데이터를 수집하는 방법을 학습한다.
> * 특정 동작을 반복하는데 루프를 사용하는 방법도 학습한다.

[Astro Pi](https://astro-pi.org/) 프로젝트 일환으로 감지센서에 대한 교재가 많이 개발되었다.

|      감지 센서          |          입출력         |
|:-----------------------:|:-----------------------:|
|        온도             |         조이스틱        |
|        습도             |        LED 전광판       |
|        압력             |           버튼          |
|        움직임           |                         |


### 1. 온도 

감각 모자에는 다양한 센서가 포함되어 있는데, 온도센서도 그중 하나다.

<img src="fig/rpi-thermometer.jpg" alt="온도 센서" width="50%" />

상기 이미지에 몸에 온도를 측정하는 체온계가 보인다. 아파서 병원에 가면
입에 물고 체온을 측정한 경험이 모두 있을 것이다.
체온계는 35도에서 시작되어, 몸의 체온을 측정하는데만 사용된다.
감각모자에 매립된 온도센서는 -40도에서 영상 120도까지 측정이 가능해서
의료용 체온계보다 다양한 용도에 사용될 수 있다.

감각모자는 온도센서가 두개 있는데, 하나는 습도센서에 달려있고, 또다른 하나는
압력센서에 달려있다. 어느 것을 사용할지 골라 사용하거나, 둘 모두 측정하고 평균을 
내서 사용할 수 있다.

#### 1.1. 온도 측정 시작

1. 다음 명령어를 루트 권한 `sudo` 으로 **파이썬3(Python 3)** 를 터미널 윈도우에서 연다.

~~~ {.python}
sudo idle3 &
~~~

2. `File > New Window` 로 새로운 창을 열고 다음 코드를 입력한다:

~~~ {.python}
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
print(temp)
~~~

3. `File > Save` 메뉴를 선택하고 상기 파이썬 프로그램에 대한 파일명을 지정하고 저장한다. 

4. `Run > Run module` 선택해서 파이썬 프로그램을 실행시킨다.

5. `Humidity Init Failed, please run as root / use sudo` 오류 메시지(파이썬 코드 실행 마지막 줄에 붉은색 글씨)가 뜨게 되면, 상기 절차를 충실히 따르지 않는 것으로 볼 수 있다. 모든 것을 닫고, 첫번째 단계부터 다시 시작한다.

6. 결과가 다음과 같이 나오면 성공이다.

~~~ {.output}
Humidity sensor Init Succeeded
28.6293258667
~~~

7. `print(temp)` 바로 앞에 다음 명령줄을 추가한다. 소수점이 너무 길어, 소수점 아래 첫번째 자리에서 반올림한다는 것이다.

~~~ {.python}
temp = round(temp, 1)
~~~

8. 다음과 같이 보이면 성공이다. 소수점 아래 첫번째 숫자를 제외하고 반올림해서 모두 사라졌다.

~~~ {.output}
Humidity sensor Init Succeeded
28.6
~~~

9. `get_temperature` 함수 대신에 다음 함수를 사용한다.
    - `get_temperature_from_humidity`, 여기서 습도센서를 사용한다는 것으로 축약해서 `get_temperature`을 사용한다.
    - `get_temperature_from_pressure`, 여기서 압력센서를 사용한다.

예를 들어, 현재 습도센서에서 압력센서로 바꿀려면 다음과 같이 파이썬 코드를 변경한다.

~~~ {.python}
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature_from_pressure()
temp = round(temp, 1)
print(temp)
~~~

작성한 코드는 압력센서에서 온도정보를 받아 소수점아래 첫번째 자리 반올림하고 결과를 출력하고 종료된다.

#### 1.2. 온도 모니터링

1. 온도변화를 모니터링하는 것이 필요해서 `while` 루프에 위에서 작성한 코드를 넣고, 재실행한다.

~~~ {.python}
while True:
  temp = sense.get_temperature()
  temp = round(temp, 1)
  print(temp)
~~~

파이썬 코드를 실행시며면, 가장 최근에 측정한 온도가 바닥에 출력되며 스크롤이 쭉 올라간다.

2. 온도센서 위에 한동안 엄지를 올려놓는다. 온도가 상승되는 것이 보일 것이다.

3. 입김을 불거나, 공기를 불어 먼지를 털어내는 먼지청소기에서 바람을 센서에 불게 한다. 온도가 떨어지는 것이 보일 것이다.

4. `Ctrl + C` 키를 눌러 프로그램을 종료시킨다.

#### 1.3. LED 전광판에 온도 출력

온도정보를 LED 전광판에 표시하는 방법을 생각해본다.
`show_message` 함수를 사용하는 것도 좋은 선택지다.
하지만, 더 좋은 방법이 있다. 예를 들어, 다음과 같이 실행한다.

* `clear` 함수를 사용하여 측정한 온도가 속하는 범위에 미리 정의된 색상을 표현한다. 예를 들어 0 ~ 5 도는 푸른색.
* `clear` 함수를 사용하여 단일 색상을 표현하지만, 측정된 온도에 따라 붉은색 휘도(0 ~ 255)를 변경시킨다.
* `set_pixel` 함수를 사용하여 온도계와 유사하게 막대를 위로 아래로 표시한다.

다음에 나온 코드는 온도막대를 표현한 코드다. 코드에 8도 온도범위를 막대로 표시한다. (LED 가로행마다 1도를 표현)
표시할 수 있는 최대온도는 `31` (하드 코딩되어 있지만, 자유로이 편집하라), 최소 온도는 `31-8` 즉, `23`도다.
만약 측정된 온도가 범위 밖에 떨어지면 오류가 발생된다. 필요하면 측정된 온도정보도 소중하니, 오류 발생을 방지하는 코드를 추가하라.

~~~ {.python}
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

tmax = 31
tmin = tmax - 8

while True:
    temp = sense.get_temperature()
    print(temp)
    temp = int(temp) - tmin
    for x in range(0, 8):
        for y in range(0, temp):
            sense.set_pixel(x, y, 255, 0, 0)
        for y in range(temp, 8):
            sense.set_pixel(x, y, 0, 0, 0)
~~~

측정된 값에서 최소값을 빼서 0 ~ 8 사이 온도값을 산출한다.
중첩된 `for` 루프를 두개 사용한다. 외곽 루프는 `x` 축에 대한 것이고, 내부 2개 루프는 `y` 축에 대한 것이다.
여기서 `y`축에 대한 루프를 두개 사용하는 이유는 측정된 온도 아래 모든 LED를 `set_pixel` 함수로 켜고, 아래 모든 LED는 끈다. 측정된 온도에 따라 막대가 `y` 축을 따라 위로 아래로 변화하는 것처럼 보인다.

`sense.clear()` 다음에 바로 `sense.set_rotation(n)` 함수(여기서 `n`은 0, 90, 180, 270)를 사용해서 막대 방향을 바꿀 수도 있다. 

### 2. 습도(Humidity)

* 습도는 공기중에 함유된 수증기 양이다.
* 수증기는 물이 기화된 상태다.


공기중에 떠있는 수증기 양은 온도에 달려있다.

* 온도가 높으면 높을수록, 공기중에 더 많은 수증기가 떠있게 된다.
* 온도가 낮으면 낮을수록, 공기중에 더 적은 수증기가 떠있게 된다.

<img src="fig/rpi-condensation.jpg" alt="수증기" width="50%" />

냉장고에서 PT병을 빼면, 물방울이 맺치는 것을 볼 수 있다. 이유는 차가운 PT병이 주변 공기를 식혀서 
공기에 함유된 수증기가 떠다니지 못하게 만들기 때문이다.
따라서, 떠있는 수증기를 액체상태 물로 변하게 만든다. 
이것을 기체의 **응결(condensation)** 이라고 부른다. 이런 기본지식을 바탕으로,
습도를 축정하는 두가지 방식이 있다는 것을 이해할 필요가 있다.

* **절대 습도(Absolute humidity)** : 해당 공기 중에 떠다니는 수증기 전체 질량. 온도는 이런 경우 고려하지 않는다.
공기 세제곱미터 당 그램으로 보통 표시한다.
* **상대 습도(relative humidity)** : 백분율로 표시한다. 공기온도가 주어지면, 함유될 수 있는 최대 수증기량이 된다.
상대습도는 최대가능한 양과 대비하여, 실제 수증기량을 백분율로 표현한 것이 상대습도다.

공기중 온도에 따라 함유할 수 있는 수증기량이 달라지기 때문에, 수증기 양이 서로 다른 상대습도 측정값으로 표현된다. 그렇기 때문에, 낮은 공기 온도는 상대적으로 높은 습도를 주는데 이유는 낮은 공기상태에서는 많은 수증기를 함유할 수 없기 때문이다. 공기중 온도를 높이면서 동일한 수증기양을 유지시키면 상대적으로 습도측정치를 떨어뜨리게 된다. 이유는 공기중에 함유할 수 있는 최대 수증기량이 증가되기 때문이다.

감각모자는 상대습도로 습도측정 정보를 제공한다. 이런 이유로 인해서 습도센서는 온도센서가 함께 내장된다.

#### 2.1. 현재 습도 측정 시작

1. 다음 명령어를 루트 권한 `sudo` 으로 **파이썬3(Python 3)** 를 터미널 윈도우에서 연다.

~~~ {.python}
sudo idle3 &
~~~

2. `File > New Window` 로 새로운 창을 열고 다음 코드를 입력한다:

~~~ {.python}
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
print(humidity)
~~~

3. `File > Save` 메뉴를 선택하고 상기 파이썬 프로그램에 대한 파일명을 지정하고 저장한다. 

4. `Run > Run module` 선택해서 파이썬 프로그램을 실행시킨다.

5. `Humidity Init Failed, please run as root / use sudo` 오류 메시지(파이썬 코드 실행 마지막 줄에 붉은색 글씨)가 뜨게 되면, 상기 절차를 충실히 따르지 않는 것으로 볼 수 있다. 모든 것을 닫고, 첫번째 단계부터 다시 시작한다.

6. 결과가 다음과 같이 나오면 성공이다.

~~~ {.output}
Humidity sensor Init Succeeded
34.6234588623
~~~

7. `print(humidity)` 바로 앞에 다음 명령줄을 추가한다. 소수점이 너무 길어, 소수점 아래 첫번째 자리에서 반올림한다는 것이다.

~~~ {.python}
humidity = round(humidity, 1)
~~~

8. 다음과 같이 보이면 성공이다. 소수점 아래 첫번째 숫자를 제외하고 반올림해서 모두 사라졌다.

~~~ {.output}
Humidity sensor Init Succeeded
34.6
~~~

#### 2.2. 습도 모니터링

1. 습도변화를 모니터링하는 것이 필요해서 `while` 루프에 위에서 작성한 코드를 넣고, 재실행한다.

~~~ {.python}
while True:
    humidity = sense.get_humidity()
    humidity = round(humidity, 1)
    print(humidity)
~~~

파이썬 코드를 실행시며면, 가장 최근에 측정한 온도가 바닥에 출력되며 스크롤이 쭉 올라간다.

2. 센서에 천천히 숨을 불어 넣는다. 숨속에 함유된 수증기가 습도측정치를 올린다.

3. 숨을 불어 넣고 계속해서 주시하고 나면 습도측정치가 현재 방안 습도값으로 천천히 돌아가는 것이 보인다.

4. `Ctrl + C` 키를 눌러 프로그램을 종료시킨다.

#### 2.3. LED 전광판에 습도 출력

습도정보를 LED 전광판에 표시하는 방법을 생각해본다.
한방법은 64(LED 전광판 갯수)를 100으로 나누고 나서, 상대습도 백분율을 곱하면 
켜야되는 LED 전광판 갯수가 산출도니다. 예를 들어, 상대습도가 100%라면 64개 LED 모두를 켜게 된다.
이렇게 만들려면, 켜야되는 픽셀 갯수와 꺼야되는 픽셀 갯수를 리스트로 만들고 나서,
`set_pixels` 함수를 호출한다.

다음에 예제 코드가 나와 있다. 습도측정값을 100으로 고정시킨 것에 주의한다.

~~~ {.python}
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

on_pixel = [255, 0, 0]
off_pixel = [0, 0, 0]

while True:
    humidity = sense.get_humidity()
    humidity = round(humidity, 1)

    if humidity > 100:
        humidity = 100.0

    pixels = []
    on_count = int((64 / 100.0) * humidity)
    off_count = 64 - on_count

    pixels.extend([on_pixel] * on_count)
    pixels.extend([off_pixel] * off_count)

    sense.set_pixels(pixels)
~~~

**습도센서에서 100보다 큰 값을 갖는 것도 가능하다는 것에 주의한다.**

