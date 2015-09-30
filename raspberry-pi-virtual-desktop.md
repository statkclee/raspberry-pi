---
layout: page
title: xwMOOC 컴퓨터
subtitle: 라즈베리 파이 가상화 : 데스크톱
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 라즈베리 파이를 가상화한다.

### 1. 라즈베리 파이 과학 컴퓨팅 툴체인 구축


[참고: 라즈베리 파이에 Python Anaconda, IPython-notebook, PIP 설치 방법](http://gongnorina.tistory.com/42)

### 1. 라즈비언 데스트톱 가상화

윈도우 환경에서 라즈베리 파이 운영체제 라즈비언을 가상화하여 실행한다.

1. [Raspberry Pi emulation for Windows](http://sourceforge.net/projects/rpiqemuwindows/)를 다운로드 한다.
1. 다운로드 받은 파일의 압축을 푼다.
1. `run.bat` 파일을 실행하면 윈도우 환경에서 라즈비언을 실행할 수 있다.

[참고: Install and Run QEMU (Raspbian Emulator) on Windows](https://www.youtube.com/watch?v=rj1QCSJjysM)

### 2. 부랑자(Vagrant) 가상 컴퓨터 접속

1. 작업 디렉토리를 생성하고 해당 디렉토리로 이동한다. `mkdir vagrant-directory`, `cd vagrant-directory`가 명령어가 된다.
1. 원하는 가상상자 이미지를 다운로드한다. 많이 검색하는 사이트는 다음과 같다.
    - (Vagrantbox.es)[http://www.vagrantbox.es/] 
    - (http://atlas.hashicorp.com)[https://atlas.hashicorp.com/boxes/search]
1. `vagrant init ARTACK/debian-jessie` 으로 초기화한다.
1. `vagrant box add ARTACK/debian-jessie` + URL을 조합하여 다운로드 한다.
1. `vagrant up` 명령어로 데비안 제시 버젼 리눅스 가상상자를 실행한다.
1. `vagrant ssh` 명령어로 로그인한다.

~~~ {.shell}
[xwmooc:~ ] $ mkdir vagrant-directory
[xwmooc:~ ] $ cd vagrant-directory/
[xwmooc:~/vagrant-directory ] $ vagrant init ARTACK/debian-jessie
~~~

~~~ {.output}
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
~~~

~~~ {.shell}
[xwmooc:~/vagrant-directory ] $ vagrant box add ARTACK/debian-jessie https://atlas.hashicorp.com/ARTACK/boxes/debian-jessie
~~~

~~~{.shell}
[xwmooc:~/vagrant-directory ] $ vagrant up
[xwmooc:~/vagrant-directory ] $ vagrant ssh
~~~

~~~ {.outpu}
The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Jul  3 11:17:55 2015 from 10.80.50.110
vagrant@debian:~$
~~~

~~~ {.shell}
[xwmooc:~/vagrant-directory ] $ sudo apt-get update
[xwmooc:~/vagrant-directory ] $ sudo apt-get install apache2
~~~

`Vagrantfile`을 열어 사설 네트워크 주석을 해제하고 저장한다. 웹브라우져를 열고 주소창에 `192.168.33.10` 주소를 입력하면 웹서비스가 정상 작동하는 것을 확인할 수 있다.

~~~ {.shell}
config.vm.network "private_network", ip: "192.168.33.10"
~~~

<img src="fig/virtual-vagrant-apache.png" width="50%" />

[참고: Vagrant Beginner (Part 1)](https://www.youtube.com/watch?v=ZGUEjZckijA)














