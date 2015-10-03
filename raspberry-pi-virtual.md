---
layout: page
title: xwMOOC 컴퓨터
subtitle: 라즈베리 파이 가상화 환경
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> *  라즈베리 파이 가상화 환경에 대해 이해한다.

<img src="fig/raspberry-pi-virtualization-stack.png" width="77%" alt="가상화 툴체인" />

### 1. 라즈비언 가상화 설치

라즈베리 파이 하드웨어가 아닌 노트북이나 개인용 컴퓨터에 가상상자와 부랑자를 사용해서 라즈비언을 설치하는 것이 필요한 이유가 있다. 라즈베리 파이 하드웨어에서 리눅스 커널을 컴파일 작업을 할 경우 상대적으로 부족한 컴퓨팅 자원으로 인해서 시간이 매우 많이 소요되고 관심있는 실험을 추진하는 것이 비용과 시간이 많이 들 수 있다. 

가상컴퓨터에 라즈비언 운영체제를 설치하고 간단한 실험을 마친 후에 라즈베리 파이 하드웨어에 최종 작업 결과물을 넣는 것도 한가지 좋은 대안이 될 수 있다. 

<img src="fig/raspberry-pi-virtualization-raspbian.png" width="77%" alt="가상화 툴체인" />

#### 1.1. GEMU 에뮬레이터 사용 라즈비언 설치

[참고: Raspberry Pi Emulation for Windows with QEMU](http://www.pcsteps.com/1199-raspberry-pi-emulation-for-windows-qemu/)

#### 1.2. 가상상자에 라즈비언 설치 (2013년 01월) 

1. 라즈베리 파이 가상상자 `.ova` 파일을 찾는다.
    - [utorrent](http://www.utorrent.com/) 같은 P2P 다운로드 프로그램이 필요할 수 있다.
    - [토렌트 다운로드](http://ediy.com.my/index.php/blog/item/52-virtualbox-raspberry-pi-emulator) 파일 참조
    - 엘리먼트14 [RaspberryPi-Development-VM-v0.8.ova](
http://downloads.element14.com/downloads/RaspberryPi-Development-VM-v0.8.ova?COM=RaspberryPi) 파일을 다운로드한다.
1. `File` &rarr; `Import Appliance` 명령어로 다운로드 받은 `.ova` 이미지를 가져온다.
    - 토렌트에서 받은 것은 라즈비언 이미지 보다는 오래된 리눅스 이미지로 보면 된다.
    - 엘리먼트14 `.ova` 파일은 거의 9 GB로 크다. 
    -  

> #### "No space left on device" 오류 발생 문제해결 {.callout}
>
> 중상: USB, 마이크로SD 카드에 4GB 이상 되는 단일 파일을 저장할 경우 저장공간이 충분이 있음에도 불구하고 저장이 되지 않음, `RaspberryPi-Development-VM-v0.8.ova` 파일의 경우 8.2GB 크기를 갖는 `.ova` 파일을 마이크로SD카드에 복사하거나 저장할 때 오류가 발생.  
> 원인: FAT32 파일형식에서는 단일 파일 크기가 최대 4GB만 저장가능함.  
> 해결 방법: **NTFS, exFAT 파일형식**으로 포맷하고 복사하거나 다운로드 받는다.  

- [참고: Virtualbox Raspberry Pi Emulator](http://ediy.com.my/index.php/blog/item/52-virtualbox-raspberry-pi-emulator)
- [참고: Raspberry Pi Virtual Appliance on OS X](https://thecustomizewindows.com/2015/03/raspberry-pi-virtual-appliance-emulation-on-os-x/)

#### 1.3. Adafruit 라즈베리 파이 Kernel-o-Matic 

[Raspberry Pi Kernel-o-Matic](https://github.com/adafruit/Adafruit-Pi-Kernel-o-Matic)을 사용해서 맞춤형 커널을 신속하게 생성할 수 있다.

1. 의존성 설치
1. 가상상자 시작
1. 커널 만들기
1. 커널 라즈베리 파이 설치

[참고: Raspberry Pi Kernel-o-Matic](https://learn.adafruit.com/raspberry-pi-kernel-o-matic)