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


### Packer를 사용한 VirtualBox 구축

1. `packer build -only=virtualbox-iso application-server.json` 실행 
1. `cd virtualbox` 실행
1. `vagrant box add ubuntu-14.04.2-server-amd64-appserver_virtualbox.box --name devops-appserver` 실행
1. `vagrant up` 실행
1. `vagrant ssh` 명령어로 VirtualBox 접속

[참고자료:Udacity Intro to DevOps교육과정](https://www.udacity.com/wiki/ud611)

<!-- <img src="fig/latex-overview.png" width="70%" /> -->
