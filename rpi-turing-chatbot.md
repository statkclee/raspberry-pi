---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 채팅로봇 만들기
---

> ## 학습 목표 {.objectives}
>
> * 라즈베리파이 컴퓨터의 입출력 장치를 식별하고 활용한다.
> * 라즈베리파이에 채팅로봇 프로그램에 코드를 추가해서 텍스트가 큰 소리로 읽혀지게 한다.
> * 지금까지 생성한 채팅로봇 프로그램을 검증하고 평가한다.


### 들어가며

이번 학습을 통해 학생들에게 화면에 대화를 출력하는 채팅로봇 프로그램을 생성하고,
로봇이 질문하는 것을 듣고 로봇이 대화를 하게 변환한다. 

`espeak` 프로그램을 다운로드해서 라즈비언 운영체제가 장착된 SD카드에 설치한다.

~~~ {.shell}
sudo apt-get install espeak
~~~

로봇의 소리를 들을 수 있도록 헤드폰이 필요하고, 경우에 따라서는 전체 학급에서 소리를 들을 수 있도록 
스피커가 필요할 수도 있다.

마지막으로, `amixer cset numid=3 1` 명령어를 타이핑해서 HDMI가 아니고 헤드폰으로 소리가 강제로 내보낼 수 있도록 조치한다. 
혹은 파이썬 게임 아이콘을 더블 클릭하고 *Force Headphones** 를 선택한다. 

### 시작 

책상위에 다음 자재들을 연결되지 않은 상태로 놓아둔다:

* 라즈베리파이
* 스피커
* 헤드폰
* 파이카메라 (자재가 있는 경우)
* 웹캠
* 키보드
* 마우스
* 모니터

학생들을 그룹으로 정렬하고, 각 그룹에 다른 색상을 갖는 포스트잇 혹은 종이를 배포한다.
각 자재에 다음 정보를 적어 넣을 수 있는 시간을 할당한다.

* 다음 자재는 무엇인가?
* 각 자재가 입력장치, 처리장치, 출력 장치인가?
* 각 자재가 수행하는 역할은 무엇인가?


학생들이 포스트잇 혹은 종이위에 정보를 모두 적어 놓은 후에, 그룹별로 정답을 토의할 시간을 갖는다.
어느 부품을 잘못 식별했는지, 정말 흥미로운 자재는 어떤 것인지, 학급에서 이유를 자유로이 토의한다.
모든 컴퓨터는 입력과 출력을 갖는다는 것을 설명한다.
로봇 목소리가 헤드폰 혹은 스피커를 통해 외부로 전달될 때, 채팅로봇 프로그램에 있어 이점이 중요하다.

<img src="fig/rpi-audio_output.png" width="50%" alt="오디오 출력을 헤드폰으로 강제선택함"/>

### 주요활동

1. 학생들에게 라즈베리파이 장비를 설치하고, 전원 켜서 사용자명 `pi`, 비밀번호 `raspberry`를 입력해서 
로그인하게 만든다. **IDLE3** 프로그램을 사용해서 채팅로봇 프로그램을 적재시킨다.

2. 이전 학습에서 나온 숙제를 사용해서, 학생들에게 더 많은 질문을 `input`과 `print` 함수를 사용해서 
추가하도록 지침을 준다.

3. 이제 프로그램의 단어를 라즈베리파이가 발음하도록 학생들에게 코드를 추가하도록 한다. 다음 코드를 
프로그램 상단에 추가한다.

~~~ {.python}
# My Python Program by ...
import os, time

def robot(text):
    os.system("espeak ' " + text + " ' ")

robot("Hello")
~~~

**들여쓰기는 매우 중요하다; IDLE3 텍스트 편집기는 자동으로 들여쓰기 기능을 제공한다.
추가로 공백과 인용부호를 잘 사용하는 것도 중요하다. 프로그램에 공백 혹은 인용부호가 없으면 동작하지 않는다.**

4. **File** 다음에 **Save As** 를 클릭해서, **robot1** 으로 이름을 짓고 저장한다.
프로그램을 실행시키면, "hello" 소리가 들여야 한다.

5. 다음으로, 질문을 화면에 출력시키는 대신에, 로봇 목소리로 말을 듣고, 대답을 한다.

이를 위해서, `print` 단어를 함수명 `robot`으로 바꾸고 나서, 콤마 `,`를 제거하고 `+` 기호로 치환한다.
편집한 것을 저장하게 하고 바로 테스트하게 만든다.
어떤 일이 생겼는지 설명할 수 있나요? 
가산점으로 로봇이 질문을 하게 만들 수도 있다!!!
`robot` 함수를 사용해서 입력 라인 바로 위에 명령문을 추가시키면 된다.

~~~ {.python}
robot('What is your name')
name = input('What is your name: ')
robot("Nice to meet you " + name)
~~~

<img src="fig/rpi-espeak2.png" width="87%" alt="질문하는 로봇"/>

옆좌석 학생과 자리를 바꾸게 한다. 몇분을 주고 옆사람 프로그램을 테스트하고, 
주석 `#` 기호를 사용해서 주석으로 적어도 한개 이상 개선점을 적도록 유도한다.
학생이 다시 좌석으로 돌아와서 주석을 보고 프로그램을 갱신한다.

조금더 확장하면, 옆좌석 친구 프로그램 코드 한줄을 삭제하고, 친구가
변경된 프로그램을 수정할 수 있는지 살펴본다.

