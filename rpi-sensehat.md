---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 감각모자(Sense HAT) 시작
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 감각모자(Sense HAT)를 이해한다.
> * 파이썬 프로그래밍 환경 IDEL을 사용해서 감각모자로 의사소통하는 방법을 학습한다. 
> * 감각모자 입출력을 프로그램하는 방법을 학습한다.
> * 감각모자 라이브러리를 사용해서 메시지와 이미지를 화면에 출력하고, 방향을 제어하고, 센서 데이터를 수집하고, 움직임에 반응한다.
> * 변수를 사용해서 센서 데이터를 수집하는 방법을 학습한다.
> * 특정 동작을 반복하는데 루프를 사용하는 방법도 학습한다.


> ### 원문 출처 및 저작 라이선스 {.getready}
>
> 이 번역의 원작 "[GETTING STARTED WITH THE SENSE HAT](https://www.raspberrypi.org/learning/getting-started-with-the-sense-hat/)"은 라즈베리파이 재단에서 개발하여 공개하고 있다.
> 이 책은 크리에이티브 커먼스(Creative Commons)의 저작자표시(BY, Attribution), 동일조건변경허락(SA, Share-Alike) 라이선스(https://creativecommons.org/licenses/by-sa/2.0/kr/](https://creativecommons.org/licenses/by-sa/2.0/kr/) 를 준용합니다.


### 1. 감각모자(Sense HAT)

감각모자(Sense HAT)은 라즈베리파이 컴퓨터를 통해 주변을 느낄 수 있게 하는 중요한 프로젝트의 하나다. LED 행렬을 제어하고, 주변에서 센서 데이터를 수집하고 이를 조합하는 방법을 학습한다.

#### 1.1. 감각모자 설치

감각모자 주요 기능에 대해 살펴본다. 주요기능에 대해서는 빨간 사각형으로 강조처리를 했다. 

<img src="fig/rpi-sense-hat-features.jpg" alt="감각모자 주요기능" width="60%" />

1. LED 행렬: 64개 [LED(light emitting diodes)](http://en.wikipedia.org/wiki/Light-emitting_diode)가 $8 \times 8$ 격자모양으로 배열되어 있다. 감각모자에 LED가 화면표시 기능을 수행한다. 모양, 아이콘, 메시지를 전송하는 기능이 가능하다.
1. [IMU(inertial measurement unit)](http://en.wikipedia.org/wiki/Inertial_measurement_unit)는 관성 측정 장치로 감각상자에 적힌 `ACCEL/GYRO/MAG` 문자 위에 위치한다. 서로 다른 센서 3개가 하나에 모여있다.
    - (닌텐도 위 리모콘처럼) 가속도를 측정하는 가속도 센서 
    - 방향으로 측정하는 자이로 센서 (어느 방향을 향하는지 알게 된다.)
    - (나침반 처럼) 지구 자기장을 측정하는 자기계센서. 기본적으로 이동센서로, 손에 든 라즈베리파이가 얼마나 이동했는지 측정한다.
1. 습도 센서: 공기에 함유된 습도를 측정하게 한다.  감각상자에 적힌 `HUMIDITY` 문자 아래 작은 반도체칩이 있다. 이를 통해 주변 온도를 측정한다.
1. 압력 센서: 공기압을 측정하는 센서다. 감각상자에 적힌 `PRESSURE` 문자 옆에 위치하는 작은 반도체칩이다.
1. 마지막은 조이스틱이다. 감각센서에는 버튼 5개를 갖는 조이스틱이 있다. 상기 그림에서 맨 아래쪽에 위치하고 있고, 상하좌우 그리고 중간클릭 기능을 지원한다.

#### 1.2. 감각모자 조립

<img src="fig/rpi-sense-hat-assembly.png" alt="감각모자 조립" width="50%" />

1. 감각모자를 아직 설치하지 않았다면, 지금이 가장 적합한 시점이다. 라즈베리파이 전원을 내리고, 전원케이블을 비롯한 모든 케이블을 분리한다.
1. 감각모자 정품을 구입하게 되면, 정전기 방지 은색 봉지에 담겨 다음 부품과 함께 전달된다:
    - $1 \times GPIO$ 핀 확장헤더
    - $4 \times 6각형$ 분리기 (암놈-암놈)
    - $8 \times M2.5$ 스크류
1. 위 그림처럼 감각모자와 라즈베리파이를 결합한다.
1. 감각모자 GPIO 확장헤더 블록을 라즈베리파이 GPIO 핀에 끼워넣는다.
1. 6각 분리기를 라즈베리파이와 스크류드라이버로 체결한다.
1. 단단히 스크류드라이버로 체결할 필요는 없고 감각모자와 라즈베리파이가 헐거워지지 않도록만 한다.

#### 1.3. 소프트웨어 설치

터미널 윈도우를 열고 최신상태로 갱신한다.

~~~ {.shell}
sudo apt-get update
sudo apt-get upgrade
~~~

감각모자 소프트웨어 팩키지를 설치한다.

~~~ {.shell}
sudo apt-get install sense-hat
~~~

마지막으로 라즈베리파이를 재부팅한다.

~~~ {.shell}
sudo reboot
~~~


### 2. 첫번째 프로그램 텍스트 표시

라즈베리파이 주변장치(키보드, 마우스, 모니터, 전원)를 모두 연결하고 다음 명령어로 로그인한다.

~~~ {.shell}
login: pi
password: raspberry
~~~

비밀번호를 타이핑할 때 어떤 텍스트도 보이지 않는다: 보안 기능.

`startx`를 타이핑해서 그래픽 사용자 인터페이스를 실행시킨다. `Menu > Programming > Python 3` 파이썬3를 연다. 이를 통해 파이썬 쉘 윈도우가 나타나면 `File > New Window` 선택하고 다음 코드를 타이핑한다.

~~~ {.python}
# -*- coding: utf-8 -*-
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello my name is Tim Peake")
sense.show_message("안녕하세요 !!! 정훈입니다.")
~~~

`File > Save` 메뉴를 선택하고 상기 파이썬 프로그램에 대한 파일명을 지정하고 저장한다. `Run > Run module` 선택해서 파이썬 프로그램을 실행시킨다. LED 전광판에 흰색 텍스트로 메시지가 보여야 된다.

인용부호 내부에 메시지를 변경하고 파이썬 프로그램을 실행시킨다.

### 3. 감각 센싱 프로그램

#### 3.1. 온도 

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

##### 3.1.1. 온도 측정 시작

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

##### 3.1.2. 온도 모니터링

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

##### 3.1.3. LED 전광판에 온도 출력

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
