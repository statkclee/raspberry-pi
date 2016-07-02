---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 파이썬 프로그래밍
---

> ## 학습 목표 {.objectives}
>
> *   파이썬 프로그램을 작성한다.
> *   변수 선언과 값을 대입한다.
> *   반복문과 조건문을 학습한다.
> *   API 프로그래밍을 실습한다. 

### Hello World !!!

마인크래프트가 실행중이고 세상(world)이 생성되고 나면, `Tab` 키를 누르게 되면 마우스를 자유로이 사용할 수 있게 되는데 마인크래프트 게임에서 벗어나 마우스 포인터를 옮길 수 있다. 
데스트톱(바탕화면)에 **IDLE** (IDLE3이 아님)을 열고 윈도우를 옮겨서 나란히 놓는다.

파이썬 윈도우에 직접 명령어를 타이핑하거나 파일을 생성해서 콛를 적어 저장하고 나중에 다시 실행할 수 있다.

만약 파일을 생성하고자 한다면, `File > New window`(파일>새창) 다음에 `File > Save`(파일>저장하기) 수행한다.
대체로 파일을 홈(home) 폴더나 새 프로젝트 폴더에 파이썬 프로그램 코드 파일을 저장한다.

마인크래프트 라이브러리를 가져오고, 게임에 연결을 생성하고, 마인크래프트 화면에 "Hello World" 메시지를 찍어 테스트한다. 

~~~ {.python}
from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")
~~~

만약 명령어를 파이썬 윈도우에서 직접 입력한다면, 각 라인을 입력하고 `Enter` 키를 친다.
만약 파일에서 코드를 입력한다면, `Ctrl + S`를 눌러 저장하고, `F5`를 눌러 실행한다.
작성한 코드를 실행하면, 게임 화면에 작성한 메시지가 보여야 한다.

<img src="fig/mcpi-idle.png" alt="Hello World" width="50%">

마인크래프트 윈도우에서 "Hello World"를 본다면, 이제 본격적으로 프로그래밍을 시작한다.

### 현재 위치 찾기

현재 본인의 위치를 찾기 위해서, 다음을 타이핑한다:

~~~ {.python}
pos = mc.player.getPos()
print pos
~~~

~~~ {.output}
Vec3(645.305762678,37.8643559655,-194.585066121)
~~~

대안으로, 좌표를 얻어 변수에 나눠 저장하는 멋진 방식으로 파이썬 개봉(unpacking) 기법을 사용한다.

~~~ {.python}
x, y, z = mc.player.getPos()
~~~

이제 `x`, `y`, `z`가 현재 위치 좌표 각각의 정보를 담고 있다.
`x`와 `z`는 걷는 방향(전진/후진, 좌측/우측) 정보를, `y`는 상/하 정보를 담고 있다. 
마인크래프트 좌표계는 다음과 같이 구성된다. 윈도우 `F3`를 클릭(노트북이나 맥에서 `Fn+F3`)하게 되면 디버그 화면에서
좌측 상단에 좌표정보를 확인할 수 있다.

- `x`축은 원점에서 동쪽(양수), 서쪽(음수), 즉 경도 (longitude)
- `z`축은 원점에서 남쪽(양수), 북쪽(음수), 즉 위도 (latitude)
- `y`축은 원점에서 높낮이(0~255, 64가 해수면), 즉 표고 (elevation)

<img src="fig/coordinates.png" alt="마인크래프트 좌표계" width="50%">

> ## 좌표(Coordinate) {.callout}
>
> 데카르트가 침대에 누워 천장을 바라보며 날아가고 있는 파리의 위치를 정확히 표현하기 위해서 `x`축과 `y`으로
> 표현되는 직교 좌표계를 고안했다고 한다. **좌표(coordiante)** 는 위치를 유일하게 표현하는 숫자 집합이다. 
> 마인크래프트에서도 3차원 좌표계를 사용해서 사용자 및 물체의 위치를 표현한다. 참조 [영문 좌표계(Coordinate System)](http://en.wikipedia.org/wiki/Coordinate_system), [국문 좌표계](https://ko.wikipedia.org/wiki/%EC%A2%8C%ED%91%9C%EA%B3%84), [마인크래프트 좌표](http://minecraft.gamepedia.com/Coordinates)


`getPos()` 메쏘드가 당해 시점에 플레이어 위치를 반환하는 것에 주목한다.
만약 위치를 이동하게 되면, 다시 함수를 호출하거나 저장된 위치정보를 사용해야 한다.

### 순간이동(Teleport, 텔레포트)

현재 위치정보를 알아낼 수도 있을 뿐만 아니라, 특정 지점을 명시해서 순간이동(teleport)도 할 수 있다.

~~~ {.python}
x, y, z = mc.player.getPos()
mc.player.setPos(x, y+100, z)
~~~

상기 명령어는 플레이어를 공중으로 100 칸 순간이동 시킨다. 
이것이 의미하는 바는 하늘 중간으로 플레이어를 순간이동 시킬 수 있고, 
처음 시작한 장소로 바로 되돌아 올 수도 있다.

다른 곳으로 지금 순간이동해 보세요!

## 블록(block) 설치

`mc.setBlock()` 메쏘드를 사용해서 특정 좌표위치에 한개 블록을 놓을 수 있다.

~~~ {.python}
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)
~~~

