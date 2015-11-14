---
layout: page
title: xwMOOC 오픈 컴퓨터
subtitle: 우분투/데비안 계열 한글 LaTeX
minutes: 10
---

> ### 학습 목표 {.objectives}
>
>  *  우분투/데비안 계열 LaTeX 환경에서 설치한다.

### 1. LaTeX 설치

`texlive-full`만 설치하면 시간이 오래걸리고 용량을 많이 차지해서 그렇지만 기타 부수적인 설정을 할 필요는 없다. 다만 이미지 관련된 작업과 변환작업이 일부 있을 수 있어 `ghostscript`와 `imagemagick`을 추가로 설치한다.

~~~
# LaTeX 설치
$ apt-get install -y --no-install-recommends \
		ghostscript \
		imagemagick \
		texlive-full \
~~~

> ### 한글 LaTeX 작업과 연관된 팩키지 {.callout}
> 
> 한글을 LaTeX에서 구현하기 위해서는 texlive-xetex, texlive-luatex, texlive-lang-cjk 가 필요하다.
> 좀더 자세한 사항은 [KTUG 위키](http://wiki.ktug.org/wiki/wiki.php/설치하기Linux/usermode)를 참조한다.

~~~
# 한글 관련 팩키지 LaTeX 설치
$ apt-get install -y texlive-xetex texlive-luatex texlive-lang-cjk
~~~


#### 1.1. 한글 LaTeX 문서 생성

LaTeX 문서 컴파일은 다음 명령어를 통해서 실행한다. `pdflatex HelloWorld.tex` 명령어를 실행하면 pdf 파일이 생성된다.

~~~ {.input}
% 한글 샘플 HelloWorld.tex 예제 
\documentclass{article}
\usepackage[hangul]{kotex}
\title{한글과 English!}
\author{xwMOOC 한글 지킴이}
\date{September 2015}
\begin{document}
   정말 잘 되나요???
   Hello world! 한글이 없어요...
\end{document}
~~~

~~~
$ pdflatex HelloWorld.tex
~~~

> #### `LaTeX Error: 'biblatex.sty' not found` 오류 해결 {.callout}
> `texlive-full`을 사용하지 않고 필요한 것만 설치하는 경우 종종 다음과 같은 오류가 난다. 
> 이런 경우 당황하지 말고 해당하는 팩키지를 찾아 설치하면 된다.
> 
> ~~~
> $ sudo apt-get install texlive-bibtex-extra
> ~~~

참조: [http://tex.stackexchange.com/questions/122559/unicode-math-and-tex4ht-with-utf-8-input](http://tex.stackexchange.com/questions/122559/unicode-math-and-tex4ht-with-utf-8-input)

<img src="fig/latex-hangul-example.png" width="70%" />

#### 1.2. 참고문헌 LaTeX 팩키지 설치

한글 LaTeX 개발에 참고문헌 기능을 사용할 경우 `texlive-bibtex-extra` 팩키지를 꼭 설치한다.

~~~ {.error}
! LaTeX Error: File `biblatex.sty' not found.
~~~

~~~ {.bash}
$ sudo apt-get install texlive-bibtex-extra 
~~~
 
#### 1.3. 한글 LaTeX 팩키지 설치

한글 LaTeX 팩키지 설치가 되어 있지 않다고 오류가 나면 `sudo apt-get install ko.tex` 명령어를 통해서 한글 LaTeX 팩키지를 설치하면 한글을 사용할 수 있다.

~~~ {.error}
! LaTeX Error: File `kotex.sty' not found.
~~~

~~~ {.bash}
$ sudo apt-get install ko.tex
~~~

참고: [우분투에서 한글 Tex 환경 설치와 에디터 소개](http://slayer95.tistory.com/28)

### 2. 한글 LaTeX 편집기([texworks](https://www.tug.org/texworks/))

LaTeX 문서를 개발을 도와주는 개발환경은 많이 있지만, 실행결과를 바로 확인해 줄 수 있는 `texworks`도 많이 사용되는 개발환경도구 중 하나다.

~~~ {.bash}
$ sudo apt-get install texworks
~~~




### 한글 LaTeX 설정 전체 스크립트

클라우드 가상컴퓨터 우분투 (14.04 기준)에서 한글 LaTeX 작업을 위한 설정 스크립트. 

~~~ {.input}
# 파일명: install-utf-8.sh
# 언어 로케일 설정
apt-get update
apt-get -y upgrade
apt-get install -y language-pack-ko
locale-gen ko_KR.UTF-8

# /etc/profile 파일 하단에 추가 내용
echo "LANG=ko_KR.UTF-8
LANGUAGE=ko_KR.UTF-8
LC_ALL=ko_KR.UTF-8"  >> /etc/profile

# 로컬 시간대 변경 혹은  dpkg-reconfigure tzdata
ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# 한글 입력기 설치
sudo apt-get install -y ibus ibus-hangul

# 한글 폰트 설치
apt-get install -y fonts-nanum fonts-nanum-coding fonts-nanum-extra  fonts-unfonts-core  fonts-baekmuk fonts-nanum-eco fonts-unfonts-extra xfonts-baekmuk 

# LaTeX 편집기 설치
sudo apt-get install -y texworks

# 범용편집기 Sublime Text 2 설치
sudo add-apt-repository -y ppa:webupd8team/sublime-text-2
sudo apt-get install -y sublime-text

# 데스트톱 GUI 설치
sudo apt-get install -y xfce4

# 원격 데스트톱 연결 프로그램 설치 및 설정
adduser --disabled-password --gecos "" xwmooc
echo xwmooc:xwmooc | chpasswd
sudo adduser xwmooc sudo

sudo apt-get install -y xrdp
echo "xfce4-session" > /home/xwmooc/.xsession
sudo service xrdp restart

# LaTeX 설치
apt-get install -y --no-install-recommends \
		ghostscript \
		imagemagick \
		lmodern \
		texlive-full \
		texinfo \
~~~




