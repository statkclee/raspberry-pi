---
layout: page
title: $100 달러 오픈 컴퓨터
subtitle: 한글 LaTeX 문서 환경 가상화
minutes: 10
---

> ### 학습 목표 {.objectives}
>
>  *  한글 LaTeX 문서 작업환경 가상화
>  *  실리콘(하드웨어)에 운영체제를 설치한다.
>  *  운영체제 위에 LaTeX 엔진과 한글 LaTeX 툴체인을 설치한다.
>  *   Git 저장소에 한글 LaTeX 프로젝트를 복제한다.
>  *   LaTeX 문서작업을 하고 최종 산출물을 출력한다.


### 1. LaTeX 테스트 사례 준비

LaTeX 문서 테스트 사례를 먼저 준비하여 한글 LaTeX 문서 작업을 본격 시작하기 전에 준비를 한다.

1. 영문 LaTeX 문서 테스트 사례: 가장 기본이 되는 테스트 사례로 `hello world` 문서를 작성해서 정상적으로 pdf 파일을 산출하는지 점검한다.
1. 영문 LaTeX 문서 다양한 기능 점검 사례: 목차, 색인, 참고문헌 등 기본적인 문서의 기능을 잘 동작하는지 점검한다.
    - 목차(Table of Contents)
    - 그림과 표
    - 색인(makeindex)
    - 참고문헌(bibtex)
1. 한글 LaTeX 문서 테스트 사례: 한글 문서의 가장 기본이 되는 테스트 사례로 `hello world` 문서를 작성해서 정상적으로 한글이 pdf 파일에 찍히는지를 점검한다.
1. 한글 LaTeX 문서 다양한 기능 점검 사례: 목차, 색인, 참고문헌 등 기본적인 문서의 기능을 잘 동작하는지 점검한다. 특히, 유니코드(utf-8)적용에 따른 줄간격, 글자간격 등 차이가 생길 수 있는 부분을 집중적으로 점검한다.
    - 목차(Table of Contents)
    - 그림과 표
    - 색인(makeindex)
    - 참고문헌(bibtex)
