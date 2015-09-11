---
layout: page
title: 아마존 웹서비스
subtitle: EC2 
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 아마존 웹 서비스


### 1. 아마존 웹 서비스


#### 1.1. 아마존 웹 서비스 비용 관리

[AWS 간편 월별 요금 계산기](http://calculator.s3.amazonaws.com/index.html)



### 2. EC2 란?

아마존 웹서비스 EC2는 가상 컴퓨터로 생각하면 된다.

#### 2.1. 접속하기

아마존 EC2 컴퓨터에 접속할 때는 **아이디/비밀번호**가 디폴트 기본설정된 것이 아니고 **공개키/비밀키** 접속방법이 기본으로 설정된다. 

1. EC2 생성할 때 키를 생성한다.
1. EC2 생성할 때 다운로드한 키(.pem)를 소중히 간직한다.
1. EC2에 `ssh` 명령어로 로그인한다.

~~~ {.shell} 
$ ssh -i xwmooc-shell.pem ubuntu@ec2-54-52-365-32.ap-northeast-1.compute.amazonaws.com
~~~
여기서 `xwmooc-shell.pem` 파일은 EC2 컴퓨터가 처음 생성될 때 만들어진다. 아마존 컴퓨터 이미지(Amazon Machine Image, AMI)인 경우 사용자명은 `ubuntu` 대신에 `ec2-user`가 되니 생성한 EC2 이미지에 따른 기본 로그인 사용자명을 확인하기 바란다. `@` 기호 다음에 넣어 `ec2-54-52-365-32.ap-northeast-1.compute.amazonaws.com` 혹은 `54.166.118.14` 같은 IP주소로 정확한 EC2 컴퓨터를 지정한다.


