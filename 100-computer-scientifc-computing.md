---
layout: page
title: xwMOOC 컴퓨터
subtitle: $100 달러 오픈 컴퓨터 과학 컴퓨팅 툴체인
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * $100 달러 오픈 컴퓨터 과학 컴퓨팅 툴체인을 구축한다.
> * 라즈베리 파이 `ssh`, `VNC` 로그인 접속한다.
> * ipython과 ipython notebook을 설치하고 웹 인터페이스를 통해 접속한다.

### 1. 라즈베리 파이 접속

1. 라즈베리 파이 컴퓨터에 `ssh` 명령어를 통해서 명령라인 인터페이스(CLI) 접속한다. 
    - [유튜브 동영상](https://youtu.be/fMsSFypP6Cs)
1. 라즈베리 파이 컴퓨터에 **VNC(Virtual Network Computing)**을 설치하고 그래픽 사용자 인터페이스(GUI) 방식으로 접속한다.
    - `ssh`로 라즈베리 파이 접속하고 `sudo apt-get install tightvncserver` 명령어로 서버를 설치한다.
    - `tightvncserver` 명령어로 서버에 접속할 비밀번호를 설정한다.
    - `vncserver :0 -geometry 1920x1080 -depth 24` 명령어로 서버를 실행한다.
    - 참고: [VNC (VIRTUAL NETWORK COMPUTING)](https://www.raspberrypi.org/documentation/remote-access/vnc/)
    - [유튜브 동영상](https://youtu.be/VjQaijI8fgo)

>### VNC를 자동화 하는 방법 {.callout}
>  
>  1. 쉘스크립트를 사용해서 필요시 실행하는 방법
> 
> ~~~ {.shell}
> #!/bin/sh
> vncserver :0 -geometry 1920x1080 -depth 24 -dpi 96
> ~~~
> `nano vnc.sh` 파일을 생성하고 상기 내용을 저장한다. 
> 
> ~~~ {.shell}
> $ chmod +x vnc.sh
> ~~~
> 저장한 쉘스크립트 파일을 실행파일로 변경한다.
> 
> ~~~ {.shell}
> $ ./vnc.sh
> ~~~
> `./vnc.sh` 명령어로를 통해서 VNC 서버를 실행하고 `tightvncviewer`를 통해 라즈베리 파이 GUI 방식으로 사용한다.
> 
> 2. 자동으로 부팅하여 VNC 서버를 띄워 사용하는 방법
> 
> 루트 권한으로 로그인하고 `/etc/init.d/` 디렉토리로 이동해서 `vncboot` 파일을 생성하고 아래 아래 파일 내용을 복사해서 붙여넣는다. `chmod 755 > vncboot` 명령어로 텍스트를 실행파일로 만들고, `update-rc.d /etc/init.d/vncboot defaults` 혹은 `update-rc.d vncboot defaults` 명령어로 > 갱신한다. 그리고 다시 부팅하면 쉘스크립트를 실행하거나 타이핑하지 않고 VNC 서버를 띄울 수 있다.
> 
> ~~~ {.shell}
> $ sudo su
> $ cd /etc/init.d/
> $ nano vncboot
> $ chmod 755 vncboot
> $ update-rc.d /etc/init.d/vncboot defaults
> $ update-rc.d vncboot defaults
> $ sudo reboot
> ~~~
> 
> **`vncboot` 파일 입력 사항**
>
>~~~ {.shell}
>### BEGIN INIT INFO
># Provides: vncboot
># Required-Start: $remote_fs $syslog
># Required-Stop: $remote_fs $syslog
># Default-Start: 2 3 4 5
># Default-Stop: 0 1 6
># Short-Description: Start VNC Server at boot time
># Description: Start VNC Server at boot time.
>### END INIT INFO
>
>#! /bin/sh
># /etc/init.d/vncboot
>
>USER=pi
>HOME=/home/pi
>
>export USER HOME
>
>case "$1" in
> start)
>  echo "Starting VNC Server"
>  #Insert your favoured settings for a VNC session
>  su - pi -c "/usr/bin/vncserver :0 -geometry 1280x800 -depth 16 -pixelformat rgb565"
>  ;;
>
> stop)
>  echo "Stopping VNC Server"
>  /usr/bin/vncserver -kill :0
>  ;;
>
> *)
>  echo "Usage: /etc/init.d/vncboot {start|stop}"
>  exit 1
>  ;;
>esac
>
>exit 0
>~~~

### 2.  ipython과 ipython notebook을 통한 웹인터페이스 접속

#### 2.1. ipython 설치 및 접속

`sudo apt-get install ipython` 명령어로 설치하고, `ipython` 명령어를 통해서 실행한다. `len?`을 입력하고 엔터를 치면 도움말을 확인할 수 있다.

~~~~ {.shell}
$ sudo apt-get install ipython
~~~~
- [유튜브 동영상](https://youtu.be/hUNM4gKcT80)
- [참고: MORE ON PYTHON](https://www.raspberrypi.org/documentation/usage/python/more.md)

#### 2.2. ipython 노트북 설치 및 접속

ipython notebook을 설치하기 전에 의존성을 갖는 `python-pip` 파이썬 팩키지 관리자와 `simplejson`을 설치한다. 그리고 ` sudo apt-get install ipython-notebook` 명령어로 아이파이썬 노트북을 설치한다. 과학 컴퓨팅을 위해 많이 사용되는 `python-matplotlib python-scipy python-pandas python-sympy python-nose` 팩키지를 일괄 설치한다. `ipython notebook` 명령어로 실행한다.

~~~ {.shell}
$ sudo apt-get install python-pip
$ sudo pip install simplejson
$ sudo apt-get install ipython-notebook
$ sudo apt-get install python-matplotlib python-scipy python-pandas python-sympy python-nose
$ ipython notebook
~~~  
- [유튜브 동영상](https://youtu.be/BWcWBh5cJsg)

#### 2.3. ipython 노트북 원격 접속

ipython 노트북을 원격 웹브라우져에서 접속하기 위해서는 해당 라즈베리 파이 IP주소를 확인하고 열어줄 포트를 설정하여 실행한다.

~~~ {.shell}
$ ifconfig eth0
$ipython notebook --no-browser --ip=192.168.103.135 --port=8889
~~~

- [유튜브 동영상](https://youtu.be/ftY7wh11oH8)
- [참고: Run ipython notebook from a remote server](http://stackoverflow.com/questions/24490278/run-ipython-notebook-from-a-remote-server)


### 3. xwMOOC $100 달러 컴퓨터 실행

컴퓨터 교육을 공개 5종 콘텐츠가 설치된 xwMOOC $100 달러 컴퓨터 

*   [컴퓨터과학 언플러그드](http://unplugged.xwmooc.org)
*   [러플(Rur-ple)](http://rur-ple.xwmooc.org/)
*   [정보교육을 위한 파이썬](http://python.xwmooc.org/)
*   [라즈베리 파이](http://raspberry-pi.xwmooc.org/)
*   [소프트웨어 카펜트리](http://swcarpentry.xwmooc.org)

- [유튜브 동영상](https://youtu.be/KZrivRz0D1c)