플레이어가 서있는 옆에 돌블록(stone block)이 나타나야 한다.
만약 플레이어 앞에 즉시 보이지 않는다면, 플레이어 뒤나 옆에 자리하고 있을 수 있다.
마인크래프트 윈도우로 돌아가서 마우스를 사용해서 플레이어 앞에 바로 회색 블록이 보일 때까지 
주변을 돌려본다.

<img src="fig/mcpi-setblock.png" alt="블록 설치" width="50%">

`set block`에 전달되는 인자는 `x`, `y`, `z`, 그리고 `id`다. `(x,y,z)`는 세계(world)에서 위치를 나타낸다.
(한개 블록 위치를 플레이어가 서 있는 장소에서 한칸 떨어지게 `x+1`으로 명시했다)
`id`는 설치하고자 하는 블록 유형을 나타낸다. `1`은 돌이 된다.

다른 유형의 블록을 시도해보라.

~~~ {.output}
Air:   0
Grass: 2
Dirt:  3
~~~

이제 눈앞에 보이는 블록을 뭔가 다른 것으로 바꿔보자.

~~~ {.python}
mc.setBlock(x+1, y, z, 2)
~~~

눈 앞에 회색 돌블록이 변경된 것을 봐야 한다.

<img src="fig/mcpi-setblock2.png" alt="블록 변경 설치" width="50%">

### 변수로서 블록

프로그램 코드 가독성을 높이기 위해서 변수를 사용해서 ID를 저장할 수 있다.
ID가 `block`으로 읽어올 수 있다.

~~~ {.python}
from mcpi import block

dirt = block.DIRT.id
mc.setBlock(x,y,z, dirt)
~~~

혹은, 만약 ID를 알고 있다면, 직접 설정할 수 있다.

~~~ {.python}
dirt = 3
mc.setBlock(x,y,z, dirt)
~~~

### 특수 블록

추가적인 속성(property)을 갖는 블록이 몇개 있다. 양모(wool) 같은 경우에는 색깔을 추가로 설정해야 한다.
양모 색깔을 설정하기 위해서 `setBlock`에 네번째 매개변수를 선택사항 옵션으로 사용한다.

~~~ {.python}
wool = 35
mc.setBlock(x,y,z, wool, 1)
~~~

여기서 네번째 매개변수 `1`은 양모색깔을 오렌지색으로 설정한다.
네번째 매개변수가 없다면, 디폴트(`0`)로 하얀색으로 설정한다. 이용가능한 다른 색깔은 다음과 같다:

~~~ {.input}
2: Magenta
3: Light Blue
4: Yellow
~~~

숫자를 변경해서 시도해 보고 블록 색깔이 바뀌는 것을 지켜보자.

추가적인 속성을 갖는 다른 블록에는 나무(`17`): 떡갈 나무(oak), 가문비 나무(spruce), 자작 나무(birch);
키큰 잔디(`31`):  관목, 잔디, 고사리; 토치(`50`): 동쪽, 서쪽, 북쪽, 남쪽; 그리고 추가로 더 있다.
전체 세부내용에 대해서는 [API 참고 문헌](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)을 살펴보기 바란다.

### 다수 블록 설치

`setBlock` 메쏘드로 블록 한개를 설치할 수도 있지만, `setBlocks`으로 특정 공간을 채울 수도 있다.

~~~ {.python}
stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)
~~~

10 x 10 x 10 정육면체를 단단한 돌로 채운다.

<img src="fig/mcpi-setblocks.png" alt="정육면체 돌" width="50%">

`setBlocks`함수로 더 용량을 갖는 도형을 생성할 수 있지만, 생성하는데 시간이 더 오래 걸릴 수도 있다.

### 걸어가면서 블록 설치하며 지나가기

이제 어떻게 블록을 설치하는지 알기 때문에, 걸어가면서 이동경로를 따라서 블록을 떨어뜨려 설치해보자.

다음 코드는 걸어가는 곳마다 플레이어 뒤에 꽃을 떨어뜨려 지나간다.

~~~ {.python}
from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

flower = 38

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)
~~~

이제 잠시 동안 앞으로 전진하고 나서 뒤를 돌아 지나온 이동 경로에 꽃이 떨어져 있는지 살펴보자.

<img src="fig/mcpi-flowers.png" alt="꽃" width="50%">


`while True` 루프를 사용해서 무한반복된다. 무한반복을 중지시키려면, 파이썬 윈도우에서 `Ctrl + C`를 누른다.

스페이스바를 두번 눌러 하늘로 날아보자. 하늘을 날면서 걸어간 경로에 꽃이 보인다.

<img src="fig/mcpi-flowers-sky.png" alt="하늘길 꽃" width="50%">

