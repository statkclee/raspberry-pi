---
layout: page
title:  xwMOOC 컴퓨터
subtitle: 소프트웨어 카펜트리 가상 개발환경
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> *  소프트웨어 카펜트리 툴체인 소개
> *  소프트웨어 카펜트리 가상 개발환경 가상상자 및 부랑자 설치
> *  라즈베리 파이를 소프트웨어 카펜트리 교육에 사용할 이미지 생성

### 1. 소프트웨어 카펜트리란?

#### 1.1. 소프트웨어 카펜트리 소개 원문

*  [Introducing Software Carpentry](http://swcarpentry.github.io/slideshows/introducing-software-carpentry/index.html)
*  [Software Carpentry: Lessons Learned](http://swcarpentry.github.io/slideshows/lessons-learned/index.html)
*  [Best Practices for Scientific Computing](http://swcarpentry.github.io/slideshows/best-practices/index.html)

- 소프트웨어 카펜트리 MOOC (2010)
    *  [SW Carpentry Version 4](http://software-carpentry.org/lessons.html)

#### 1.2. 대한민국 소프트웨어 카펜트리 

- [파이콘 2015 라이트닝 토크](http://www.pycon.kr/2015/program/77)
    * [한국에서 소프트웨어 카펜트리 1년...](./korea/index.html)  
- 소프트웨어 카펜트리 교재
    *  [GitHub 저장소](https://github.com/statkclee/xwmooc-sc)
    *  [xwMOOC 소프트웨어 카펜트리](http://xwmooc.net/swcarpentry/)
- 소프트웨어 카펜트리 워크샵
    *  [한국전파진흥협회(RAPA)](http://statkclee.github.io/2015-02-25-seoul/)
    *  [경기콘텐츠코리아랩](http://statkclee.github.io/2015-04-29-pangyo/)
    *  [연세대학교](http://statkclee.github.io/2015-06-29-yonsei/)
    *  [나노종합기술원 대전창조경제혁신센터](http://statkclee.github.io/2015-08-20-daejeon/)

### 2. 소프트웨어 카펜트리 툴체인(Tool chain)

소프트웨어 카펜트리 워크샵에는 소프트웨어 전반적인 교육을 위해서 리눅스 기반 다양한 소프트웨어가 사용되고 툴체인을 구성한다.

#### 2.1. 작업 자동화와 프로그래밍을 위한 주요 소프트웨어 

- 유닉스 쉘 &nbsp;&rArr; 작업자동화
    - 윈도우에서 유닉스 쉘 대용으로 사용되는 [Git Bash](https://git-for-windows.github.io/)가 라즈비언에는 배쉬 쉘(Bash Shell)이 기본으로 장착되어 있다.
        - GNU 배쉬 버젼: GNU bash, version 4.2.37
    - `nano` 편집기 자동 설치됨.
- Git 과 GitHub &nbsp;&rArr; 작업 추적과 협업
    - [Git]()도 자동으로 설치되어 있음. `git version 1.7.10.4`
- 파이썬, R, 매트랩 &nbsp;&rArr; 모듈방식 코드 작성
    - 라즈베리 파이에 파이(PI, Python Interpreter)가 의미하듯이 파이썬2, 파이썬3가 자동으로 설치됨
        - 파이썬 2 버젼: `Python 2.7.3`
        - 파이썬 3 버젼: `Python 3.2.3`
    - R 설치해야 됨
    - [매트랩](http://www.mathworks.com/)은 매스웍스(Mathworks)사의 사용 프로그램으로 별도로 설치해야 됨.
    - 효과적인 과학기술 컴퓨팅을 위해 아나콘다(Anaconda)를 설치한다.
        - [Continuum Analytics](http://continuum.io/downloads) 웹사이트에서 리눅스 펭귄 턱스를 클릭하여 파이썬 2, 파이썬 3 버젼에 맞춰 다운로드 한후 `bash` 명령어로 설치한다.
        - 라즈베리 파이 2는 32비트 컴퓨터로 가능하면 32비트 버젼을 다운로드 받는다.
        - 디렉토리를 지정하야 하는데 디폴트 기본설정으로 `/home/pi/anaconda3/` 디렉토리가 지정된다. 만약 파이썬 2 아나콘다를 다운로드하면 기본 디렉토리가 `/home/pi/anaconda/`로 된다. 
- SQL &nbsp;&rArr; 데이터 관리
    - `sudo apt-get install sqlite3` 명령어를 통해서 간단히 sqlite3 데이터베이스를 설치한다.
    - `sqlite3 --version` 명령어를 타이핑하면 `3.7.13 2012-06-11 02:05:22 f5b5a13f7394dc143aa136f1d4faba6839eaa6dc` 결과 출력된다.

#### 2.2. 한글화 및 웹서버 관련 소프트웨어

라즈베리 파이 기반 소프트웨어 카펜트리 교육을 위해서 한글 설정과 웹서버 및 자주 사용하는 웹브라우져를 설치한다.

- 한글 입력기 `ibus`를 통한 한글 설정 
    - `sudo apt-get install ibus ibus-hangul` 명령어를 한글 입력기를 설치한다.
    - **ibus**를 설치한 후 시스템 &rarr; 입력기 화면에서 `ibus`를 표준입력기로 설정한다.
    - `ibus 설정` 에서  한국어를 설정하고 나면 키보드와 설정이 맞으면 한/영키를 누르면 한글을 입력할 수 있다.
- 웹브라우져를 통한 외부 접속을 위해 웹브라우져와 웹서버를 설치한다.
    - 기본 장착된 웹브라우져가 있지만, 크롬과 불여우(얼음쪽제비)도 다음 명령어로 설치한다.
        - 크롬 : `sudo apt-get install chromium`
        - 얼음쪽제비(불여우): `sudo apt-get install iceweasel`
    - `sudo apt-get install -y apache2` 명령어로 [아파치 웹서버](http://httpd.apache.org/)를 설치한다.

~~~ {.shell}
pi@raspberrypi ~ $ sudo apt-get install ipython
pi@raspberrypi ~ $ sudo apt-get -y install ipython-notebook
pi@raspberrypi ~ $ sudo apt-get -y install \
                                python-numpy \
                                python-matplotlib \
                                python-scipy \
                                python-pandas \
                                python-sympy \
                                python-nose
~~~


### 3. 가상 개발환경을 사용한 소프트웨어 카페트리 워크샵 툴체인 설치

ARM 계열 라즈베리 파이나 x86 인텔 계열 하드웨어 상에 기본 운영체제를 두고 소프트웨어 카펜트리 툴체인을 구축하는 것도 가능하지만, 하드웨어가 바뀔 때마다 매번 동일한 작업을 반복하는 것도 좋은 접근방법이 아니고, 특정 하드웨어에 맞춰 설치를 하게 되면 일반화가 어렵고, 귀중한 시간을 낭비하는 좋지 못한 경험을 할 수도 있다. 이와 같이 소프트웨어를 설치한다고 하더라도 반듯이 과학 컴퓨팅을 위한 **모든 소프트웨어를 설치한다는 보장도 없다**.

#### 3.1. 루분투 소프트웨어 카펜트리 가상상자 설치 방법

[소프트웨어 카펜트리](http://software-carpentry.org/)에서 워크샵을 위해서 만들어 놓은 가상상자 이미지를 가져와서 툴체인을 설치한다.

1. 가상상자를 설치한다.
    - 윈도우 가상상자 설치방법 : [버추얼박스(VirtualBox) 완벽 설치](http://niceit.tistory.com/187)
    - 리눅스 계열 가상상자 설치방법 : `sudo apt-get install virtualbox`
1. 소프트웨어 카펜트리 가상 파일을 [다운로드](https://docs.google.com/uc?id=0B4Kr6DYkzkQtd05FekRId05DLXM&export=download)한다. 다운로드 파일 명칭은 `swc_lubuntu.ova`이다.
1. `파일` &rarr; `가상 시스템 가져오기`(Import Appliance)를 선택하고 VM을 가져와서 적재한다.
    - 다운로드한 파일은 **OVF(열린 가상화 형식)** 확장자를 갖는다.

[참조: 소프트웨어 카펜트리 워크샵 환경설정](http://software-carpentry.org/workshops/setup.html)

#### 2.2. 부랑자 소프트웨어 카펜트리 설치 방법

루분투 소프트웨어 카펜트리 이미지는 주어진 것이 때문에 한번 생성된 뒤 매번 복사한다는 느낌이다. 반면에 부랑자는 동일한 리눅스 계열 이미지라고 하더라도 설치 시점의 최신 버젼 리눅스를 가져오고 이를 기반으로 해서 소프트웨어 카펜트리 워크샵 툴체인을 위한 소프트웨어를 설치하는 유연성이 있다. 

설치되는 소프트웨어와 환경은 `Vagrantfile` 파일에 담겨 있어서 본인의 환경에 맞춰 유연하게 구성할 수 있는 장점이 있는 반면 추가로 시간을 들여 관련 내용을 학습할 필요가 있다.

1. 가상상자와 부랑자를 설치한다.
    - 윈도우 : [윈도에서 Vagrant-VirtualBox 설치하기](https://www.youtube.com/watch?v=1lgUtcu-03Y)
    - 리눅스 : `sudo apt-get install virtualbox vagrant`
1. [vagrant-swc](https://github.com/cfriedline/vagrant-swc)에 접속해서 `Vagrantfile`을 복제한다.
    - `git clone git@github.com:cfriedline/vagrant-swc.git`
1. Git 복제한 디렉토리로 이동한다.
    - `cd vagrant-swc`
1. `vagrant up` 명령어를 실행한다.
1. `vagrant ssh` 명령어로 접속한다.

소프트웨어 카펜트리 워크샵을 위한 툴체인 구축 쉘스크립트(`setup.sh`)는 다음과 같다.

~~~ {.shell}
#!/bin/bash

# Update the OS and install Software Carpentry requirements
sudo apt-get update -y
sudo apt-get dist-upgrade -y 
sudo apt-get install -y git sqlite3 zsh r-base 

# Install/update Anaconda and adjust environment
ANACONDA_HOME=$HOME/anaconda
wget http://repo.continuum.io/archive/Anaconda-2.0.1-Linux-x86_64.sh
bash Anaconda-2.0.1-Linux-x86_64.sh -b -p $ANACONDA_HOME
echo "PATH=$ANACONDA_HOME/bin:$PATH" >> ~/.bashrc
echo "export PATH" >> ~/.bashrc
$ANACONDA_HOME/bin/conda update --yes conda
$ANACONDA_HOME/bin/conda update --yes anaconda

# Make IPython notebook start at boot
sudo sh -c "echo 'cd /vagrant && $ANACONDA_HOME/bin/ipython notebook --ip=* --no-browser &' > /etc/rc.local"
sudo sh -c "echo 'exit 0' >> /etc/rc.local"

# Restart
sudo reboot
~~~

<img src="fig/virtual-vagrant-swc.png" width="50%" />

[참고: vagrant-swc GitHub](https://github.com/cfriedline/vagrant-swc)


### 4. 소프트웨어 카펜트리 이미지 및 배포

#### 4.1. 소프트웨어 카펜트리 이미지 생성(굽기)

라즈베리 파이를 이용한 소프트웨어 카펜트리 워크샵 소프트웨어 교육 환경을 구축했으면 이를 이미지로 만들어서 동일한 교육환경을 배포한다.

1. [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/)를 다운로드해서 설치한다.
    - 이미지를 생성하고 생성된 이미지를 마이크로 SD카드에 넣는 역할을 윈도우에서 수행하는 프로그램이다.
1. USB에 마이크로 SD카드를 넣고 이미지를 저장할 파일명과 함께 디렉토리를 지정한다.
    - 대략 `C:/_RASPBERRY_PI/SWCarpentry/swcarpentry_hangule_v_5_2_python.img` 와 같다.
1. 이미지를 만들기 위해서 USB 마이크로 SD카드에서 읽어오는 것이기 때문에 **Read**를 클릭하면 이미지가 지정한 디렉토리에 파일명으로 생성된다.

<img src="fig/raspberry-pi-swcarpentry-img.png" width="50%" />

> #### [라즈비언](https://www.raspberrypi.org/downloads/noobs/) NOOBS {.callout}
> NOOBS에 포함된 라즈비언 데비언 위지(Debian Wheezy), 커널 버젼 3.18 기준.
> - 버젼: 1.4.1.
> - 출시일: 2015-05-11
참조: [라즈베리파이 기초 강좌 : SD메모리카드 이미지 백업하기](http://www.rasplay.org/?p=1630)

> #### 소프트웨어 카펜트리 워크샵 소프트웨어 이미지 다운로드 {.callout}
> 제작된 소프트웨어 카펜트리 워크샵 소프트웨어 교육을 위한 이미지는 구글 드라이브에 공유 예정입니다.
>
> [다운로드: SWCarpentry 버젼 5.2. 파이썬 2 기준 (공유 예정)]() 

#### 4.2. 소프트웨어 카펜트리 이미지 넣기

1. [Win32 Disk Imager](http://sourceforge.net/projects/win32diskimager/)를 실행한다.
    - 이미지를 생성하고 생성된 이미지를 마이크로 SD카드에 넣는 역할을 윈도우에서 수행하는 프로그램이다.
1. USB에 마이크로 SD카드를 넣고 [SD Card Formatter](https://www.sdcard.org/downloads/formatter_4/)를 사용해서 포맷을 한다.
1. 이미지 `swcarpentry_hangule_v_5_2_python.img`를 찾는다.
1. USB 마이크로 SD카드에 이미지를 넣는 것이기 때문에 **Write**를 클릭하면 이미지가 설치된다.

<img src="fig/raspberry-pi-swcarpentry-img-copy.png" width="50%" />

> #### 아나콘다와 라즈베리 파이 기본 설치 {.callout}
> 라즈베리 파이 하드웨어는 ARM 계열이라 인텔계열 소프트웨어가 설치가 되지 않는다.
> 따라서, 아나콘다를 바로 라즈베리 파이에 설치가 되지 않아 다른 방법을 모색한다.

참조: [Remote IPython notebook with Raspberry Pi](https://arundurvasula.wordpress.com/2014/04/01/remote-ipython-notebook-with-raspberry-pi/)



