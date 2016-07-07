---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 마인크래프트 설치
---

> ## 학습 목표 {.objectives}
>
> *   마인크래프트 파이를 설치한다.
> *   마인크래프트를 실행한다.
> *   마인크래프트 기본 명령어를 학습한다.

## 마인크래프트 파이 설치

2014년 9월 이후 [라즈비안(Raspbian)](http://www.raspbian.org/) 라즈베리 파이에 
마인크래프트가 기본 설치되어 있다.

<img src="fig/minecraft-pi-shortcut.png" alt="마인크래프트 파이 단축 아이콘" width="20%">


만약 이전 라즈비안 버젼을 사용한다면, 터미널 윈도우를 열고 다음 명령어를 타이핑한다. 
(단, 인터넷에 연결이 되어 있어야 한다.)

~~~ {.shell}
sudo apt-get update
sudo apt-get install minecraft-pi
~~~

상기 작업을 끝낸 후에는 마인크래프트 파이와 파이썬 라이브러리가 설치되어야 한다.

### 마인크래프트 테스트

마인크래프트를 실행하기 위해서, 데스크톱 아이콘을 마우스로 두번 클릭하거나 혹은 터미널 윈도우에서 `minecraft-pi`를 키보드로 타이핑한다.

<img src="fig/mcpi-start.png" alt="마인크래프트 파이 실행" width="50%">


마인크래프트 파이(Minecraft Pi)가 실행되어 적재되면, **Start Game**(게임 시작하기)을 클릭하고, **Create New**(새로 생성하기)를 클릭한다. 담겨진 윈도우가 살짝 오프셋되어 있다. 따라서, 윈도우를 잡기 위해서는 마인크래프트 윈도우 뒤에 제목막대(title bar)를 잡아야 한다.

<img src="fig/mcpi-game.png" alt="마인크래프트 파이 게임" width="50%">


이제 마인크래프트 게임에 여러분이 들어가 있다.

## 마인크래프트 파이 실행

주위를 둘러보는데 마우스를 사용하고, 키보드에 다음 단축키를 사용한다.

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

