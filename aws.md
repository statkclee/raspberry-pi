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


#### 1.4. 정적 웹 사이트 배포

<img src="fig/aws-route53-cloudfront-s3-architecture.png" width="70%" />

- **S3 버킷**: `index.html` 파일을 포함한 정적 웹사이트 서비스를 위한 원데이터를 업로드한다.
    - 권한(Permissions): `Add bucket policy`를 클릭하고 기본 정책을 저장한다.
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

[참조: Static Sites using AWS S3, CloudFront, and Route 53](https://sysadmincasts.com/)

S3 버킷에 정적 웹사이트를 자동으로 넣는 방법
[참고: GitHub Manage an S3 website](https://github.com/laurilehmijoki/s3_website)
[참고: Setting up AWS credentials](https://github.com/laurilehmijoki/s3_website/blob/master/additional-docs/setting-up-aws-credentials.md)


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
