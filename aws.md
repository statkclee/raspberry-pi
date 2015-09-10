---
layout: page
title: 아마존 웹서비스
subtitle: EC2 
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 아마존 웹 서비스
> * 정적 웹사이트 구축
> * GitHub 개발환경 구축


### 1. 윈도우에서 아마존 웹서비스 개발환경 구축

#### 1.1. 가상상자 (버츄얼박스, VirtualBox)

X86 중앙처리장치가 올라간 개인용 하드웨어 컴퓨터에 윈도우 운영체제가 주인 운영체제(Host Operating Syste)가 일반적으로 설치된다. 하지만, 개인용 PC 운영체제로 우분투 리눅스를 설치하려고 하면 과거에는 윈도우를 삭제하고 설치해야 됐다. 하지만, [가상상자](https://ko.wikipedia.org/wiki/버추얼박스) 같은 가상화 소프트웨어를 설치하면 윈도우 상태에서 우분투 리눅스를 사용할 수도 있다. 반대로 맥이나 리눅스를 사용한 경우에도 가상화 소프트웨어를 설치하고 윈도를 응용프로그램처럼 사용하는 것도 많이 사용된다.

<img src="fig/aws-virtualbox-architecture.png" width="50%" />


1. 우분투 14.04 설치 이미지를 다운로드한다. [Ubuntu Server 14.04.3 LTS 다운로드](http://www.ubuntu.com/download/server)
1. 가상상자를 다운로드 한다. [가상상자 다운로드](https://www.virtualbox.org/wiki/Downloads)
1. 가상상자에 다운로드 받은 우분투 14.04 버젼을 설치한다.
    - 가상상자를 실행하고 `새로 만들기(N)`를 클릭한다.
    - 가상상자 명칭을 `ubuntu`로 정하고 기본설정값을 따라 설정을 완료하면 `ubuntu` 전원 꺼짐 상태로 가상상자 하나가 생성된다.    
1. `ubuntu` 가상상자를 우클릭 `설정`으로 들어가고 대화상자에서 `어댑터 1` `브리지 어댑터`를 선택하고 저장한다.
1. 다시 `ubuntu` 가상상자를 우클릭하고 `시작(T)`를 눌러 다운로드 받은 우분투 이미지를 선택한다.
1. 일반 컴퓨터에 우분투를 설치하는 기분으로 쭉 설치한다.
    - `root` 사용자 대신 기본 사용자를 정하게 된다. 예를 들어 `xwmooc` 등 임의 사용자를 생성하고, 추후 `ssh` 로그인에 사용한다.


#### 1.2. 가상상자 접속하기

1. 터미널을 실행하고, `sudo apt-get install openssh-server` 명령어로 ssh 로그인 가능케 소프트웨어를 설치한다.
1. 가상상자 우분투 터미널을 실행하고 `ifconfig` 명령어로 IP주소를 확인한다. 통상 **10.0.2.15** 가 된다.
1. `ssh xwmooc@10.0.2.15`와 유사한 명령어로 가상상자에 접속한다.

~~~ {.shell}
$ ssh xwmooc@192.168.0.11
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


#### 1.2. 부랑자(Vagrant) 설치

[부랑자(Vagrant)](https://www.vagrantup.com/)는 가상 개발 환경을 생성하고 환경설정을 가능케하는 소프트웨어로, 초기에는 [버츄얼 박스](https://www.virtualbox.org/)만 지원했으나, 1.1버젼 이후에는 VMWare, KVM, LXC(리눅스 컨테이너), 다양한 형상관리 소프트웨어와 함께 사용할 수 있고, 특히 1.6버젼 이후 도커 컨테이너를 지원한다.

[부랑자 다운로드](https://www.vagrantup.com/downloads.html) 웹사이트에서 소프트웨어는 다운로드 받으면 된다. 

> #### 다양한 부랑자 공개 박스 {.callout}
>
> [Hashicorp Atlas](https://atlas.hashicorp.com/boxes/search)
> [Vagrantbox.es](http://www.vagrantbox.es/)

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

##### 1.2.1. 파이썬 소프트웨어 카펜트리 

[소프트웨어 카펜트리 부랑자 환경설정](https://github.com/cfriedline/vagrant-swc) 사이트에서 `git clone` 명령어로 복제한다.

- 가상상자와 부랑자를 설치한다.
- [Software Carpentry Vagrant](https://github.com/cfriedline/vagrant-swc) 환경파일을 복제한다.
- 복제한 디렉토리로 변경한다.
- `vagrant up` 실행한다.
- `vagrant ssh`를 통해 배쉬쉘 접속한다.

##### 1.2.2. 빅데이터 스파크(Spark)


### 2. 아마존 웹 서비스를 활용한 정적 웹 서비스 

#### 2.1. S3를 활용한 정적 웹 서비스 구축 

<img src="fig/aws-s3-website.png" width="50%" />

- **S3 버킷**: `index.html` 파일을 포함한 정적 웹사이트 서비스를 위한 원데이터를 업로드한다.
    - 권한(Permissions): `Add bucket policy`를 클릭하고 기본 정책을 저장한다.
        - S3 버킷 정책에 대한 자주 사용하는 유형을 아마존 웹 서비스에서 잡아놔서 그중 적합한 것을 골라 사용한다. [참조: 아마존 웹 서비스 버킷 정책 예제](http://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/example-bucket-policies.html)
    - 정적 웹사이트 호스팅(Static Website Hosting): `Enable website hosting`에 `index.html` 파일을 추가한다.

~~~ {.input}
{
  "Version":"2012-10-17",
  "Statement":[{
  "Sid":"PublicReadGetObject",
        "Effect":"Allow",
    "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::example-bucket/*"
      ]
    }
  ]
}
~~~
<img src="fig/aws-s3-bucket-website.png" width="40%" />


#### 2.2. 사용자 지정 도메인으로 정적 웹서비스로 개발된 S3에 정적 웹 사이트 설정

사용자 구매한 지정 도메인으로 정적 웹서비스로 개발된 S3에 정적 웹 사이트 설정하기 위해서 다음 절차를 거친다.

1. 도메인 등록, 만약 도메인이 없다면 다양한 제공업체를 통해서 구입한다.
1. S3 버킷 생성과 개발된 정적 웹서비스를 S3 버킷에 올린다.
1. 아마존 라우트53 호스팅 영역 생성하고 환경설정한다.
1. DNS 서비스를 제공하는 아마존 라우트53으로 설정한다.

<img src="fig/aws-route53-s3-static-website.png" width="40%" />

라우트53 &rarr; `호스트 존(Hosted Zones)` 에서 해당 도메인을 선택하고 `Go to Record Sets` &rarr; `Create Record Set`에서 도메인 명칭과 S3 버킷 설정된 것을 연결한다.

S3 버킷 명칭을 `rur-ple.xwmooc.org` 으로 설정했으면, `Name`은 `rur-ple`, `Type`은 `A - IPv4 address`, `Alias:`는 `Yes`를 선택하고, `Alias Target:`은 S3 버킷 명칭을 선택하거나, 복사해서 넣는다.

<img src="fig/aws-route53-rur-ple-configuration.png" width="40%" />

[참고: 사용자 지정 도메인으로 정적 웹 사이트 설정](http://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)

### 1. 아마존 웹 서비스


#### 1.1. 아마존 웹 서비스 비용 관리

[AWS 간편 월별 요금 계산기](http://calculator.s3.amazonaws.com/index.html)


#### 1.2. 정적 웹 서비스 아키텍쳐

<img src="fig/aws-route53-cloudfront-s3-github-jekyll-architecture.png" width="100%" />

아마존 웹 서비스를 이용한 정적 웹 사이트 구축 구성요소는 다음과 같다.
- **제킬**: 
- **GitHub**:
- **S3 버킷**:
- **클라우드 프론트(CloudFront)**:
- **라우트 53**:

#### 1.3. 정적 웹 사이트 개발




### 1. S3와 클라우드프론트(Cloudfront) 연동

정적 웹 서비스를 개발해서 S3에 저장하고 이를 클라우드프론트(CloudFront)를 통해 배포하는 방식은 다음과 같다.

<img src="fig/aws-s3-cloudfront-website.png" width="100%" />

1. S3 버킷에 개발된 정적 웹서비스를 업로드 합니다.
1. 클라우드프론트 배포 서비스로 가서 Web(웹), RTMP(동영상) 중 웹을 선택하고 설정을 합니다.
    - `Origin Settings`에 정적 웹 서비스를 올린 S3 버킷을 선택합니다.
1. 배포가 완료되면 `Domain Name`에 `http://dsssmxxsjebsd.cloudfront.net/` 와 같이 생성된 것을 확인한다.
1. (크롬)웹 브라우져로 접속해서 단축키 F12 혹은 메뉴 &rarr; 도구(L) &rarr; 개발자 도구(D) 를 통해 *개발자 도구*를 실행하고 `Network`에서 `Header` 패널에서 `X-cache: Hit from cloudfront`를 확인한다.

### 1. EC2 란?

아마존 웹서비스 EC2는 가상 컴퓨터로 생각하면 된다.

### 2. 접속하기

아마존 EC2 컴퓨터에 접속할 때는 **아이디/비밀번호**가 디폴트 기본설정된 것이 아니고 **공개키/비밀키** 접속방법이 기본으로 설정된다. 

1. EC2 생성할 때 키를 생성한다.
1. EC2 생성할 때 다운로드한 키(.pem)를 소중히 간직한다.
1. EC2에 `ssh` 명령어로 로그인한다.

~~~ {.shell} 
$ ssh -i xwmooc-shell.pem ubuntu@ec2-54-52-365-32.ap-northeast-1.compute.amazonaws.com
~~~
여기서 `xwmooc-shell.pem` 파일은 EC2 컴퓨터가 처음 생성될 때 만들어진다. 아마존 컴퓨터 이미지(Amazon Machine Image, AMI)인 경우 사용자명은 `ubuntu` 대신에 `ec2-user`가 되니 생성한 EC2 이미지에 따른 기본 로그인 사용자명을 확인하기 바란다. `@` 기호 다음에 넣어 `ec2-54-52-365-32.ap-northeast-1.compute.amazonaws.com` 혹은 `54.166.118.14` 같은 IP주소로 정확한 EC2 컴퓨터를 지정한다.


### 3. Elastic IP 변경

공개형 IP (Public IP)를 IP 주소에 연계한다.


### 4. 웹 콘텐츠 올리기

웹서비스 콘텐츠 올리는 권한 부여.

~~~ {.shell}
$  chown -R ubuntu /var/www/
~~~



### 1.4. 정적 웹 사이트 배포

<img src="fig/aws-route53-cloudfront-s3-architecture.png" width="70%" />


[참조: Static Sites using AWS S3, CloudFront, and Route 53](https://sysadmincasts.com/)

S3 버킷에 정적 웹사이트를 자동으로 넣는 방법
- [참고: GitHub Manage an S3 website](https://github.com/laurilehmijoki/s3_website)
- [참고: Setting up AWS credentials](https://github.com/laurilehmijoki/s3_website/blob/master/additional-docs/setting-up-aws-credentials.md)
