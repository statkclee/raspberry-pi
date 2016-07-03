---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 파이카메라(picamera) 시작
---

라즈베리파이 카메라 모듈(picamera, 파이카메라)을 사용해서 사진을 찍고, 동영상도 찍고, 이미지에 효과도 넣을 수 있다.

> ## 학습 목표 {.objectives}
>
> * 라즈베리파이에 카메라 모듈을 연결한다.
> * 파이썬으로 카메라 모듈을 제어한다.
> * `start_preview()` `stop_preview()` 명령어를 사용해서 카메라 미리보기를 제어한다.
> * `capture()` 명령어로 정지화면 사진을 찍는다.
> * `start_recording()` `stop_recording()` 명령어로 동영상을 촬영한다.
> * `omxplayer` 플레이어로 촬영한 동영상을 재생한다.
> * 휘도(brightness)와 명암(contrast)를 조정한다.
> * 이미지 효과와 노출 모드(exposure mode)를 적용한다.

> ### 원문 출처 및 저작 라이선스 {.getready}
>
> 이 번역의 원작 "[GETTING STARTED WITH PICAMERA](https://www.raspberrypi.org/learning/getting-started-with-picamera/)"은 라즈베리파이 재단에서 개발하여 공개하고 있다.
> 이 책은 크리에이티브 커먼스(Creative Commons)의 저작자표시(BY, Attribution), 동일조건변경허락(SA, Share-Alike) 라이선스(https://creativecommons.org/licenses/by-sa/2.0/kr/](https://creativecommons.org/licenses/by-sa/2.0/kr/) 를 준용합니다.

### 1. 필요한 하드웨어와 소프트웨어 

<img src="fig/rpi-camera.png" alt="라즈베리파이 카메라" width="30%">

* 하드웨어
    * SD카드가 장착된 라즈베리 파이
    * 라즈베리파이 기본 주변장치(USB 마우스, 키보드, 전원장치 등)
    * 파이카메라
* 소프트웨어
    * 라즈비언 최신버젼 : `sudo apt-get dist-upgrade`

먼저 라즈베리파이 전원을 내리고, 라즈베리파이 카메라 포트에 파이카메라 모듈을 연결시킨다.
그리고 나서, 라즈베리파이을 켜고 소프트웨어를 활성화시킨다.

1. 카메라 포트 위치를 찾아 파이카메라를 연결시킨다:

<img src="fig/rpi-connect-camera.jpg" alt="라즈베리파이 카메라 연결" width="50%">

2. 라즈베리파이 부팅해서 시작한다.

3. **Raspberry Pi Configuration Tool** 을 선택한다. `Menu > Preferences > Raspberry Pi Configuration Tool`.

<img src="fig/rpi-raspi-config-menu.png" alt="라즈베리파이 카메라 환경설정" width="50%">

4. 카메라 소프트웨어를 활성화시킨다:

<img src="fig/rpi-raspi-config.png" alt="라즈베리파이 카메라 활성화" width="50%">

만약 활성화되지 않았다면, 활성화시키고, 라즈베리파이를 재부팅한다.

### 2. 카메라 미리보기 기능

카메라를 연결시켰고, 소프트웨어도 활성화시켰으니, 카메라 미리보기 기능을 시작할 준비가 되었다.

1. `Menu` 주메뉴에서 **파이썬3(Python 3)** 을 선택해서 연다. `Menu > Programming > Python 3 (IDLE)`.

<img src="fig/rpi-python3-app-menu.png" alt="파이썬3 실행" width="50%">

2. 새로 파일을 열고 `camera.py`로 저장한다. 절대로 `picamera.py` 파일명을 사용해서 저장하지 않는다.

3. 다음 코드를 `camera.py` 편집창에 타이핑한다.

~~~ {.python}
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.stop_preview()
~~~

4. **Ctrl + S** 키를 눌러 입력한 내용을 저장하고 나서, **F5** 키를 눌러 실행시킨다.
카메라 미리보기 기능이 10 동안 동작하고 나서 종료된다. 카메라를 옮겨서 카메라가 촬영한 것을 미리보기 기능을 살펴본다.

생방송 카메라 비리보기 기능은 다음과 같이 모니터 화면을 꽉 채워야 된다.

<img src="fig/rpi-preview.jpg" alt="라즈베리파이 카메라 미리보기" width="50%">

**카메라 미리보기 기능은 라즈베리파이가 모니터에 직접 연결될 때만 동작된다. 원격연결(SSH, VNC)된 경우 카메라 미리보기 기능이 작동되지 않는다.**

5. 미리보기로 볼 때 위와 아래가 뒤바뀐 경우 다음 코드로 회전시켜 보정한다:

~~~ {.python}
camera.rotation = 180
camera.start_preview()
sleep(10)
camera.stop_preview()
~~~

이미지를 `90`, `180`, `270`도로 회전시키거나 `0`으로 설정해서 초기 재설정시킨다.

6. 알파수준을 조정해서 카메라 미리보기 투명도를 변경시킬 수도 있다:

~~~ {.python}
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=200)
sleep(10)
camera.stop_preview()
~~~

`alpha` 값은 `0` 에서 `255` 사이 값을 갖는다.
