---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 인공지능 준비-TTS(Text-to-Speech)
---

> ### 학습 목표 {.objectives}
>
> * 텍스트를 음성으로 변환(Text-to-Speech, TTS)을 이해한다.
> * `HDMI` 대신 USB를 지원하는 스피커로 와이어링한다.
> * 라즈베리파이 리눅스 팩키지를 설정한다.

### 텍스트를 음성으로 변환하는 기능을 사용하는 이유 [^rpi-tts]

[^rpi-tts]: [RPi Text to Speech (Speech Synthesis)](http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis))


문자로 화면 대신에 음성함수(speech function)을 사용하게 되면, LCD 혹은 모니터가 필요하지 않게 된다.
이어폰, MP3 플레이어 스피커, PC 스피커를 사용하여 출력으로 내보내면 된다.

음성 출력이 필요한 경우는 다음과 같다.

* 상태 메시지 전달: 예를 들어, 인터넷 연결되거나 끊어진 경우
* 사용자 인터페이스: 예를 들어, RPi 인터넷 라디오로 지정한 채널 혹은 선택한 모드 음성으로 알려줌.
* 주기능: 예를 들어, 현재 시간이나 날씨 예보정보를 전달해 준다.

### TTS 지원 팩키지 설치

음성을 출력시키려면 RPi에 오디오(Audio) 팩키지를 몇개 설치해야 된다. 
먼저 라즈비언 배포판을 갱신한다.
경우에 따라서 처음하는 경우 시간이 다소 소요될 수 있다.

~~~ {.shell}
sudo apt-get update
sudo apt-get upgrade
~~~

RPi에 소리관련 팩키지가 설치되지 않았다면, `alsa` 소리 유틸리티를 설치한다.

~~~ {.shell}
sudo apt-get install alsa-utils
~~~

`etc/modules` 파일을 편집해서... `snd_bcm2835` 행을 추가한다.

~~~ {.shell}
sudo nano /etc/modules
~~~

`etc/modules` 파일에 이미 `snd_bcm2835` 행이 추가된 경우 그냥 넘어간다.

`mplayer` 오디오/영화 재생기를 설치한다.

~~~ {.shell}
sudo apt-get install mplayer
~~~

`mplayer` 오류 메시지를 해결하려면, `/etc/mplayer/mplayer.conf` 파일을 열어, `nolirc=yes` 행을 추가한다.

~~~ {.shell}
sudo nano /etc/mplayer/mplayer.conf
~~~

#### 1. Festival TTS

`festival`은 로봇같은 음성을 낸다. RPi 로봇 프로젝트에 활용하면 좋을 듯 하다.

~~~ {.shell}
sudo apt-get install festival
~~~

설치를 한 다음, 다음을 실행해서 테스트한다.

~~~ {.shell}
echo “Just what do you think you're doing, Dave?” | festival --tts
~~~

RPi의 현재 IP주소를 음성으로 출력시킬 수도 있다.

~~~ {.shell}
hostname -I | festival --tts
~~~

#### 2. `espeak` TTS

`espeak`는 `festival` 보다 최신 음성 합성 팩키지다. 소리가 좀더 깨끗하지만, 다소 울리는 느낌을 준다. 다음 명령어로 `espeak`를 설치한다.

~~~ {.shell}
sudo apt-get install -y espeak
~~~

`espeak`를 다음 명령어로 테스트한다: 영문 여성 목소리, 대문자 강조(`-k`), 천천히 말하기(`-s`)를 `-` 선택옵션으로 사용한다.


~~~ {.shell}
espeak -ven+f3 -k5 -s150 "I've just picked up a fault in the AE35 unit"
~~~

#### 3. 구글 TTS

구글 TTS엔진은 `festival`, `espeak`와는 다소 차이가 있다. 음성 파일을 만들어 내기 위해서 텍스트를 구글 클라우드 서버로 보낸다. 결과가 RPi로 되돌아오고, `mplayer`로 음성을 재생한다.
이것이 의미하는 것은 인터넷에 연결되어야 하는 제약이 있지만, 음성 품질은 아주 좋다.

구글 TTS 엔진에 접속하는 ax206geek 배쉬 스크립트를 사용해 본다. 먼저 `speech.sh` 파일을 생성한다.

~~~ {.shell}
nano speech.sh
~~~

다음 행을 `speech.sh` 파일에 추가하고 저장한다. 

~~~ {.shell}
#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en&q=$*"; }
say $*
~~~

다른 방법으로 인터넷에 저장된 파일, [speech.sh](http://elinux.org/images/8/87/Speech.sh)을 저장한다.

저장하거나, 편집을 완료한 배쉬 스크립트에 실행권한을 부여한다:

~~~ {.shell}
chmod u+x speech.sh
~~~

다음 명령어로 테스트를 해본다.

~~~ {.shell}
./speech.sh Look Dave, I can see you're really upset about this.
~~~

텍스트를 음성으로 변환하는데 구글을 사용할 경우 100 바이트로 제한이 있다.

#### 4. Pico TTS

구글 안드로이드 TTS 엔진은 다음과 같이 사용한다.

~~~ {.shell}
sudo apt-get install libttspico-utils
pico2wave -w lookdave.wav "Look Dave, I can see you're really upset about this." && aplay lookdave.wav
~~~

### 소리 출력장치 설정

RPi 소리 출력장치를 기본디폴트설정된 **HDMI** 대신 **헤드폰 오디오 잭** 으로 변경할 경우 다음 명령어를 타이핑한다.

* `amixer cset numid=3 1` : `1`은 헤드폰 오디오 잭
* `amixer cset numid=3 2` : `2`는 HDMI
* `amixer cset numid=3 0` : `0`은 기본디폴트 설정으로 자동

~~~ {.shell}
amixer cset numid=3 1
~~~

혹은, `raspi-config` 명령어를 입력하여 환경설정으로 들어가서, `Advanced Options` `Audio` 로 들어가서 헤드폰 오디오 잭 혹은 HDMI로 설정한다.
