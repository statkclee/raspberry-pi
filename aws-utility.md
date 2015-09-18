---
layout: page
title: 아마존 웹서비스
subtitle: AWS 유틸리티
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> *  AWS 유틸리티


### EC2 FTP 연결


1. [PuTTYgen 다운로드](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)한다.
    - installer를 설치하면 필요한 모든 것을 자동 설치한다.
    - [참고: PuTTY를 사용하여 Windows에서 Linux 인스턴스에 연결](http://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/putty.html)
1. `.pem` 파일을 `.ppk` 형식으로 변환한다.
    - 시작 &rarr; [모든 프로그램] &rarr; [PuTTY] &rarr; [PuTTYgen] 클릭한다.


[No supported authentication methods available (server sent public key](http://askubuntu.com/questions/204400/ssh-public-key-no-supported-authentication-methods-available-server-sent-publ) 오류가 발생해서 WinSCP를 통해서 EC2 인스턴스에 접근할 수 없는 경우는 EC2 인스턴스에 공개키가 등록이 되지 않는 것이 원인이다. 이를 해결하기 위해서 `~.ssh/authorized_keys`에 `.pem`에서 `.ppk` 파일 생성하면서 공개키를 함께 생성하고 이를 열어 내용을 복사해서 `~.ssh/authorized_keys` 하단에 붙여넣는다.

