---
layout: page
title: xwMOOC 컴퓨터
subtitle: 윈도우 가상 개발환경 구축
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 윈도우 가상 개발환경을 구축한다.
> * 가상 개발환경에 소프트웨어 카펜트리, 스파크 빅데이터 분석환경을 설치한다.



### 1. 윈도우 환경 가상 개발환경 개발환경 구축

<img src="fig/aws-virtualbox-architecture.png" width="50%" />

#### 1.1. 가상상자 (버츄얼박스, VirtualBox)

1. 우분투 14.04 설치 이미지를 다운로드한다. [Ubuntu Server 14.04.3 LTS 다운로드](http://www.ubuntu.com/download/server)
1. 가상상자를 다운로드 한다. [가상상자 다운로드](https://www.virtualbox.org/wiki/Downloads)
1. 가상상자에 다운로드 받은 우분투 14.04 버젼을 설치한다.
    - 가상상자를 실행하고 `새로 만들기(N)`를 클릭한다.
    - 가상상자 명칭을 `ubuntu`로 정하고 기본설정값을 따라 설정을 완료하면 `ubuntu` 전원 꺼짐 상태로 가상상자 하나가 생성된다.    
1. `ubuntu` 가상상자를 우클릭 `설정`으로 들어가고 대화상자에서 `어댑터 1` `브리지 어댑터`를 선택하고 저장한다.
1. 다시 `ubuntu` 가상상자를 우클릭하고 `시작(T)`를 눌러 다운로드 받은 우분투 이미지를 선택한다.
1. 일반 컴퓨터에 우분투를 설치하는 기분으로 쭉 설치한다.
    - `root` 사용자 대신 기본 사용자를 정하게 된다. 예를 들어 `xwmooc` 등 임의 사용자를 생성하고, 추후 `ssh` 로그인에 사용한다.

> #### 우분투 `ssh` 원격 로그인 {.callout}
> 
> 기본 설치된 우분투 이미지에는 `ssh` 서비스가 제공되지 않아서 필히 
> `sudo apt-get install -y openssh-server` 명령어로 설치를 해야 원격작업을 할 수 있게 된다.

#### 1.2. 가상상자 접속하기

1. 터미널을 실행하고, `sudo apt-get install openssh-server` 명령어로 ssh 로그인 가능케 소프트웨어를 설치한다.
1. 가상상자 우분투 터미널을 실행하고 `ifconfig` 명령어로 IP주소를 확인한다. 통상 **10.0.2.15** 가 된다.
1. 호스트 운영체제(예, 윈도우가 설치되면 호스트 운영체제는 윈도우)의 IP주소를 확인하는 절차는 `시작` &rarr; `실행(R)` 하고 `ncpa.cpl` 명령어를 입력 혹은, `시작` &rarr; `네트워크 연결` &rarr; `VirtualBox Host-Only Network`을 선택하고 우클릭해서 IP주소를 확인한다. 통상 **192.168.56.1**이된다.
<img src="fig/aws-virtualbox-ip-address.png" width="50%" />
1. 우분투가 설치된 가상상자에 네트워크 환경설정을 한다. 포트포워딩(port forwarding) 기능을 설정해서 호스트 운영체제 명령라인 인터페이스 쉘을 사용해서 `ssh` 로그인한다.
<img src="fig/aws-virtualbox-port-forwarding.png" width="50%" />
    - Host IP는 `192.168.56.1`
    - Guest IP는 `10.0.2.15`
    - `ssh`는 기본포트가 22다. 만약 Host IP를 `2222`로 설정하면 `ssh xwmooc@192.168.56.1 -p 2222` 와 같이 입력해서 로그인해야 된다.
1. `ssh xwmooc@192.168.56.1` 명령어로 우분투가 깔린 가상상자 컴퓨터에 로그인한다.

~~~ {.shell}
$ ssh xwmooc@192.168.56.1
The authenticity of host '192.168.0.11 (192.168.0.11)' can't be established.
ECDSA key fingerprint is 2d:57:2b:2c:38:31:a3:0e:c3:bc:30:13:05:98:b4:fd.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.0.11' (ECDSA) to the list of known hosts.
xwmooc@192.168.0.11's password:
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.19.0-25-generic i686)

 * Documentation:  https://help.ubuntu.com/

58 packages can be updated.
32 updates are security updates.

The programs included with the Ubuntu system are free software; the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law.

xwmooc@xwmooc-VirtualBox:~$
~~~

[참조: 우분투 14.04 서버 세팅하기 (Virtual Box)](http://rorlab.gitbooks.io/railsguidebook/content/appendices/ubuntu14server.html)

[참조: VirtualBox Ubuntu 기본 환경에서 ssh 접근하기](http://junho85.tistory.com/259)


#### 1.3. 부랑자(Vagrant) 설치

[부랑자(Vagrant)](https://www.vagrantup.com/)는 가상 개발 환경을 생성하고 환경설정을 가능케하는 소프트웨어로, 초기에는 [버츄얼 박스](https://www.virtualbox.org/)만 지원했으나, 1.1버젼 이후에는 VMWare, KVM, LXC(리눅스 컨테이너), 다양한 형상관리 소프트웨어와 함께 사용할 수 있고, 특히 1.6버젼 이후 도커 컨테이너를 지원한다.

[부랑자 다운로드](https://www.vagrantup.com/downloads.html) 웹사이트에서 소프트웨어는 다운로드 받으면 된다. 

> #### 다양한 부랑자 공개 박스 {.callout}
>
> - [Hashicorp Atlas](https://atlas.hashicorp.com/boxes/search)
> - [Vagrantbox.es](http://www.vagrantbox.es/)

디렉토리를 하나 생성하고 그 디렉토리로 이동해서 원하는 부랑자 박스 명칭을 입력한다.
`vagrant init ubuntu/trusty64` 명령어를 통해서 `.vagrant` 와 `Vagrant` 파일이 자동 생성된다.
`vagrant up` 명령어는 `Vagrant` 설정정보에 맞춰 부랑자 상자를 생성한다. `vagrant ssh` 명령어로 다운로드받은 가상 우분투 컴퓨터에 접속한다.

~~~ {.shell}
$ vagrant init ubuntu/trusty64
$ vagrant up
$ vagrant ssh
~~~
[Vagrantbox.es](http://www.vagrantbox.es/) 사이트를 활용할 경우 원하는 부랑자 박스를 찾아 `vagrant box add` 명령어로 추가하고 `vagrant init` 와 `vagrant up` 명령어로 설치한다.

~~~ {.shell}
$ vagrant box add https://atlas.hashicorp.com/ARTACK/boxes/debian-jessie
==> box: Loading metadata for box 'https://atlas.hashicorp.com/ARTACK/boxes/debian-jessie'
==> box: Adding box 'ARTACK/debian-jessie' (v8.1.0) for provider: virtualbox
    box: Downloading: https://atlas.hashicorp.com/ARTACK/boxes/debian-jessie/versions/8.1.0/providers/virtualb
    box: Progress: 100% (Rate: 894k/s, Estimated time remaining: --:--:--)
==> box: Successfully added box 'ARTACK/debian-jessie' (v8.1.0) for 'virtualbox'!
$ vagrant init ARTACK/debian-jessie
$ vagrant up
$ vagrant ssh
~~~

### 2. 가상 개발환경 개발 사례

#### 2.1. 파이썬 소프트웨어 카펜트리 

[소프트웨어 카펜트리 부랑자 환경설정](https://github.com/cfriedline/vagrant-swc) 사이트에서 `git clone` 명령어로 복제한다.

- 가상상자와 부랑자를 설치한다.
- [Software Carpentry Vagrant](https://github.com/cfriedline/vagrant-swc) 환경파일을 복제한다.
- 복제한 디렉토리로 변경한다.
- `vagrant up` 실행한다.
- `vagrant ssh`를 통해 배쉬쉘 접속한다.

#### 2.2. 빅데이터 스파크(Spark) 가상 컴퓨터 설치 

[GitHub](https://github.com/)에 공개된 버츄얼박스 [아파치 스파트(Spark)](https://spark.apache.org/) 이미지를 다운로드 받아 실습해본다. [https://github.com/spark-mooc/mooc-setup/archive/master.zip](https://github.com/spark-mooc/mooc-setup/archive/master.zip) 파일을 다운로드한다.

~~~ {.input}
[xwmooc:~/spark ] $ wget https://github.com/spark-mooc/mooc-setup/archive/master.zip^C
[xwmooc:~/spark ] $ unzip master.zip 
[xwmooc:~/spark ] $ wget http://nbviewer.ipython.org/github/spark-mooc/mooc-setup/blob/master/lab0_student.ipynb
[xwmooc:~/spark ] $ ls
~~~
~~~ {.output}
lab0_student.ipynb  master.zip  mooc-setup-master
~~~

**`Vagrant up`을 통한 실행**

`vagrant up`을 통해 격리된 가상컴퓨터를 실행하기 위해서 먼저 *Vagrantfile*이 있는 곳에서 실행한다. 유닉스 `make` 명령어가 `Makefile`에 설정을 실행하는 것에 비견된다. 가상컴퓨터를 인터넷을 통해 설치를 진행하는만큼 시간이 제법 걸리니 커피를 한잔하고 와도 좋다.

~~~ {.input}
[xwmooc:~/spark/mooc-setup-master ] $ vagrant up
~~~
~~~ {.output}
Bringing machine 'sparkvm' up with 'virtualbox' provider...
==> sparkvm: Box 'sparkmooc/base' could not be found. Attempting to find and install...
    sparkvm: Box Provider: virtualbox
    sparkvm: Box Version: >= 0
==> sparkvm: Loading metadata for box 'sparkmooc/base'
    sparkvm: URL: https://atlas.hashicorp.com/sparkmooc/base
==> sparkvm: Adding box 'sparkmooc/base' (v0.0.7.1) for provider: virtualbox
    sparkvm: Downloading: https://atlas.hashicorp.com/sparkmooc/boxes/base/versions/0.0.7.1/providers/virtualbox.box
==> sparkvm: Successfully added box 'sparkmooc/base' (v0.0.7.1) for 'virtualbox'!
==> sparkvm: Importing base box 'sparkmooc/base'...
==> sparkvm: Matching MAC address for NAT networking...
==> sparkvm: Checking if box 'sparkmooc/base' is up to date...
==> sparkvm: Setting the name of the VM: sparkvm
==> sparkvm: Clearing any previously set network interfaces...
==> sparkvm: Preparing network interfaces based on configuration...
    sparkvm: Adapter 1: nat
==> sparkvm: Forwarding ports...
    sparkvm: 8001 => 8001 (adapter 1)
    sparkvm: 4040 => 4040 (adapter 1)
    sparkvm: 22 => 2222 (adapter 1)
==> sparkvm: Booting VM...
==> sparkvm: Waiting for machine to boot. This may take a few minutes...
    sparkvm: SSH address: 127.0.0.1:2222
    sparkvm: SSH username: vagrant
    sparkvm: SSH auth method: private key
    sparkvm: Vagrant insecure key detected. Vagrant will automatically replace
    sparkvm: this with a newly generated keypair for better security.
    sparkvm: 
    sparkvm: Inserting generated public key within guest...
    sparkvm: Removing insecure key from the guest if its present...
    sparkvm: Key inserted! Disconnecting and reconnecting using new SSH key...
==> sparkvm: Machine booted and ready!
==> sparkvm: Checking for guest additions in VM...
==> sparkvm: Setting hostname...
==> sparkvm: Mounting shared folders...
    sparkvm: /vagrant => /home/statkclee/spark/mooc-setup-master
~~~

`http://localhost:8001/` 혹은 `http://127.0.0.1:8001/`을 웹브라우저 주소창에 입력하게 되면 스파크를 *ipython*을 통해 사용할 수 있다. 


<img src="fig/aws-virtual-machine-spark-ipython.png" width="50%" alt="스파크를 가상상자 부랑자(Vagrant)를 통해 실행한 화면" />


부랑자(Vagrant)를 정지하는 명령어는 `vagrant halt`다.

~~~ {.input}
[xwmooc:~/spark/mooc-setup-master ] $ vagrant halt
~~~
~~~ {.output}
==> sparkvm: Attempting graceful shutdown of VM...
~~~

**버츄얼박스 sparkvm 가상컴퓨터 CLI에서 실행**

`VBoxManage startvm` 명령어를 통해서 `sparkvm` 가상컴퓨터를 시작한다.

~~~ {.input}
[xwmooc:~/spark/mooc-setup-master ] $ VBoxManage startvm sparkvm --type headless
~~~
~~~ {.output}
Waiting for VM "sparkvm" to power on...
VM "sparkvm" has been successfully started.
~~~

`VBoxManage controlvm` 명령어를 통해서 `sparkvm` 가상컴퓨터를 끈다(poweroff).

~~~ {.input}
[xwmooc:~/spark/mooc-setup-master ] $ VBoxManage controlvm sparkvm poweroff
~~~
~~~ {.output}
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
~~~

#### 2.3. 웹서버 (아파치)

가상상자에 웹서버를 설치해서 웹인터페이스를 이용하여 접근할 수 있다. 
`sudo apt-get install apache2` 명령어를 통해서 아파치 웹서비스를 설치한다. 
필요시 `sudo service apache2 restart` 명령어를 통해서 아파치 웹서비스를 재시작한다.

~~~ {.shell}
xwmooc@xwmooc-VirtualBox:~$ sudo apt-get install apache2
xwmooc@xwmooc-VirtualBox:~$ sudo service apache2 restart
~~~

가상상자를 정지하고 `Settings` &rarr; `Network` &rarr; `Adapter`에서 **Port Forwarding**으로 가서 `80` 포트를 등록하면 웹브라우져를 통해 가상상자에서 제공하는 웹서비스를 받을 수 있다.

<img src="fig/aws-virtualbox-webservice.png" width="70%" alt="가상상자 웹서비스 포트포워딩 설정" />

웹브라우져 주소창에 `http://localhost`를 입력하면 웹서비스가 제공되는 것을 확인할 수 있다.

### 3. 가상상자 용량 크게 늘리기

가상상자를 사용하다보면 초기 4G, 8G로 설정한 것이 어느 순간 부족함을 느낄 때가 있다. 이런 경우 이미지 크기재조정(image resize) 기능을 사용해서 저장공간을 늘리거나 필요가 없을 경우 줄일 수 있다.

가상상자 명령어는 `vboxmanage`로 윈도우의 경우 `c:\Program Files\Oracle\VirtualBox` 디렉토리에 프로그램이 저장되어 있고, 이미지는 `C:\Users\admin\VirtualBox VMs` 디렉토리에 저장된다.

1. 최신 가상상자 이미지가 돌고 있는 `.vmdk` 확장자 파일을 `.vdi` 확장자 파일로 변환한다.

~~~ {.shell}
$ "c:\Program Files\Oracle\VirtualBox\vboxmanage" clonehd "C:\Users\admin\VirtualBox VMs\ubuntu\ubuntu-disk1.vmdk" "C:\ubuntu.vdi" --format VDI
~~~
~~~ {.output}
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Clone medium created in format 'VDI'. UUID: 4eca716c-8c73-42da-97fd-cfd34d266d4d
~~~

2. `vboxmanage modifyhd` 명령어로 `--resize 20000` 인자를 줘서 이미지 크기를 기존 8G에서 20GB로 변경한다.

~~~ {.shell}
 $ "c:\Program Files\oracle\VirtualBox\VBoxManage.exe" modifyhd ubuntu.vdi --re
size 20000
~~~
~~~ {.output}
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
~~~

3. 정상적으로 생성되었는지는 `vboxmanage list hdds` 명령어로 확인한다.

~~~ {.shell}
$ "c:\Program Files\oracle\VirtualBox\VBoxManage.exe" list hdds
~~~

~~~ {.output}
UUID:           4eca716c-8c73-42da-97fd-cfd34d266d4d
Parent UUID:    base
State:          inaccessible
Type:           normal (base)
Location:       c:\Program Files\Oracle\VirtualBox\ubuntu.vdi
Storage format: VDI
Capacity:       8192 MBytes
Encryption:     disabled

UUID:           e4368f6f-30d6-42a6-9191-94e588b3f572
Parent UUID:    base
State:          created
Type:           normal (base)
Location:       c:\ubuntu.vdi
Storage format: VDI
Capacity:       20000 MBytes
Encryption:     disabled
~~~

4. `.vdi` 파일을 가상상자로 다른 일반 이미지와 마찬가지로 불러온다.
5. 가상으로 이미지 공간이 잡힌 것이기 때문에 우부투의 경우 `gparted` 를 통해서 운영체제에서 파티션을 재정하는 작업을 하면 증가시킨 공간을 활용가능하다.

- [참고:VirtualBox 디스크 용량 변경하기(resize)](http://idchowto.com/index.php/virtualbox-디스크-용량-변경하기resize/)
- [참고: VirtualBox 저장소(VDI) 용량 늘리기](http://leechwin.tistory.com/17)
