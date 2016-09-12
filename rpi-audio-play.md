---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 인공지능 준비-소리파일 재생
---

> ### 학습 목표 {.objectives}
>
> * `wav`, `mp3` 음성 파일을 명령라인 인터페이스로 재생한다.


### 1. 가장 먼저 확인할 사항 [^rpi-cmd-audio] [^rpi-play-audio]

[^rpi-cmd-audio]: [Raspberry Pi Command Line Audio](http://www.raspberrypi-spy.co.uk/2013/06/raspberry-pi-command-line-audio/)

[^rpi-play-audio]: [6. Playing Audio](http://workshop.raspberrypiaustralia.com/audio/2014/08/31/06-playing-audio/)

`wav`, `mp3` 음성 파일을 RPi 명령라인 인터페이스로 재생할 때 가장 먼저 확인할 사항은 
`snd_bcm2835` 가 적재되어 있는지 확인하는 것이다.

~~~ {.shell}
$ lsmod | grep snd_bcm2835
~~~

만약 `snd_bcm2835` 적재되지 않는 경우, 다음 명령어를 실행해서 올린다.

~~~ {.shell}
$ sudo modprobe snd_bcm2835 
~~~

그래도 자동으로 적재되지 않는 경우, 부팅할 때 자동으로 올라가도록 다음 과정을 거쳐 설정을 한다:

~~~ {.shell}
$ cd /etc
$ sudo nano modules
~~~

**snd-bcm2835** 을 추가한다.

~~~ {.python}
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be
# loaded at boot time, one per line. Lines beginning with "#" are
# ignored. Parameters can be specified after the module name.
 
snd-bcm2835
~~~

> ### 스피커 테스트 {.callout}
>
> `speaker-test` 프로그램이 라즈비언 내에 포함되어 있어 이를 통해 소리가 나는지 사전 검사한다.
> `ctrl+c` 키를 눌러 소리가 나면, 혹은 소리가 나지 않으면 상황을 파악하고 정지시킨다.
>
> ~~~ {.shell}
> $ speaker-test -t sine -f 600 > /dev/null
> ~~~



### 2. 오디오 출력단자 확인

다음으로 오디오 출력단자를 확인한다. 기본디폴트 설정으로 아날로그 출력단자로 설정되지 않는 경우, `HDMI`가 설정된다.
하지만, 다음 명령어를 통해 강제로 설정하는 것도 가능하다:

~~~ {.shell}
$ amixer cset numid=3 n
~~~

여기서 **n** 값을 지정해서 출력단자를 지정한다. `0=auto, 1=analog, 2=hdmi`
예를 들어, 아날로그 출력단자로 지정하는 경우 다음과 같이 명령어를 설정한다.

~~~ {.shell}
$ amixer cset numid=3 1
~~~

### 3. `wav` 파일 `aplay`로 재생

`aplay` 프로그램으로 `wav` 파일을 재생하기 전에 `.wav` 파일이 필요하다.

~~~ {.shell}
$ wget http://www.freespecialeffects.co.uk/soundfx/sirens/police_s.wav
$ wget http://www.freespecialeffects.co.uk/soundfx/computers/bleep_01.wav
~~~

다운로드 받은 `.wav` 파일을 다음 명령어로 재생시킨다:

~~~ {.shell}
$ aplay police_s.wav
~~~

### 4. `mp3` 파일 `mpg321`로 재생

`mp3` 파일을 재생하는 방법은 많지만, `mpg321` 프로그램을 사용해서 명령라인 인터페이스로 실행시킨다.

~~~ {.shell}
$ sudo apt-get -y install mpg321
~~~

소프트웨어를 설치한 다음 재생시킬 `mp3` 파일을 다운로드 받는다.

~~~ {.shell}
$ wget http://www.freespecialeffects.co.uk/soundfx/household/bubbling_water_1.mp3
~~~

`mp3` 파일을 `mpg321` 프로그램으로 재생시킨다.

~~~ {.shell}
$ mpg321 bubbling_water_1.mp3
~~~

소리 볼륨을 `-g` 매개변수를 사용해서 조절하는 것도 가능하다. 다음 예제에서는 50%로 볼륨을 조정했다.

~~~ {.shell}
$ mpg321 -g 50 bubbling_water_1.mp3
~~~

### 5. `mp3` 파일 `omxplayer`로 재생

`mp3` 파일을 재생하는데, `omxplayer` 재생기도 권장할 만한다.

~~~ {.shell}
$ sudo apt-get -y install omxplayer
~~~

소프트웨어를 설치한 다음 재생시킬 `mp3` 파일을 다운로드 받는다.

`mp3` 파일을 `omxplayer` 프로그램으로 재생시킨다.

~~~ {.shell}
$ omxplayer bubbling_water_1.mp3
~~~

소리 볼륨을 `+`, `-` 키보드 자판 키를 눌러 조절하는 것도 가능하다.

~~~ {.shell}
$ mpg321 -g 50 bubbling_water_1.mp3
~~~
