---
layout: page
title: $100 달러 오픈 컴퓨터
subtitle: 한글 LaTeX 문서 환경 가상화
minutes: 10
---

> ### 학습 목표 {.objectives}
>
>  *  한글 LaTeX 문서 작업환경 가상화

> ### 한글 LaTeX 가상환경 구축 도구 {.getready}
>
>*[Packer](https://www.packer.io/downloads.html)  
>     - Control panel -> System -> Advanced System settings -> Environment Variables -> System variables : PATH  추가 
>*[VirtualBox](https://www.virtualbox.org/wiki/Downloads)  
>*[Vagrant](https://www.vagrantup.com/downloads.html)  
>*[Git](https://git-for-windows.github.io/)

#### 우분투 Packer 설치 [^1]

`packer`를 다운로드한 후에 압축을 풀고 경로를 지정해 주어 어디에서든지 `packer` 명령어를 사용할 수 있는 것이 핵심이다.

1. 임의 명칭 디렉토리 생성한다. `packer`도 좋다.
1. `packer` 디렉토리로 이동한다.
1. `wget` 명령어로 

~~~ {.shell}
$ mkdir packer
$ cd packer
$ wget https://releases.hashicorp.com/packer/0.8.6/packer_0.8.6_linux_amd64.zip
$ sudo unzip packer_0.8.6_linux_amd64.zip
$ nano ~/.bashrc
$ export PATH=$PATH:~/packer/
$ reboot # 혹은 source ~/.bashrc
~~~

### Packer를 사용한 VirtualBox 구축

1. `packer build -only=virtualbox-iso application-server.json` 실행 
1. `cd virtualbox` 실행
1. `vagrant box add ubuntu-14.04.2-server-amd64-appserver_virtualbox.box --name devops-appserver` 실행
1. `vagrant up` 실행
1. `vagrant ssh` 명령어로 VirtualBox 접속

[참고자료:Udacity Intro to DevOps교육과정](https://www.udacity.com/wiki/ud611)

<!-- <img src="fig/latex-overview.png" width="70%" /> -->

[^1]: [우분투 Packer 설치](https://www.digitalocean.com/community/tutorials/how-to-install-and-get-started-with-packer-on-an-ubuntu-12-04-vps)
