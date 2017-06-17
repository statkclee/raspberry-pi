# xwMOOC 라즈베리파이




## 1. 라즈베리 파이에 접근하는 세가지 방법

라즈베리 파이에 접근하는 세가지 방법은 명령라인인터페이스(CLI), 데스크톱(GUI), 웹을 통한 세가지 방법이 있다.

### 1.1. XRDP 원격 데스크톱 접근


~~~{.r}
# 원격 데스트톱 연결 프로그램 설치 및 설정
pi@raspberrypi ~ $ sudo apt-get update
pi@raspberrypi ~ $ sudo apt-get install -y xrdp
pi@raspberrypi ~ $ sudo service xrdp restart # sudo /etc/init.d/xrdp start 명령어도 가능.
~~~

|  원격 데스크톱 | 승인 | 연결 연결된 화면 | 
|:-------------------------------:|:----------------------------------:|:----------------------------------:|
| <img src="fig/raspberry-pi-mstsc-01.png" width="100%" />    |  <img src="fig/raspberry-pi-mstsc-02.png" width="100%" />  |  <img src="fig/raspberry-pi-mstsc-connected.png" width="70%" />  | 

원격 데스크톱 서비스를 이용할 수 있는 다양한 방법이 있다.
[Xming](http://www.raspians.com/knowledgebase/?knowledgebase=setting-up-a-remote-desktop-view-the-pi-on-your-windows-pc/), [VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)를 사용하여 `mstsc` 원격 데스크톱 연결과 같은 효과를 낼 수 있다. 

### 1.2. 명령라인 인터페이스 CLI를 통한 방법

__Git Bash__를 설치하고 콘솔에서 라즈베리 파이 IP를 입력한다. 명령어는 `ssh pi@192.168.103.107`으로 ssh (보안쉘, Secure Shell)로 `192.168.103.107` IP를 갖는 호스트 컴퓨터에 `pi`사용자로 로그인한다.
비밀번호는 `raspberry`를 입력하면 라즈베리파이에 로그인했다.


~~~{.r}
admin@STATxxxxxx /c/pyr-cloudlayer (gh-pages)
$ ssh pi@192.168.103.107
pi@192.168.103.107 s password:
Linux raspberrypi 3.18.11-v7+ #781 SMP PREEMPT Tue Apr 21 18:07:59 BST 2015 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Jul 30 16:59:13 2015 from 192.168.103.125
pi@raspberrypi ~ $
~~~

### 1.3. 웹 인터페이스를 통한 방법

라즈베리파이를 웹서버로 만들기 위해서 아파치 웹서버를 설치한다. `sudo apt-get install -y apache2` 명령어를 콘솔에서 입력하면 아파치 웹서버가 설치되어 웹브라우져를 통해 라즈베리파이에 접근할 수 있다.


~~~{.r}
pi@raspberrypi ~ $ sudo apt-get install -y apache2
~~~

`/var/www/` 폴더에 `index.html` 파일을 수정하거나 개발된 웹서비스를 웹서비스 제공 디렉토리에 저장하면 된다.

<img src="fig/raspberry-pi-webserver.png" width="70%" />

## 2. 유선이나 무선상태에서 가장 많이 사용되는 CLI/GUI 로그인

<img src="fig/rpi-cli-vnc-connect.png" alt="유무선 RPi 접속" width="77%" />

유선이나 무선을 통해 다양한 방식으로 라즈베리파이에 접속을 할 수 있다.
그리고, 명령라인 인터페이스(CLI), 그래픽사용자 인터페이스(GUI)를 통해 접속하는 방법도 생각할 수 있다.

유선이나 무선 각기 장단점이 있으므로 개발자가 처한 환경에서 최적의 선택을 하면 좋겠다.
유선인 경우 별도 IP주소 확인이 필요하지 않고 안정적인 연결이 가능한 반면 별도 연결선이 필요하고 개발환경이 
와이어링 연결선으로 지저분해지는 단점은 감수한다.

무선은 깔끔하기는 하지만 IP주소를 확인해야 하고 이에 대해 여러 설정을 해줘야 하는 번거러음이 있다.

### 2.1. CLI 터미널 접속

명령라인 인터페이스를 통해 라즈베리파이에 접속할 경우 유선과 무선으로 나눠진다.
앞서 언급하였듯이 무선의 경우 IP주소를 확인하는 과정이 필요하고, 유선인 경우는 그 과정을 단일화하게 된다.

#### 2.1.1. 무선 CLI 터미널 접속

윈도우를 비롯한 리눅스와 맥에서 `ssh` 로그인 하는 경우 먼저 `hostname -I` 명령어를 통해 IP 주소를 확인하고 이를 확인해서 `ssh pi@<IP주소>` 방식으로 로그인한다.
 
RPi 터미널에서 먼저 사전에 확인할 사항은 IP주소를 확인한 것이다.



~~~{.r}
pi@raspberrypi:~ $ hostname -I
192.168.0.11
~~~

리눅스 혹은 맥 터미널에서 확인된 RPi IP주소, `192.168.0.11` 입력하여 로그인한다.
 

~~~{.r}
$ ssh pi@192.168.0.11 
pi@192.168.0.11 s password: 
~~~

외부 IP주소를 통해 접속할 경우 IP주소를 넣고 `ssh IP주소 -l pi` 명령어로 로그인 접속한다.
여기서 사전에 확인할 사항은 라즈베리파이에 ssh-server가 설치되어야 한다.

즉,`sudo apt-get install openssh-server` 명령어로 라즈베리파이에 사전에 설치를 완료한다.


~~~{.r}
raspberry-pi $ ssh 169.XXX.XX.XXX -l pi
The authenticity of host '169.XXX.XX.XXX (169.XXX.XX.XXX)' can't be established.
ECDSA key fingerprint is SHA256:yy7lEiSYXXXXXXXXXXXXXXXXXaakW5/7KXXXXX4.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '169.XXX.XX.XXX' (ECDSA) to the list of known hosts.
pi@169.XXX.XX.XXX's password: 

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have new mail.
Last login: Sat Jun 17 11:03:38 2017 from XX0::XX60:4XXX:7XXX:1XXX%wlan0
pi@raspberrypi:~ $ 
~~~

#### 2.1.2. 유선 CLI 터미널 접속

유선 CLI를 통해 라즈베리파이에 접속할 경우 `ssh pi@raspberrypi.local` 명령어를 입력하고
비밀번호 `raspberry`를 입력하면 바로 로그인할 수 있게 된다.


~~~{.r}
raspberry-pi $ ssh pi@raspberrypi.local
pi@raspberrypi.local s password: 

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have new mail.
Last login: Sat Jun 17 10:05:44 2017 from XX0::XX60:4XXX:7XXX:1XXX%wlan0
pi@raspberrypi:~ $ 
~~~

<img src="fig/rpi-minecraft-vnc.png" alt="라즈베리파이 마인크래프트 VNC 실행" width="70%" />

### 2.2. GUI VNC 연결 [^dexter-vnc]

[^dexter-vnc]: [Virtually Control the Raspberry Pi](https://www.dexterindustries.com/howto/virtually-control-the-raspberry-pi/)

그래픽 사용자 인터페이스를 통해 라즈베리파이에 접속하게 되면 마인크래프트를 구매하지 않고도 
PC에서 게임을 즐길 수 있는 장점이 있다. 즉, 마인크래프트 라이선스 구매비용 약 3만원 대신 
라즈베리파이 하드웨어를 구매하게 되면 그 내부에 포함되어 있어 일석이조가 된다.

VNC 뷰어(VNC Viewer)를 다운로드받아 설치하고 나서 `VNC Viewer`를 실행한다.

#### 2.2.1. 유선 VNC 연결

VNC 뷰어를 실행하게 되면 연결에 필요한 정보를 넣는 화면이 나온다.
VNC Server에 `raspberrypi.local` 을 입력하고 Name은 적당한 이름을 임의로 적어 넣고 OK를 누르면 된다.

연결되면 로그인 ID와 비밀번호를 요구하는데, 접속하는 컴퓨터가 라즈베리파이이기 때문에 `pi`, `raspberry`를 
각각 ID와 비밀번호로 입력하게 되면 된다.

<img src="fig/rpi-vnc-local.png" alt="라즈베리파이 VNC 연결" width="50%" />

#### 2.2.2. 무선 VNC 연결

무선도 VNC 뷰어를 통해 접속하는 것이 동일하다. 다만 차이가 있다면, `raspberrypi.local` 대신에
IP주소를 넣어주는 것이 차이가 된다. 예를 들어 `210.29.100.23` 주소에 `210.29.100.23:1`, `210.29.100.23:2`와 같이
다중접속도 가능하다. 단 서비스를 별도로 열어줘야 가능하게 된다.

> ### 마인크래프트 해상도 설정 [^rpi-minecraft] {.callout}
> 
> VNC에서 마인크래프트를 실행하게 되면 검은 화면이 나와 이를 맞춰주는 작업이 필요하다.
> 
> 
> ~~~{.r}
> $ sudo nano /root/.vnc/config.d/vncserver-x11
> ~~~
> 
> 명령어를 실행하여 다음 내용을 저장한다. 
> 
> 
> ~~~{.r}
> CaptureTech=raspi
> ExperimentalRaspiCapture=1
> ServerPreferredEncoding=JPEG
> ~~~
> 
> 그리고 나서, 다음 명령어를 실행하면 정상적으로 마인크래프트가 실행되는 것이 확인된다.
> 
> 
> ~~~{.r}
> $ sudo systemctl restart vncserver-x11-serviced
> ~~~

[^rpi-minecraft]: [Minecraft from VNC](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=162495)










