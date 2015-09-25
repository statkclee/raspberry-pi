---
layout: page
title: xwMOOC 컴퓨터
subtitle: 가상 개발환경
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 가상 개발환경을 이해한다.
> * 가상상자와 부랑자를 설치한다.


### 1. 클라우드 하이퍼바이저 유형

개인 가상컴퓨터(Virtual Machine)를 구축하는 방법은 Type 2 유형을 많이 쓴다. 개인 가상컴퓨터가 가능해진 이유는 중앙처리장치 성능이 높아지고 주기억장치 및 보조기억장치 저장공간이 늘어남에 따라 넉넉한 하드웨어 자원을 바탕으로 개인 가상컴퓨터 구축도 매우 쉬워졌다. 개인 가상 컴퓨터를 구축을 위해서 먼저 하이퍼바이저 이해가 필요하다.

[하이퍼바이저(hypervisor)](http://ko.wikipedia.org/wiki/하이퍼바이저)는 호스트 컴퓨터에서 다수의 운영 체제(operating system)를 동시에 실행하기 위한 논리적 플랫폼(platform)을 말한다. 가상화 머신 모니터(virtual machine monitor, 줄여서 VMM)라고도 부른다. 

하드웨어에서 직접 실행되며 운영 체제는 하드웨어 위의 하이퍼바이저 위에서 2번째 수준으로 실행되는 **Type 1 (베어메탈)**형 하이퍼바이저(hypervisor)가 있고, **Type 2**형  하이퍼바이저는 일반 프로그램과 같이 호스트 운영 체제에서 실행되며 VM 내부에서 동작되는 게스트 운영 체제는 하드웨어에서 3번째 수준으로 실행된다. 개인용 가상화 클라우드 환경으로 사용되는 대표적인 것이 오라클 [버추얼박스(Virtual Box)](https://www.virtualbox.org/)다.

출처: [한국 위키피디아](http://ko.wikipedia.org/wiki/하이퍼바이저)

<img src="fig/aws-virtualbox-hypervisor.png" width="50%" alt="클라우드 하이퍼바이저와 버츄얼박스(VirtualBox)" />

X86 중앙처리장치가 올라간 개인용 하드웨어 컴퓨터에 윈도우 운영체제가 주인 운영체제(Host Operating Syste)가 일반적으로 설치된다. 하지만, 개인용 PC 운영체제로 우분투 리눅스를 설치하려고 하면 과거에는 윈도우를 삭제하고 설치해야 됐다. 하지만, [가상상자](https://ko.wikipedia.org/wiki/버추얼박스) 같은 가상화 소프트웨어를 설치하면 윈도우 상태에서 우분투 리눅스를 사용할 수도 있다. 반대로 맥이나 리눅스를 사용한 경우에도 가상화 소프트웨어를 설치하고 윈도를 응용프로그램처럼 사용하는 것도 많이 사용된다.

### 2. 리눅스 환경 가상상자 설치

#### 2.1. 현 리눅스 시스템 환경 파악

맥을 포함한 리눅스 사용자는 윈도우, 윈도우 사용자의 경우 리눅스가 필요하다. 이를 위해 필요한 것이 하이퍼바이저이고, 윈도우 사용자나 리눅스 사용자가 많이 사용하는 Type 2형 가상상자를 설치한다.

리눅스 사용자의 경우 본인이 사용하는 리눅스에 대한 정확한 정보가 필요하다. 이를 위해 필요한 정보를 다음 명령어를 통해 확인한다.

~~~ {.input}
root@dev-hangul:~# lsb_release -a
~~~

~~~ {.output}
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.2 LTS
Release:        14.04
Codename:       trusty
~~~

`lsb_release -a` 명령어를 통해서 우분투 14.04이고 코드명은 `trusty`다. 

#### 2.2. 가상상자 설치

상기 정보를 바탕으로 버츄얼 박스를 설치한다. `nano /etc/apt/sources.list` 명령어를 통해서 상기 코드명에서 확인한 것과 매칭되는 것을 골라 `/etc/apt/sources.list`에 추가한다. `trusty` 코드명이기 때문에 `deb http://download.virtualbox.org/virtualbox/debian trusty contrib`을 선택한다. 다른 배포판의 자세한 정보는 [askubuntu](http://askubuntu.com/questions/367248/how-to-install-virtualbox-from-command-line)나 [virtualbox.org](https://www.virtualbox.org/wiki/Linux_Downloads)를 참조한다.

보안키를 추가하고 나서 `virtualbox-4.3`을 설치한다.

~~~ {.input}
root@dev-hangul:~# sudo sh -c 'echo "deb http://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" >> /etc/apt/sources.list'

root@dev-hangul:~# wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
root@dev-hangul:~# sudo apt-get update
root@dev-hangul:~# sudo apt-get install virtualbox-4.3
root@dev-hangul:~# sudo apt-get install dkms
root@dev-hangul:~# VBoxManage --version
~~~

~~~ {.output}
4.3.28r100309
~~~

특히, 우분투/데비안 사용자는 `dkms` 팩키지를 설치해서 다음번 `apt-get upgrade`에 리눅스 커널 변경에 맞춰 버추얼박스 커널 모듈 3종 세트(vboxdrv, vboxnetflt, vboxnetadp)가 자동으로 갱신되게 한다. `VBoxManage --version` 명령어로 정상적으로 버츄얼박스가 설치된 것을 확인한다.

**가상상자 `.deb` 팩키지 설치**

가상상자가 오래되어 새로운 버젼이 올라가면, 가상상자를 실행하면 새로운 버젼이 나왔다고 안내가 나오고 다운로드 안내를 한다. 만약 이전 가상상자가 설치되어 있으면 충돌이 나기 때문에 `sudo dpkg -r virtualbox-4.3` 명령어로 제거하고 신규로 설치한다.

~~~ {.shell}
$ sudo dpkg -r virtualbox-4.3
$ wget http://download.virtualbox.org/virtualbox/5.0.4/virtualbox-5.0_5.0.4-102546~Ubuntu~trusty_i386.deb
$ sudo dpkg -i  virtualbox-5.0_5.0.4-102546~Ubuntu~trusty_i386.deb
~~~

> #### 리눅스 팩키지 설치 명령어 비교 {.callout}
>
> `dpkg`는 **수작업**으로 데비안 팩키지 관리 시스템(Debian Package Management System) 기능을 수행했고, 이는 CLI의 경우 `apt-get`, `aptitude`, GUI의 경우 `Synaptic` 혹은 `Software Center`로 진화해 나갔다. 
> 
> - CLI: dpkg &rarr; apt-get, aptitude
> - GUI: dpkg &rarr; Synaptic, Software Center  
>
> dpkg를 통한 팩키지 설치는 `dpkg -i`, 팩키지 삭제는 `dpkg -r` 이다.


#### 2.3. 부랑자(Vagrant) 설치 

부랑자(Vagrant) 가장 최신버젼을 설치한다. 먼저 [부랑자(Vagrant)](https://www.vagrantup.com/) 사이트에 접속해서 [다운로드 사이트](https://www.vagrantup.com/download-archive/v1.7.1.html)로 들어간다. 리눅스 버전을 골라 우클릭하고 `링크주소복사` 해서 `wget` 명령어로 다운로드해서 설치한다.

~~~ {.input}
root@dev-hangul:~# wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.1_x86_64.deb
root@dev-hangul:~# sudo dpkg -i vagrant_1.7.1_x86_64.deb
root@dev-hangul:~# vagrant -v
~~~
~~~ {.output}
Vagrant 1.7.1
~~~

### 3. 가상 컴퓨터 SSH 접속

버츄얼박스에 올라온 가상컴퓨터에 접속하는 알려진 최상의 방법은 [포트 포워딩(Port Forwarding)](http://simple.wikipedia.org/wiki/Port_forwarding)이다. [네트워크 주소 변환(network address translation, NAT)](http://ko.wikipedia.org/wiki/네트워크_주소_변환)은 사설 네트워크에 속한 여러 개의 호스트가 하나의 공인 IP 주소를 사용하여 인터넷에 접속하는데 많이 사용된다. 

`VBoxManage showvminfo` 명령어로 포드번호를 확인한다. `ssh` 포트는 `2222`으로 설정되어 있다.
본인이 가상컴퓨터 이미지를 만든 경우 버츄얼박스 가상컴퓨터에 `ssh` 연결에 대한 자세한 사항은 다음 [웹사이트](http://stackoverflow.com/questions/5906441/how-to-ssh-to-a-virtualbox-guest-externally-through-a-host)를 참조한다.

~~~ {.input}
[xwmooc:~/spark/mooc-setup-master ] $ VBoxManage showvminfo sparkvm | grep 'Rule'
~~~

~~~ {.output}
NIC 1 Rule(0):   name = ssh, protocol = tcp, host ip = 127.0.0.1, host port = 2222, guest ip = , guest port = 22
NIC 1 Rule(1):   name = tcp4040, protocol = tcp, host ip = , host port = 4040, guest ip = , guest port = 4040
NIC 1 Rule(2):   name = tcp8001, protocol = tcp, host ip = , host port = 8001, guest ip = , guest port = 8001
~~~

`ssh -p` 포트번호 `2222`를 통해 사용자 `vagrant`로 로컬컴퓨터에 로그인했다.

~~~ {.input}
[xwmooc:~/spark/mooc-setup-master ] $ ssh -p 2222 vagrant@127.0.0.1
~~~

~~~ {.output}
vagrant@127.0.0.1's password: 
Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.13.0-53-generic i686)

 * Documentation:  https://help.ubuntu.com/
  System information as of Thu Jun 11 04:56:02 UTC 2015

  System load:  0.61              Processes:           77
  Usage of /:   3.3% of 39.34GB   Users logged in:     0
  Memory usage: 4%                IP address for eth0: 10.0.2.15
  Swap usage:   0%

  Graph this data and manage this system at: https://landscape.canonical.com/
  Get cloud support with Ubuntu Advantage Cloud Guest:     http://www.ubuntu.com/business/services/cloud

Last login: Thu Jun 11 04:56:03 2015 from 10.0.2.2
~~~


#### 3.1. `Xen` 하이퍼바이저 오류

`vagrant up`을 실행시킬 때 다음과 같은 오류가 발생한다면, `sudo apt-get update && sudo apt-get dist-upgrade` 명령어로 깔끔한 상태로 다시 설치한다. 그럼에도 불구하고 `vagrant up` 명령어로 실행을 해도 오류가 생긴다. 그래서 `sudo /etc/init.d/vboxdrv setup` 명령어로 재설치를 한다.

~~~ {.output}
VirtualBox is complaining that the kernel module is not loaded. Please run `VBoxManage --version` or open the VirtualBox GUI to see the error message which should contain instructions on how to fix this error.
~~~

~~~ {.input}
root@dev-hangul:~# sudo apt-get update && sudo apt-get dist-upgrade
root@dev-hangul:~# sudo apt-get install build-essential libssl-dev linux-headers-`uname -r`
root@dev-hangul:~# sudo apt-get install dkms
root@dev-hangul:~# sudo /etc/init.d/vboxdrv setup
~~~

자체 컴퓨터가 아닌 클라우드 환경에서 하이퍼바이저를 설치할 경우, **(Running VirtualBox in a Xen environment is not supported)** 메시지가 의미하는 바는 소프트레이어는 `Xen` 하드웨어 가상 컴퓨터(Hardware Virtual Machine)를 사용하고 있다. 그래서 `Xen` 하이퍼바이저 위에 동일한 `Xen` 하이퍼바이저를 사용할 이유가 없다.

~~~ {.output}
Stopping VirtualBox kernel modules ...done.
Uninstalling old VirtualBox DKMS kernel modules ...done.
Trying to register the VirtualBox kernel modules using DKMS ...done.
Starting VirtualBox kernel modules ...failed!
  (Running VirtualBox in a Xen environment is not supported)
~~~


