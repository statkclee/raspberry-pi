---
layout: page
title: 컴퓨터적 사고 함양을 위한 라즈베리 파이
subtitle: NOOBS 운영체제 관리자
minutes: 10
---
> ## 학습 목표
>
> *   라즈베리 파이 운영체제 관리자 : NOOBS

## NOOBS

**NOOBS(New Out Of the Box Software)** - 라즈베리 파이를 위한 쉬운 운영체제 설치 관리자다.

![NOOBS](fig/noobs.png)

## NOOBS 얻는 방법

### 사전 설치된 SD 카드를 구매

NOOBS를 습득하는 가장 쉬운 방법은 NOOBS가 사전 설치된 SD 카드를 구매하는 것이다: [swag 상점](http://swag.raspberrypi.org/collections/frontpage/products/noobs-8gb-sd-card)에서 4 파운드에 구입가능하다.

### 다운로드

대안으로 라즈베리 파이 웹사이트에서 무료로 NOOBS를 다운로드할 수 있다:  

[http://www.raspberrypi.org/downloads](http://www.raspberrypi.org/downloads)

### SD 카드에 NOOBS 설치하는 방법

NOOBS 압축 파일을 다운로드하면, 사용자 컴퓨터에 있는 포맷된 SD 카드에 다운로드 받은 것을 복사한다. 

빈 SD카드에 NOOBS을 설치하는 방법은 다음과 같다:

- 4GB 이상 되는 SD카드를 FAT 방식으로 포맷한다. 자세한 방법은 아래를 참조한다.  
- 다운로드한 NOOPS 압축파일을 푼다.
- 방금 포맷한 SD 카드에 압축을 푼 파일을 복사한다. 복사한 파일은 SD 카드 루트 디렉토리에 위치시킨다. 몇몇 경우에 압축을 풀 파일을 폴더에 복사하거나 폴더에 압축을 풀기도 한다; 만약 이런 경우라면 폴더 자체보다 폴더 내부에서 파일을 복사해서 루트로 이동시킨다.
- 첫번째 부팅에서 "RECOVERY" FTA 파티션이 자동으로 최소 화면으로 조정하고 설치 가능한 OS 목록이 화면에 표시된다.  

#### FAT 형식으로 SD 카드를 포맷하는 방법

**주의:** 32 GB 이상(즉, 64GB 혹은 그 이상) 저장 용량을 갖는 SD 카드를 포맷한다면, 별도 [SDXC 포맷](https://www.raspberrypi.org/documentation/installation/sdxc_formatting.md) 지침을 참조한다.

#### 윈도우

윈도우 사용자에 대해서 SD 연합회(SD Association) 포맷 도구를 사용해서 SD 카드를 포맷하는 것을 추천한다. 포맷 도구는 [sdcard.org](https://www.sdcard.org/downloads/formatter_4/)에서 다운받을 수 있다.옵션(`Options`)메뉴에서 "FORMAT SIZE ADJUSTMENT" 옵션을 "ON"으로 설정해서 단일 파티션만 포맷하는 것이 아니라 전체 SD 카드 볼륨이 포맷되게 한다.

#### 맥 OS

OSX 디스크 유틸리티가 전체 디스크를 포맷할 수 있지만, 
[SD 연합회 포맷 도구](https://www.sdcard.org/downloads/formatter_4/)도 맥사용자에게 사용가능한다. 포맷을 하기 위해서, SD 카드 볼륨을 고르고 나서, `MS-DOS` 포맷을 갖는 `Erase`를 선택한다.

#### 리눅스

리눅스 사용자에게는 `gparted`를 추천한다. (혹은, 명령-라인 버젼인 parted) Norman Dunbar가 리눅스 사용자를 위한 [포맷방법](http://qdosmsq.dunbar-it.co.uk/blog/2013/06/noobs-for-raspberry-pi/)을 자세히 작성했다.

### NOOBS 내부에는 무엇이 있을까?

NOOBS에는 다음 운영체제가 내장되어 있다.

- [Raspbian](http://raspbian.org/)
- [Pidora](http://pidora.ca/)
- [OpenELEC](http://wiki.openelec.tv/index.php?title=Raspberry_Pi_FAQ)
- [OSMC](http://osmc.tv/)
- [RISC OS](https://www.riscosopen.org/wiki/documentation/show/Welcome%20to%20RISC%20OS%20Pi)
- [Arch Linux](http://archlinuxarm.org/platforms/armv6/raspberry-pi)

NOOBS v1.3.10(2014년 9월) 버젼에는 라즈비언만 디폴트로 설치되어 있다. 다른 운영체제는 네트워크 연결을 통해서 설치될 수 있다.

### NOOBS 와 NOOBS Lite

NOOBS는 두가지 형태로 이용가능하다: 오프라인과 네트워크 설치; 혹은 네트워크 설치 전용.

전체 버젼에는 라즈비언이 포함되어 있어서 오프라인 상태에서 SD 카드로 설치될 수 있다. 반면에 NOOBS Lite를 사용하거나 다른 운영체제를 설치하려면 설치 중에 인터넷 연결이 요구된다.

만약 새로운 버젼의 운영체제가 출시되면 전체 버젼 운영체제는 구식이 될 수 있다. 하지만, 만약 인터넷에 연결이 되고, 만약 최신 운영체제가 이용가능하다면 가장 최신 버전 운영체제 다운로드 옵션이 나타날 것이다.

### NOOBS 개발

#### 최신 NOOBS 출시

가장 최신 NOOBS 버젼은 **2015년 2월 18일** 출시된 **v1.4.0**이다.

(NOOBS v1.4.0 이후로, NOOBS Lite는 단지 버젼 숫자 첫 두 자리만 공유한다. 즉, v1.4)

#### NOOBS 문서

NOOBS 고급 환경설정을 포함한 전체 문서는 [GitHub](https://github.com/raspberrypi/noobs/blob/master/README.md)에서 이용가능한다.

#### NOOBS 소스 코드

NOOBS 소스 코드도 [GitHub](https://github.com/raspberrypi/noobs)에서 볼 수 있다.

