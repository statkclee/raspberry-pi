# xwMOOC 라즈베리파이





> ### 학습 목표 {.objectives}
>
> *  콘솔, GUI, 미디어센터 화면을 캡쳐한다.
> *  동영상, 소리, 웹브라우져 설정한다.  

<img src="fig/raspberry-pi-fullstack-toolchain.png" width="70%" />

## 1. 화면 캡쳐

### 1.1. 명령라인 인터페이스 화면 캡쳐

라즈베리 파이 명령라인 인터페이스(CLI)를 쓰게 되면 터미널 콘솔에 찍히는 색깔이 검은색 바탕에 흰색이 아니고, 사용자명/호스트 컴퓨터명/현재 디렉토리/파일과 디렉토리에 시각정보를 입혀서 보기 좋게 표현한다. 이런 화면을 잡아낼 때 사용하는 것이 **fbgrab** 이다. 

**fbgrab 설치 및 실행 명령어**
`sudo apt-get install fbgrab` 명령어를 넣어 설치하고, `sudo fbgrab screenshot.png` 와 같이 타이핑하면 콘솔화면이 저장된다. `ssh`를 통해 원격으로 접속해서 해당 명령어를 입력한 경우 원격 접속한 터미널 화면이 캡쳐되는 것이 아니라 라즈베리 파이에서 돌고 있는 해당 화면이 직접 캡쳐된다.

<img src="fig/raspberry-pi-fbgrab.png" width="50%" />

