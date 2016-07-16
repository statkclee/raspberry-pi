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

### Festival TTS

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

