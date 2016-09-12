---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 웹캠(WebCam)
---

> ### 학습 목표 {.objectives}
>
> * 파이캠 대신 많이 사용되는 USB 웹캠을 사용해서 사진을 찍고, 비디오를 녹화한다.


> ### 원문 출처 및 저작 라이선스 {.getready}
>
> 이 번역의 원작 "[USING A STANDARD USB WEBCAM](https://www.raspberrypi.org/documentation/usage/webcams/)"은 라즈베리파이 재단에서 개발하여 공개하고 있다.
> 이 책은 크리에이티브 커먼스(Creative Commons)의 저작자표시(BY, Attribution), 동일조건변경허락(SA, Share-Alike) 라이선스(https://creativecommons.org/licenses/by-sa/2.0/kr/](https://creativecommons.org/licenses/by-sa/2.0/kr/) 를 준용합니다.

RPi로 사진을 찍거나 동영상을 녹화할 경우 [파이캠](https://www.raspberrypi.org/documentation/usage/camera/README.md)으로 알려진 카메라 모듈을 많이 사용하지만, 많이 사용되는 USB 웹캠을 사용해서도 동일한 작업을 수행할 수 있다. 그렇지만, 파이캠을 사용하는 것이 품질이나 설정에 있어 훨씬 USB 웹캠보다 낫다.

### 1. `fswebcam` 설치

`fswebcam` 팩키지를 먼저 설치한다.

~~~ {.shell}
$ sudo apt-get install fswebcam
~~~

### 2. 기본 사용법 [^rpi-webcam-ts]

[^rpi-webcam-ts]: [fswebcam - gd-jpeg: JPEG library reports unrecoverable error](https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=60076)

`fswebcam` 명령어 다음에 파일명을 입력하면, 웹캠을 사용해서 사진이 찍히고, 지정된 파일명으로 저장된다:

~~~ {.shell}
$ fswebcam image.jpg
$ # fswebcam -p YUYV -d /dev/video0 image.jpg
~~~

상기 명령어를 실행시키면 다음과 같은 정보가 화면에 출력된다.

~~~ {.output}
--- Opening /dev/video0...
Trying source module v4l2...
/dev/video0 opened.
No input was specified, using the first.
Adjusting resolution from 384x288 to 352x288.
--- Capturing frame...
Corrupt JPEG data: 2 extraneous bytes before marker 0xd4
Captured frame in 0.00 seconds.
--- Processing captured image...
Writing JPEG image to 'image.jpg'.
~~~

<img src="fig/rpi-webcam-image.jpg" alt="RPi 웹캠으로 찍은 사진" width="77%" />

기본디폴트 설정된 해상도가 사용되었고, 하단에 시간도장(Timestamp)이 찍힌 배너가 나타난다.


#### 2.1. 해상도 지정

해상도(resolution)를 $1280 \times 720$ 으로 지정해서 찍으려면, `-r` 플래그를 사용한다. 

~~~ {.shell}
$ fswebcam -r 1280x720 image2.jpg
$ # fswebcam -p YUYV -d /dev/video0 -r 1280x720 image2.jpg
~~~

상기 명령어를 실행시키면 다음과 같은 결과가 화면에 출력된다.

~~~ {.output}
--- Opening /dev/video0...
Trying source module v4l2...
/dev/video0 opened.
No input was specified, using the first.
--- Capturing frame...
Corrupt JPEG data: 1 extraneous bytes before marker 0xd5
Captured frame in 0.00 seconds.
--- Processing captured image...
Writing JPEG image to 'image2.jpg'.
~~~


<img src="fig/rpi-webcam-image2.jpg" alt="RPi 웹캠으로 해상도 조정해서 찍은 사진" width="77%" />

#### 2.2. 배너를 지정하지 않는 경우

`--no-banner` 옵션플래그를 추가한다:

~~~ {.shell}
$ fswebcam -r 1280x720 --no-banner image3.jpg
$ # fswebcam -p YUYV -d /dev/video0 -r 1280x720 --no-banner image2.jpg
~~~

상기 명령어를 실행시키면 다음과 같은 결과가 화면에 출력된다.

~~~ {.output}
--- Opening /dev/video0...
Trying source module v4l2...
/dev/video0 opened.
No input was specified, using the first.
--- Capturing frame...
Corrupt JPEG data: 2 extraneous bytes before marker 0xd6
Captured frame in 0.00 seconds.
--- Processing captured image...
Disabling banner.
Writing JPEG image to 'image3.jpg'.
~~~


<img src="fig/rpi-webcam-image3.jpg" alt="RPi 웹캠으로 배너를 제거하고 찍은 사진" width="77%" />

옵션플래그로 해상도를 지정하고, 배너를 제거해서 사진을 찍었다.

### 3. 배쉬 스크립트

웹캠으로 사진을 찍는 배쉬 스크립트를 작성한다.
`/home/pi/webcam` 디렉토리에 이미지를 저장할 예정이라 먼저, `webcam` 디렉토리를 생성한다.

~~~ {.shell}
$ mkdir webcam
~~~

스크립트를 생성하려면, 편집기를 열고, 다음과 같이 예제 코드를 작성한다.

~~~ {.bash}
#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner -p YUYV -d /dev/video0 /home/pi/webcam/$DATE.jpg
~~~

상기 배쉬 스크립트를 실행시키면, 사진을 찍고 나서 시간도장이 포함된 파일명으로 저장시킨다.
먼저 상기 스크립트를 `webcam.sh`로 저장시키고, 아스키 텍스트 파일을 실행파일로 변경시킨다.

~~~ {.shell}
$ chmod +x webcam.sh
~~~

그리고 나서, 다음 명령어로 실행시킨다.

~~~ {.shell}
$ ./webcam.sh
~~~

상기 배쉬 스크립트를 실행시키면 파일에 적힌 명령어를 실행하고, 일반적인 출력결과를 화면에 뿌려준다.

~~~ {.output}
--- Opening /dev/video0...
Trying source module v4l2...
/dev/video0 opened.
No input was specified, using the first.
--- Capturing frame...
Corrupt JPEG data: 2 extraneous bytes before marker 0xd6
Captured frame in 0.00 seconds.
--- Processing captured image...
Disabling banner.
Writing JPEG image to '/home/pi/webcam/2013-06-07_2338.jpg'.
~~~

### 4. `cron` 명령어를 사용한 저속촬영(time-lapse)

`cron` 명령어를 사용해서 정해진 시간간격을 갖고 사진찍는 것에 스케쥴을 둘 수 있다. 예를 들어,
매 10분마다 시간경과를 촬영.

먼저 `crontab`을 실행해서 편집을 시작한다:

~~~ {.shell}
$ crontab -e
~~~

`crontab -e`를 실행하면 어떤 편집기를 사용할지 사용자에게 묻거나 기본디폴트 편집기를 연다.
편집기가 열리면, 매 5분마다 사진을 찍는 스케쥴을 다음과 같이 적어 추가시킨다.
스케쥴로 돌릴 스크립트는 `webcam.sh`로 위에서 정의한 배쉬 스크립트다.

~~~ {.shell}
* * * * * /home/pi/webcam.sh 2>&1
~~~

저장하고 나오면 다음 메시지가 보이면 된다.

~~~ {.output}
crontab: installing new crontab
~~~

작성한 스크립트가 매번 사진을 찍을 때마다 동일한 파일명으로 저장되지 않도록 유의한다. 

> ### `crontab` {.callout}
> 
> `crantab`에 대한 자세한 사항은 [SCHEDULING TASKS WITH CRON](https://www.raspberrypi.org/documentation/linux/usage/cron.md) 참조한다.