1. HTML 산출물 점검: `.pdf`, `.ps`, `.dvi`는 동일한 계열이라 하나가 되면 나머지는 자동으로 될 수 있지만, `.tex` 파일을 **HTML**로 변환하는 것은 전혀 다른 문제로 단일 편집문서(LaTeX)에서 `.pdf`와 `.html`이 생성되도록 점검한다.
    - `hevea.sty`를 저자는 사용했지만 다른 HTML 변환도구도 살펴보기를 권장한다.
    - [Pandoc](http://pandoc.org/)도 많이 사용되는 강력한 HTML문서 변환도구로 간단한 명령어로 HTML 파일을 자동생성한다. 예를 들어, `pandoc -s book.tex --mathjax -o book.html`.
   
   
#### **1.1. 영문 `.tex` 문서가 정상적으로 `.pdf` 파일을 생성하는지 시험한다.**

`pdflatex hello-world.tex` 명령어를 실행하면 `hello-world.pdf` 파일을 생성한다. 물론 `hello-world.aux` , `hello-world.log` 파일로 함께 만들어낸다.

~~~ {.shell}
% hello-world.tex 견본 파일
\documentclass{article}
\begin{document}

Welcome to LaTeX Hello World!
% 한글을 사랑합니다.

\end{document}
~~~

영문은 정상적으로 출력되나 한글은 그렇지 못할 수 있다. 따라서 적절하게 설정이 되었는지 다음 LaTeX 예제를 통해서 확인을 할 필요가 있다.

#### **1.2. 한글 LaTeX 작업을 위해서 사용자 모드로 관련 팩키지를 설치한다.**

~~~ {.shell}
% 한글견본 출처: 김도현, 2004년 동국대 법대, LaTeX으로의 초대 교재에서 발췌.
\documentclass{article}
\usepackage{dhucs}
\begin{document}
\title{첫번째 \LaTeX}
\author{아무개}
\maketitle
\section{들어가며}
나의 첫 \LaTeX\ 파일입니다.%
\footnote{이걸 어떻게 처리할까?}
\section{나오며}
시작하자마자 끝내려니 쑥스럽네요.
\end{document}
~~~


###3. 우분투/데비안 계열 리눅스 LaTeX 설치

#### 3.1. texlive 전체 엔진 설치
LaTeX 전체 엔진 및 전체 팩키지를 설치한다. `sudo apt-get -y install texlive-full`, 
`sudo apt-get -y install  texlive-xetex, texlive-luatex, texlive-lang-cjk` 명령어를 통해서 한글을 처리하도록 관련 팩키지를 설치한다.

~~~ {.shell}
$ sudo apt-get -y install texlive-full
$ sudo apt-get -y install  texlive-xetex, texlive-luatex, texlive-lang-cjk
$ sudo apt-get install xzdec
$ tlmgr --usermode init-usertree
$ tlmgr repository add http://ftp.ktug.org/KTUG/texlive/tlnet ktug
$ sudo tlmgr pinning add ktug "*"
~~~
[KTUG 위키 설치하기Linux/usermode](http://wiki.ktug.org/wiki/wiki.php/설치하기Linux/usermode)

#### 3.2. 통계적 사고(Think Stats2) 의존성 설치

~~~ {.shell}
sudo apt-get -y install hevea
sudo apt-get -y install evince
~~~

**한글 LaTeX 출판을 위한 `Vagrantfile`**

~~~ {.output}
$install_mss = <<INSTALL
sudo apt-get update
#install git
sudo apt-get -y install git

#install C dependencies
sudo apt-get -y install libacl1-dev libgnutls-dev gcc make
#install packaging dependencies
sudo apt-get -i install build-essential fakeroot lintian devscripts debhelper ubuntu-dev-tools cowbuilder
#install LaTeX Full version
sudo apt-get -y install texlive-full
#install Korean LaTeX Dependencies
sudo apt-get -y install collection-kotex
# sudo apt-get -y install  texlive-xetex, texlive-luatex, texlive-lang-cjk
# 
sudo tlmgr update --all --self
tlmgr --usermode init-usertree
# tlmgr repository add http://ftp.ktug.org/KTUG/texlive/tlnet ktug
# tlmgr repository add http://ftp.ktug.or.kr/KTUG/texlive/2014 ktug
sudo tlmgr install collection-kotex
sudo apt-get -y install xzdec
sudo tlmgr pinning add ktug "*"
# Think Stat2 Dependencies - translated from LaTeX to hevea
sudo apt-get -y install hevea
sudo apt-get -y install evince
INSTALL

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty32"
  config.vm.provision "shell", inline: $install_mss
end
~~~

> ### 한글 LaTeX 가상환경 구축 도구 {.getready}
>
>*[Packer](https://www.packer.io/downloads.html)  
>     - Control panel -> System -> Advanced System settings -> Environment Variables -> System variables : PATH  추가 
>*[VirtualBox](https://www.virtualbox.org/wiki/Downloads)  
>*[Vagrant](https://www.vagrantup.com/downloads.html)  
>*[Git](https://git-for-windows.github.io/)


### 4. 실리콘(하드웨어) 위에 운영체제 설치 - 우분투 Packer 설치 [^10]

`packer`를 다운로드한 후에 압축을 풀고 경로를 지정해 주어 어디에서든지 `packer` 명령어를 사용할 수 있는 것이 핵심이다.

1. 임의 명칭 디렉토리 생성한다. `packer`도 좋다.
1. `packer` 디렉토리로 이동한다.
1. `wget` 명령어로 

~~~ {.shell}
$ mkdir packer
$ cd packer
$ wget https://releases.hashicorp.com/packer/0.8.6/packer_0.8.6_linux_amd64.zip
$ sudo unzip packer_0.8.6_linux_amd64.zip
$ nano ~/.bashrc
$ export PATH=$PATH:~/packer/
$ reboot # 혹은 source ~/.bashrc
~~~

### Packer를 사용한 VirtualBox 구축

1. `packer build -only=virtualbox-iso application-server.json` 실행 
1. `cd virtualbox` 실행
1. `vagrant box add ubuntu-14.04.2-server-amd64-appserver_virtualbox.box --name devops-appserver` 실행
1. `vagrant up` 실행
1. `vagrant ssh` 명령어로 VirtualBox 접속

[참고자료:Udacity Intro to DevOps교육과정](https://www.udacity.com/wiki/ud611)

<!-- <img src="fig/latex-overview.png" width="70%" /> -->

[^1]: [Modern LaTeX](http://wiki.ktug.org/wiki/wiki.php/ModernLaTeX)
[^2]: [What is TeX and Metafont all about?](http://www.ntg.nl/maps/11/18.pdf)
[^3]: [공주대학교 LaTeX 워크샵](http://wiki.ktug.org/wiki/wiki.php/LaTeXWorkshop)

[^10]: [우분투 Packer 설치](https://www.digitalocean.com/community/tutorials/how-to-install-and-get-started-with-packer-on-an-ubuntu-12-04-vps)
