# xwMOOC 데이터과학




## 0. R 마인크래프트 목차

- [마인크래프 세상 속 위치](r-mc-position.html)
- [하늘로 가는 계단](r-mc-stair.html)
- [지나온 길에 꽃을 뿌리기](r-mc-flower.html)
- [챗봇이 낸 문제 맞추기](r-mc-number-guess.html)
- [로고와 이미지](r-mc-images.html)
- [무지개(rainbow)](r-mc-rainbow.html)
- [미로](r-mc-maze.html)
- [데이터과학 시작 - 산점도](r-mc-stat.html)

## 1. R 마인크래프트

[miner: R package for controlling Minecraft via API](https://github.com/ropenscilabs/miner) 팩키지가 개발되어 R을 활용한 마인크래프트 도전이 
가능하게 되었습니다. 마인크래프트 서버를 통해 마인크래프트 R 코딩을 하기 위해서 사전에 설정된 두가지 방법이 존재한다.

- [Wiley 출판사, Adventures in Minecraft](http://as.wiley.com/WileyCDA/Section/id-823690.html) 방법: 1.6.4 버젼 지원.
- [No Starch 출판사, Learn to Program with Minecraft - Transform Your World with the Power of Python](https://www.nostarch.com/programwithminecraft) 방법: 마인크래프트 1.9.4 버젼 이상 설치 

윈도우 10 버젼을 사용하는 경우 [Learn to Program with Minecraft - Transform Your World with the Power of Python](https://www.nostarch.com/programwithminecraft) 방식을 추천한다.
일부 명령어가 [Wiley 출판사, Adventures in Minecraft](http://as.wiley.com/WileyCDA/Section/id-823690.html)에서 정상동작하지 않는 문제가 있을 수 있다.

## 2. R 마인크래프트 설치 

### 2.1. 버킷서버 1.6.4. Wiley 출판사 설치 방법

마인크래프트에 R로 작성한 코드를 돌리기 위해서 크게 3가지 구성요소가 필요하다.

- 마인크래프트 서버 설치
- 마인크래프트 클라이언트 (즉, 마인크래프트 게임) 설치
- R에서 API를 통해 마인크래프트 서버에 접속

#### 2.1.1. 마인크래프트 서버 설치

[Wiley 출판사, Adventures in Minecraft](http://as.wiley.com/WileyCDA/Section/id-823690.html)책은 파이썬을 이용한 마이크래프트 
프로그래밍을 학습할 수 있다.

[마인크래프트 PC Bukkit 서버](http://media.wiley.com/assets/7266/45/AIMStarterKitPC.zip)를 다운로드 받아 압축을 풀어 `StartBukkit.bat`를 
실행하게 되면 쉽게 마인크래프트 서버를 본인 PC에 설치할 수 있다. 물론, 맥을 비롯해 라즈베리파이에도 동일한 방식으로 쉽게 설치할 수 있다. 
웹사이트에서 설치 동영상도 제공하니 찬찬히 살펴보고나서 직접 따라하는 것도 좋을 듯 하다.

<img src="fig/minecraft-bukkit-server.png" alt="마인크래프트 버킷버서" width="77%" />

#### 2.1.2. 마인크래프트 클라이언트 (즉, 마인크래프트 게임) 설치

라즈베리파이를 소지한 경우 라즈비언을 설치하게 되면 무료 마인크래프가 포함되어 있어 문제가 없다.
하지만, 모바일 `Pocket Minecraft`, 윈도우 10 버젼 마인크래프트는 지원이 되지 않기 때문에 꼭 PC 버젼 
[minecraft.net](https://minecraft.net/ko-kr/)을 통해 구매를 한 버젼을 사용한다. 
저자와 같이 두번 결재를 하고 돈을 돌려받지 못한 경험은 하지 않았으면 좋겠다.
윈도우 10으로 구매를 하면 더 비싸기도 하다. 그리고 돈을 돌려달라고 여러번 의견을 표현해도 묵묵부답이다.
윈도우 10 스토어를 통한 구매는 비추한다.

[minecraft.net](https://minecraft.net/ko-kr/)에서 구매를 하게 되면 마인크래프트 론쳐(launcher)가 윈도우 바탕화면에 설치된다.
마인크래프트 론쳐에서 위에서 설치한 마인크래프트 서버에 접속한다는 강력한 의사를 전달해야 한다.
상기 마인크래프트 버킷서버가 1.6.4를 지원하기 때문에 론처에서 설정을 하고 나서 앞서 실행시킨 서버에 접속을 한다.

<img src="fig/minecraft-setup.png" alt="마인크래프트 실행" width="77%" />

### 2.2. Spigot 서버 1.9.4. No Starch 출판사 설치 방법

앞선 방법과 순서는 유사하다. 다만 버킷 서버 대신에 Spigot 서버가 사용된다는 면에서 차이가 나고 
자바설치를 확인하면 된다.

- 자바 설치 확인
- Spigot 마인크래프트 서버 설치
- 마인크래프트 클라이언트 (즉, 마인크래프트 게임) 설치
- R에서 API를 통해 마인크래프트 서버에 접속

설치과정에서 중요한 내용만 확인하면 다음과 같다.

[Learn to Program with Minecraft](https://www.nostarch.com/pythonwithminecraft/) 사이트를 방문하여 하단에 
윈도우의 경우 **Minecraft Tools.zip**, **Minecraft Tools Mac.zip** 파일을 다운로드 받는다.

- [Download the setup files for Windows (Minecraft Tools.zip)](https://sourceforge.net/projects/python-with-minecraft-windows/)
- [Download the setup files for Mac OS (Minecraft Tools Mac.zip)](https://sourceforge.net/projects/python-with-minecraft-mac/files/?source=navbar)

압축을 풀면 `Minecraft Tools` 폴터 아래 **install_API.bat** 파일을 실행하면 
Spigot 마인크래프트 서버 설치를 수행한다.
**Start_Server**를 실행하면 서버가 실행된다.

<img src="fig/minecraft-spigot-server.png" alt="마인크래프트 Spigot 서버" width="57%" />

#### 2.2.1. Spigot 마인크래프트 접속

마인크래프트 론쳐에서 마인크래프트 1.9.4 버젼으로 설정하고 `localhost`로 접속을 하게 되면 된다.
Spigot 마인크래프트 서버는 1.6.4 버젼은 지원을 중단한 것으로 보인다. 

<img src="fig/mincraft-spigot-server_join.png" alt="마인크래프트 Spigot 서버 접속" width="57%" />


### 2.3. R에서 마인크래프트 서버에 접속

R에서 API를 통해 마인크래프트에 접속하는 것은 초딩도 한다는 R 프로그래밍에 경험이 조금만 있다면 쉽게 할 수 있다.

`miner` 팩키지를 설치하고 나서, `mc_connect("127.0.0.1")` 명령어를 통해 로컬 컴퓨터에 접속한다.
그리고 `chatPost` 명령어를 통해 채팅을 통해 헬로월드를 통해 R코드를 마인크래프트에 정상적으로 전송할 수 있음을 확인한다.


~~~{.r}
devtools::install_github('ropenscilabs/miner')

library(miner)
mc_connect("127.0.0.1")

chatPost("안녕하세요...")
~~~

<img src="fig/minecraft-hello-world.png" alt="마인크래프트 헬로월드" width="77%" />

## 3. 마인크래프트 프로그래밍 정보

마인크래프트를 실행한 후에 윈도우에서는 `F3`를 클릭(노트북이나 맥에서 `Fn+F3`)하게 되면 디버그 화면에서
좌측 상단에 좌표정보를 확인할 수 있다. `F3`를 다시 클릭하게 되면 디버깅 정보가 사라진다.

<img src="fig/minecraft-f3-debug.png" alt="마인크래프트 F3 디버깅 정보" width="57%" />

## 4. 마인크래프트 기본 사용법

주위를 둘러보는데 마우스를 사용하고, 키보드의 다음 단축키를 사용한다.

| 단축키      | 동작           | Action              |
|:-----------:|:--------------:|:-------------------:|
| W           | 전진           | Forward             |
| A           | 왼쪽           | Left                |
| S           | 후진           | Backward            |
| D           | 오른쪽         | Right               |
| E           | 소장목록       | Inventory           |
| Space       | 뛰다           | Jump                |
| Double Space| 날다/떨어지다  | Fly / Fall          |
| Esc         | 일시정지/메뉴  | Pause / Game menu   |
| Tab         | 마우스커서 해제| Release mouse cursor|

빠른 그리기 패널(quick draw panel)에서 아이템을 선택하는데, `E` 를 누르거나, 
마우스 가운데 스크롤 휠, 혹은 키보드에 숫자를 사용해서 소장목록(inventory)에서 원하는 것을 고른다.

<img src="fig/mcpi-inventory.png" alt="소장목록(inventory)" width="50%">

스페이스바(space bar)를 두번 눌러 하늘로 날 수 있다. 누른 스페이스바를 해제하게 되면 하늘을 나는 것을 멈춘다.
만약 다시 스페이스바를 두번 누르게 되면 지상으로 떨어지게 된다.

<img src="fig/mcpi-flying.png" alt="하늘로 날아오르기" width="50%">

칼을 손에 잡고, 앞에 있는 블록을 클릭하면 해당 블록을 제거할(혹은 파고 들어갈) 수 있다. 
손에 블록이 있으면, 우클릭을 사용해서 앞에 손에 있는 블록을 놓거나 혹은 좌클릭으로 블록을 제거할 수 있다.

> ### 생존(survival) 모드, 창작(creative) 모드 {.callout}
>
> 좀비가 돌아다니면서 어두워지면 게임이 어려워지는 경우 채팅창을 활성화(키보드 `t` 누름)시켜 
> `/gamemode c`를 입력하면 창작(creative) 모드로 들어가고 반대로 창작모드에서 
> 생존 모드로 돌아가려면 채팅창에 `/gamemode c`를 입력하면 된다.


