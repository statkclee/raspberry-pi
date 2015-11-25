---
layout: page
title: xwMOOC 컴퓨터
subtitle: 통계적 사고 가상컴퓨터기반 개발 환경
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 부랑자(Vagrant)를 활용해서 통계적 사고 개발환경을 구축한다.

### 1. 통계적 사고 개발환경 아키텍처

사용자 컴퓨터 운영체제 독립적으로 가상상자(VirtualBox)와 부랑자(Vagrant)를 설치한 후에 `Vagrantfile`에 설정된 내용에 맞춰 과학컴퓨팅(아나콘다)과 LaTeX 기본환경을 설정하고, 공용 디렉토리를 설정해서 모든 작업을 일원화한다.

<img src="fig/think-stat-vagrant.png" width="70%" />

### 2. 통계적 사고관련 툴체인

> ### 가상개발환경 구축 도구 모음 {.getready}
>
>- [Packer](https://www.packer.io/downloads.html)[^1]  
>- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)  
>- [Vagrant](https://www.vagrantup.com/downloads.html)  
>- [Git](https://git-for-windows.github.io/)  
>- [Jenkins](https://jenkins-ci.org/)

[VirtualBox](https://www.virtualbox.org/wiki/Downloads)와 [Vagrant](https://www.vagrantup.com/downloads.html)를 설치한 후에 **Vagrantfile**에 파이썬과 LaTeX 설치 및 환경설정을 담은 정보를 실행한다.

### 3. 통계적 사고 작업 파일

파이썬과 LaTeX 설치 **Vagrantfile**에 공용폴더를 지정하여 그곳에 `git clone`을 통해 [GitHub:한글 통계적 사고](https://github.com/statkclee/ThinkStats2), [GitHub: 영문 ThinkStat2](https://github.com/AllenDowney/ThinkStats2)를 복제하여 작업한다.

[^1]: [Packer](https://www.packer.io/downloads.html)를 윈도우에서 설치하는 경우는 **제어판 &rarr; 시스템 &rarr; 고급 시스템설정 &rarr; 환경변수 &rarr; 시스템변수** 로 들어가서 `경로`에 추가한다.