잔디위를 걸을 때만 꽃을 지나온 경로에 떨어 뜨리고 싶다면 어떨까? `getBlock`을 사용해서 블록이 어떤 유형인지 알아낼 수 있다:

~~~ {.python}
x, y, z = mc.player.getPos()  # player position (x, y, z)
this_block = mc.getBlock(x, y, z)  # block ID
print(this_block)
~~~

상기 코드는 플레이어가 *있는* 블록 위치를 알려준다(`0`일 것이다--공기블록). 
플레이어가 *서있는* 블록 유형을 알고 싶다. 
이를 위해서는 `y`에 1을 빼서 `getBlock()`을 사용하게 되면 플레이어가 서있는 블록의 유형을 식별할 수 있다.

~~~ {.python}
x,y,z = mc.player.getPos() # 플레이어 위치 (x,y,z)
block_beneth = mc.getBlock(x, y-1, z) # 블록 ID
print(block_beneth)
~~~

상기 코드는 플레이어가 서있는 블록 ID 정보를 출력하여 알려준다.

플레이어가 현재 서있는 곳 어디서나 블록 ID를 출력하는 루프를 실행하는 다음 코드를 테스트해보라.

~~~ {.python}
while True:
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y-1, z)
    print(block_beneath)
~~~

<img src="fig/mcpi-block-test.png" alt="밟고 서 있는 블록 유형" width="50%">


`if` 문장을 사용해서 꽃을 심을 것인지 심지 않을 것인지 선택한다.

~~~ {.python}
grass = 2
flower = 38

while True:
    x, y, z = mc.player.getPos()  # 플레이어 위치 (x, y, z)
    block_beneath = mc.getBlock(x, y-1, z)  # 블록 ID

    if block_beneath == grass:
        mc.setBlock(x, y, z, flower)
    sleep(0.1)
~~~

아마도 다음에 만약 플레이어가 잔디 위에 있지 않는다면, 
서있는 블록을 뒤집어 잔디위에 서있게 한다.

~~~ {.python}
if block_beneath == grass:
    mc.setBlock(x, y, z, flower)
else:
    mc.setBlock(x, y-1, z, grass)
~~~

이제 앞으로 전진하는데, 만약 잔디 위를 걷게되면 뒤에 꽃을 놓게 된다.
만약 걸어가는 다음 블록이 잔디가 아니라면, 잔디로 뒤집는다.
뒤를 돌아 다시 걷게 되면, 플레이어가 걸어 간 뒤에는 꽃이 놓여지게 된다.

<img src="fig/mcpi-flowers-grass.png" alt="잔디길과 꽃길" width="50%">


### 폭탄 블록 가지고 놀기

또다른 흥미로운 블록은 TNT다! 
정상적인 일반 TNT 블록을 위치시킬때, 다음과 같이 코드를 작성한다.

~~~ {.python}
tnt = 46
mc.setBlock(x, y, z, tnt)
~~~

<img src="fig/mcpi-tnt.png" alt="TNT 폭탄" width="50%">

하지만, TNT 폭탁이 매우 단조롭다. `data`에 `1`값을 적용해보자.

~~~ {.python}
tnt = 46
mc.setBlock(x, y, z, tnt, 1)
~~~

이제 칼을 사용해서 TNT 블록을 좌클릭하자: 폭탄이 활성화되고 수초내에 폭발할 것이다!

이제 엄청나게 큰 TNT 블록 폭탄더미를 만들어보자.

~~~ {.python}
tnt = 46
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)
~~~

<img src="fig/mcpi-tnt-blocks.png" alt="TNT 블록 폭탄더미" width="50%">


이제 매우 커다란 TNT 블록으로 가득찬 정육면체를 볼 수 있다.
다가가서 TNT 블록중에 하나를 활성화시키고 나서 장관을 지켜보기 위해 냅다 도망간다.
정말 많은 것이 한번에 변경되어서 그래픽을 렌더링하는데 정말 느릴 것이다.

<img src="fig/mcpi-tnt-explode.png" alt="TNT 블록 폭탄더미 폭파" width="50%">




## 다음 학습

이제 마인크래프트 세상을 여기저기 돌아다니는 방법과 파이썬 인터페이스 프로그래밍을 익혔기 때문에 
할 수 있는 것은 무척이나 많다.

### 네트워크 게임

만약 로컬 네트워크로 라즈베리 파이에 다수 학생이 접속한다면, 동일한 마인크래프트 세계에 접속해서 함께 게임을 즐길 수 있다. 플레이어는 마인크래프트 세상에서 서로를 만나게 된다.

### API 참고 문헌

블록 ID에 대한 전체 목록과 좀더 폭넓은 문서에 대해서 [stuffaboutcode.com](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)을 참조하기 바란다.

### 게임 만들기

또다른 학습 교재를 읽어보고 두더지 잡기(whac-a-mole) 게임을 만들어 보세요: [Minecraft Whac-a-Block](https://www.raspberrypi.org/learning/minecraft-whac-a-block-game/)