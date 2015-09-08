---
layout: page
title: 라즈베리 파이
subtitle: 아치 리눅스
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> *  아치 리눅스 

### 1. 아치 리눅스란?

아치 리눅스 개발팀은 사용자 관점보다는 개발자 관점에서 간결함에 중점을 두며, 우아함, 코드 정확성 및 최소주의를 추구한다. 아치 리눅스는 자체 꾸러미 관리자인 팩맨(pacman)을 사용해 꾸러미를 설치·제거·갱신한다. 롤링 릴리스 모델을 사용하므로 최신 소프트웨어를 설치하려면 시스템 갱신만 하면 된다. 출처: [위키피디아: 아치 리눅스](https://ko.wikipedia.org/wiki/아치_리눅스)

#### 1.1. 팩맨(Pacman)

팩맨(pacman)은 주기적으로 쉽게 관리하기 위해 저드 비넷이 개발한 아치 리눅스의 패키지 관리자로, 팩키지 설치·제거·갱신·다운그레이드를 다루며 의존성을 자동으로 해결해 준다. 명령라인 인터페이스(CLI)만 현재 제공하고 있다.

팩맨 팩키지 갱신 명령어는 `pacman -Syu`이다.

~~~ {.shell}
$ pacman -Syu
~~~

### 2. 아치 리눅스 라즈베리 파이 설치

라즈베리 파이 2에 채택된 브로드콤(Broadcom BCM2836) SoC는 ARMv7 Cortex-A7 쿼드코어를 사용한다. 

반면에 라즈베리 파이에는 브로드콤(Broadcom BCM2835) SoC가 채택되었고, ARM11 코어가 사용된다.

- [Raspberry Pi 2: 아치리눅스 | ARM 7](http://archlinuxarm.org/platforms/armv7/broadcom/raspberry-pi-2)
- [설치 동영상 : Install Arch Linux on a Raspberry Pi 2](https://www.youtube.com/watch?v=OaJjk2NcSM8)