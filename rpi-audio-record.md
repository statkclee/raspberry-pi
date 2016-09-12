---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 청각 정보 입력 -- 녹음(마이크)
---

> ### 학습 목표 {.objectives}
>
> * USB 마이크로폰을 사용해서 목소리를 저장한다.

### 목소리 저장 [^rpi-voice-record]

[^rpi-voice-record]: [How to record voice with USB microphone then play it on Raspberry Pi 2](http://www.instructables.com/id/How-to-Record-Voice-With-USB-Microphone-Then-Play-/)

USB 웹캠 혹은 USB 마이크로폰을 장착하고 터미널 윈도우를 연다.

~~~ {.shell}
$ arecord /home/pi/voice-record-file.wav -D sysdefault:CARD=1
~~~

상기 명령어를 입력하고 마이크로폰에 녹음을 시작한다. 녹음이 끝나면, 최소 6초 정도 시간을 두고 터미널 윈도우를 닫는다. 그러면 녹음된 것이 `voice-record-file.wav` 파일에 저장된다.

### 목소리 재생

`voice-record-file.wav` 저장된 파일을 재생시킬 경우 `omxplayer`, 혹은 `aplayer`를 사용해서 목소리를 재생시킨다.

~~~ {.shell}
$ omxplayer -p -o hdmi /home/pi/voice-record-file.wav
~~~

만약, `hdmi` 단자가 아니고 아날로그 잭에 연결시킨 경우는 `-o local` 옵션을 주면 된다.

~~~ {.shell}
$ omxplayer -p -o local /home/pi/voice-record-file.wav
~~~

`omxplayer` 가 아니고 `aplay`를 사용해서 오디오를 재생시켜도 된다.

~~~ {.shell}
$ amixer cset numid=3 1
$ aplay /home/pi/voice-record-file.wav
~~~

