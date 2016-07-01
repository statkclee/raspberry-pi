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