참조: [[라즈베리파이 기초] (6) 콘솔 화면 캡쳐](http://echo.tistory.com/45)

### 1.2. 화면 캡쳐한 것 가져오기

라즈베리 파이 하드웨어에 미디어센터 OSMC를 올린 사례를 살펴보자.
OSMC는 오픈일렉(OpenElec)과 달리 sftp, scp 등을 지원한다. 이러한 기능을 통해서 OSMC 에서 캡쳐한 파일을 가져다가 편집등 작업을 할 수 있다. 

1. 라즈베리 파이 OSMC 미디어 센터 화면 캡쳐하는 방법
    - 단축키 `Ctrl + S`를 눌러 설정한다. (주의: 처음 `Ctrl+S`를 누르면 캡쳐한 파일을 저장할 디렉토리 지정하라고 안내가 나옴)
    - [raspi2png](https://github.com/AndrewFromMelbourne/raspi2png) 프로그램으로 화면 캡쳐함.
1. 라즈베리 파이 OSMC 캡쳐된 파일 로컬 컴퓨터로 복사해서 가져오는 방법
    - [filezilla](https://filezilla-project.org/), [Winscp](http://winscp.net/eng/docs/lang:ko) 등등 [파일전송프로토콜(FTP)](https://ko.wikipedia.org/wiki/파일_전송_프로토콜) 프로그램을 사용해서 가져온다.
    - 명령라인 인터페이스 `sftp`를 통해 원격 컴퓨터에 접속해서 `get` 명령어로 해당 파일을 가져온다.
    - `scp` 명령어를 통해서 원격 컴퓨터(OSMC 라즈베리 파이)에서 복사해서 가져온다.
    -. 윈도우 환경에서 **bash** 명령어를 사용하기 위해서는 [Git Bash](https://msysgit.github.io/)를 설치해서 가져온다.
        * git 대몬을 다음 명령어로 띄운다. `git daemon --base-path=. --export-all`
        * 새로운 창을 열고 `scp -r osmc@192.168.103.130:~/snapshot.png winsnapshot.png` 명령어처럼 192.168.103.130 호스트에 `osmc` 사용자로 로그인해서 `~/` 디렉토리에 `snapshot.png` 파일을 복사해서 로컬 컴퓨터에 `winsnapshot.png` 이름으로 가져온다. 

<img src="fig/raspberry-pi-screenshot-scp.png" width="70%" />

`raspi2png` 프로그램의 실행파일은 `git clone` 명령어로 복제한 디렉토리 *raspi2png* **아래 raspi2png** 이다.  프로그램이 설치된 디렉토리로 들어가서 `./raspi2png` 명령어를 실행하면 snapshot.png 파일이 자동 생성된다.


~~~{.r}
osmc@osmc:~/raspi2png$ sudo passwd root
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
root@osmc:/home/osmc# git clone https://github.com/AndrewFromMelbourne/raspi2png.git
root@osmc:/home/osmc# cd raspi2png/
root@osmc:/home/osmc/raspi2png# ls
LICENSE  Makefile  README.md  raspi2png  raspi2png.c
root@osmc:/home/osmc/raspi2png# ./raspi2png
root@osmc:/home/osmc/raspi2png# ls
LICENSE  Makefile  README.md  raspi2png  raspi2png.c  snapshot.png
~~~

<img src="fig/raspberry-pi-snapshot.png" width="50%" />

참조: [[라즈베리파이 기초] (7) 라즈베리파이 스크린샷 끝!!](http://echo.tistory.com/48)

## 3. 인터넷

에피퍼니(epiphany) 웹브라우져가 현재 라즈비언에는 기본으로 설치되어 있다. 만약, 다른 웹브라우져 설치를 원한다면, [How to Install Alternative Web Browsers on the Raspberry Pi](http://computers.tutsplus.com/articles/how-to-install-alternative-web-browsers-on-the-raspberry-pi--mac-60717) 웹사이트를 참조한다. GUI 뿐만 아니라 Lynx같은 CLI 기반 다양한 웹브라우져가 있다.

* Midori 
* NetSurf
* Dillo
* Lynx
* Luakit
* 크롬(Chromium) : `sudo apt-get install chromium`
* 얼음쪽제미(Iceweasel), 불여우(Firefox): `sudo apt-get install iceweasel`
    - 불여우를 여러 이유로 사용할 수 없어 포크해서 동일한 웹브라우져로 이름은 얼음쪽제비로 작명하고 라즈베리 파이에서 사용하게 함.


~~~{.r}
pi@raspberrypi ~ $ sudo apt-get update
pi@raspberrypi ~ $ sudo apt-get dist-upgrade
pi@raspberrypi ~ $ sudo apt-get install epiphany-browser
~~~

## 4. 동영상 

### 4.1. 라즈베리 파이 소리 설정

[Audio Configuration](https://www.raspberrypi.org/documentation/configuration/audio-config.md)을 참조한다.

라즈비언은 *고급 리눅스 음향 아키텍쳐 (Advanced Linux Sound Architecture, ALSA)*를 사용한다. `aplay` 명령어로 테스트할 수 있다.


~~~{.r}
$ aplay /usr/share/scratch/Media/Sounds/Human/PartyNoise.wav
~~~

소리는 디폴트 기본설정으로 HDMI 를 사용한다. 만약 라즈베리 파이에 설치된 아날로그 잭을 통해서 소리를 내보내려면 `sudo raspi-config` 에서 `Advanced Options` &rarr; `Audio` &rarr; `Force 3.5mm(headphone) jack` 을 선택한다.


~~~{.r}
$ alsamixer
~~~

`alsamixer` 명령어를 통해서 음향을 화살표 위아래로 조정한다.


라즈베리 파이 USB 오디오 장치를 이용해서도 소리를 들을 수 있다.


~~~{.r}
$  sudo nano /etc/modprobe.d/alsa-base.conf
~~~

|                                |         |                               |
|:------------------------------:|:-------:|-------------------------------|
| options snd-usb-audio index=-2 | &rarra; | options snd-usb-audio index=0 |

`alsa-base.conf` 출력 장치를 위와 같이 변경하고 저장하고 나서 재시작하면 USB 오디오 장치가 디폴트 출력장치로 변경된다.

> #### 라즈베리 파이 음악 프로젝트 {.callout}
>
> - [Satellite CCRMA](https://ccrma.stanford.edu/~eberdahl/Satellite/)
>     * [Satellite CCRMA: A Musical Interaction and Sound Synthesis Platform (2011)](https://ccrma.stanford.edu/~eberdahl/Papers/NIME2011SatelliteCCRMA.pdf)
>     * [Embedded Networking and Hardware-Accelerated Graphics with Satellite CCRMA(2013)](https://ccrma.stanford.edu/~eberdahl/Papers/NIME2013SatelliteCCRMA.pdf)
>     * [How to Make Embedded Acoustic Instruments(2014)](https://ccrma.stanford.edu/~eberdahl/Papers/NIME2014EmbeddedAcousticInstruments.pdf)
> - [Volumio](https://volumio.org/)는 [RaspyFi](http://www.raspyfi.com/)에서 진화한 오디오 애호가를 위한 음악재생기다.
> - [PI Synthesisers](https://www.raspberrypi.org/blog/pi-synthesisers/)


### 4.2. 라즈베리 파이에서 유튜브 동영상 감사

1. 에피퍼니 웹브라우져를 연다.
2. [YouTube HTML5 동영상 플레이어](https://www.youtube.com/html5) 웹사이트에 접속한다.
3. 유튜브 동영상을 `HTML5 동영상 플레이어`로 설정한다.

[Watch YouTube in Browser with Raspbian](http://raspberrypi.stackexchange.com/questions/13955/watch-youtube-in-browser-with-raspbian)참조

## 5. 미디어센터 (셋톱박스)

미디어 콘텐츠 소비에 최적화 된 미디어센터는 기존 [RaspBMC](http://www.raspbmc.com/index.html)를 거쳐 현재는 [OSMC ](https://osmc.tv/)로 진화되었다. 라즈베리파이 NOOBS에 포함된 (네트워크 설치) 미디어센터로 [Kodi, 이전 XBMC로 불림](http://kodi.tv/) 다양한 미디어 콘텐츠를 라즈베리 파이에서 경험할 수 있다. OSMC를 설치하는 방법은 크게 인터넷에 연결된 NOOBS에서 설치하는 방법과  [OSMC](https://osmc.tv/) 웹사이트에서 포맷된 USB(마이크로SD)에 설치하는 방법으로 크게 나눌 수 있다.  

자세한 사항은 [라즈베리 파이 활용](08-raspberry-pi-os.html)을 참조한다.


## 6. 펌웨어 갱신하기

일부 라즈베리 파이 펌웨어(firmware)가 SD카드에 저장되어 있고 부팅할 때 관여를 한다. 
인터넷이 연결된 라즈베리 파이에서 `sudo rpi-update` 명령어를 통해서 펌웨어를 최신버젼으로 갱신한다.

현재 라즈베리 파이 펌웨어 정보는 `vcgencmd version` 명령어로 확인한다.


~~~{.r}
$ vcgencmd version


> #### 왜 우분투(Ubuntu) 배포판이 라즈베리 파이 운영체제가 아닐까? {.callout}
>
> 라즈베리 파이 재단에서 처음에 우분투를 검토했으나 우분투가 ARMv7 이상만 지원하기 때문에
> 라즈비언 배포판을 별도로 개발했다. 
> 하지만, 아치 리눅스는 ARM기반 컴퓨터를 목표로 개발되서 라즈베리 파이에서도 이용가능하다.
~~~
