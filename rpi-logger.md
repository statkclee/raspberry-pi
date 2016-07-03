---
layout: page
title: xwMOOC 라즈베리 파이
subtitle: 감각모자 데이터 로거(Logger)
---

> ## 학습 목표 {.objectives}
>
> * 센서 다수에서 데이터를 수집하여 리스트 자료구조로 생성하는 방법을 학습한다.
> * 파이선 프로그램 내부에서 데이터를 텍스트 파일에 덧붙여 저장하는 방법을 배운다.
> * 감각모자 조이스틱에서 입력을 받아 대응하는 법을 학습한다.
> * 쓰레드를 사용해서 프로그램 여러 부분을 한번에 실행시킨다.

감각모자 하드웨어를 사용해서 주변 환경에 관한 다양한 정보를 수집하는 데이터 로거 장치를 만든다.

데이터 로거 장치를 만들게 되면 다양한 실험을 수행해서 데이터를 수집하게 된다. 가능한 실험에 다음이 포함된다.

* 4층 높이 옥상에서 데이터 로거 장치 낙하 실험
* 데이터 로거 장치를 냉장고에 넣고 온도 변화 관찰
* 헬륨 풍선으로 대기권 언저리로 데이터 로거 장치 날려보내기


> ### 원문 출처 및 저작 라이선스 {.getready}
>
> 이 번역의 원작 "[SENSE HAT DATA LOGGER](https://www.raspberrypi.org/learning/sense-hat-data-logger/)"은 라즈베리파이 재단에서 개발하여 공개하고 있다.
> 이 책은 크리에이티브 커먼스(Creative Commons)의 저작자표시(BY, Attribution), 동일조건변경허락(SA, Share-Alike) 라이선스(https://creativecommons.org/licenses/by-sa/2.0/kr/](https://creativecommons.org/licenses/by-sa/2.0/kr/) 를 준용합니다.

### 1. 필요한 하드웨어와 소프트웨어 

<img src="fig/rpi-sense-hat.png" alt="감각모자 이미지" width="30%">

* 하드웨어
    * SD카드가 장착된 라즈베리 파이
    * 라즈베리파이 기본 주변장치(USB 마우스, 키보드, 전원장치 등)
    * 감각모자(Sense HAT)
* 소프트웨어
    * 라즈비언 최신버젼 : `sudo apt-get dist-upgrade`
    * 파이썬3 Sense-HAT
    * 파이썬3 Pillow
    * 파이썬3 Evdev

~~~ {.shell}
sudo apt-get install sense-hat
sudo pip-3.2 install pillow
sudo pip-3.2 install evdev
~~~

### 2. 감각모자에서 데이터 가져오기

1. 매우 간략한 파이썬 스크립트를 작성해서 감각모자에서 데이터를 가져와서 화면에 출력한다. 센서를 사용해서 다음 데이터를 캡쳐해서 저장한다.

* 온도
* 습도
* 압력
* 움직임 

파이썬 스크립트를 작성하려면 라즈베리파이를 GUI 데스크톱 모드로 부팅하고 나서, 
파이썬3 IDLE 을 실행시킨다. 

IDLE이 실행되면 파이썬 쉘 윈도우가 뜨고, `File > New File` 을 선택하면 별도 창이 떠서 파이썬 코드를 작성할 수 있게 된다.


<img src="fig/rpi-idle3.png" alt="파이썬 IDLE 개발환경" width="70%">

상기 이미지 우측편 윈도우에 파이썬 코드를 작성하고, 왼쪽 윈도우에 파이썬 코드 실행결과가 출력된다. 
감각모자 센서에서 데이터를 수집하는 프로그램을 작성해보자.

2. 오른쪽 윈도우 창에 다음 파이썬 코드를 추가한다. `#` 기호로 시작하는 줄은 **주석(comments)** 으로 컴퓨터는 무시하지만, 사람에게는 유용하다. 주석을 사용해서 코드를 4개 부분으로 쪼갠다. 이렇게 하면 프로그램이 복잡해져도 프로그램을 더 쉽게 개발하게 된다.

<img src="fig/rpi-code1.png" alt="파이썬 코드 작성" width="30%">

* 첫번째 부분, **LIbraries** 라이브러리는 프로그램에 부가적인 기능을 부여하는 코드를 가져오는 영역이다.
`from sense_hat import SenseHat` 명령어는 감각모자 하드웨어를 사용하는 기능을 부여한다.
`from datetime import datetime` 명령어는 시간 모듈을 사용하는 기능을 부여한다.
* 두번째 부분, **Logging Settings** 로깅 설정 부분은 로거 프로그램의 다양한 기능을 제어하는 영역이다.
* 세번째 부분, **Function** 함수 부분에 '현 데이터를 파일에 저장' 같은 특정 작업을 수행하는 재사용가능한 코드 덩어리가 담겨진다.
* 마지막 부분, **Main Program** 주프로그램 부분은 전체 프로그램을 올바른 순열로 앞서 환경설정한 코드와 함수를 실행시키는 역할을 하게 된다.


3. 감각모자에서 데이터를 받아오려면 `get_sense_data` 함수를 호출한다. `get_sense_data` 함수는 센서 각각을 순서대로 점검하고 센서데이터를 리스트로 저장한다. 작성한 함수를 **Function** 영역에 추가한다.

~~~ {.python}
def get_sense_data():
    sense_data=[]

    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())
~~~

함수 첫번째 줄에 함수명이 정의되고, 두번째 줄에 빈 **리스트** 자료구조를 설정해서 수집되는 데이터가 추가되도록 만든다.

다음 네줄은 각 센서에서 데이터를 받아와서 `sense_data` 리스트에 센서데이터를 추가하거나 덧붙이는 역할을 수행한다.

먼저 방향(orientation)관련 센서는 값 3개를 되돌려 주어야 되서 다소 복잡하다.
방향값(요, 피치, 롤)을 감각모자에 요청하고, 전달받은 세가지 값을 `sense_data` 리스트에 쭉 집어넣는다.

~~~ {.python}
    o = sense.get_orientation()
    yaw = o["yaw"]
    pitch = o["pitch"]
    roll = o["roll"]
    sense_data.extend([pitch,roll,yaw])

    mag = sense.get_compass_raw()
    mag_x = mag["x"]
    mag_y = mag["y"]
    mag_z = mag["z"]
    sense_data.extend([mag_x,mag_y,mag_z])

    acc = sense.get_accelerometer_raw()
    x = acc["x"]
    y = acc["y"]
    z = acc["z"]
    sense_data.extend([x,y,z])

    gyro = sense.get_gyroscope_raw()
    gyro_x = gyro["x"]
    gyro_y = gyro["y"]
    gyro_z = gyro["z"]
    sense_data.extend([gyro_x,gyro_y,gyro_z])

    sense_data.append(datetime.now())

    return sense_data
~~~

함수 나머지 부분에 센서가 3개(지자계, 가속도, 자이로스코프) 더 추가되고 나서 현재시간을 추가한다.
함수 마지막에 **return** 문이 있어, 센서데이터를 요청한 주프로그램에 **sense_data** 리스트를 반환한다.

4. **Main Program** 주프로그램에 코드를 몇줄 추가해야 되는데, 다음 두가지 역할을 수행하게 된다:

* `sense` 객체를 생성. `sense` 객체는 `Sense HAT`을 대표함.
* 반복적으로 센서에서 `get_sense_data` 함수로 센서데이터를 가져오고, 이를 화면에 출력.

**Main Program** 주프로그램에 다음 코드를 추가한다.

~~~ {.python}
sense = SenseHat()

while True:
  sense_data = get_sense_data()
  print(sense_data)
~~~

<img src="fig/rpi-logger-fn.png" alt="로거 센서데이터 수집 함수" width="77%">

5. 이제 로거를 테스트한다. 먼저 작성한 파이썬 프로그램을 저장한다: **Ctrl+S** 키를 누르고 나서, `Sense_Logger_v1.py` 처럼 파일명을 저장한다. 프로그램을 저장하고 나서, **F5** 키를 눌러 실행한다. 다음과 같이 센서 정보가 스크롤 되면서 빨리 넘어가는 것이 보이면 정상이다.

<img src="fig/rpi-run1.png" alt="로거 센서데이터 수집 함수" width="50%">

상기 이미지에서 강조표시된 영역이 센서에서 수집된 데이터가 한데 묶여 리스트 한줄로 표시된 것이다. 리스트에 나온 데이터 중 어떤 부분이 어느 센서에서 나온 것인지 분간할 수 있어야 한다.

잘 돌고 있는 프로그램을 멈추는데 **Ctrl+C** 키를 눌러 실행을 취소한다.

### 3. 데이터를 파일에 저장

지금까지 작성한 프로그램은 연속적으로 감각모자 센서를 확인하고 나서 센서에서 나온 데이터를 화면에 출력하는 역할을 한다. 따라서, 정말 빨리 읽고 센서데이터를 기억하지 못하면 그다지 도움은 되지 않는다.

좀더 유용하게 만들려면 데이터를 CSV(콤마 구분값, Comma Separated Values) 파일에 저장해서, 나중에 로깅 프로그램이 종료된 후에 센서 데이터를 면밀히 조사하면 된다. 이런 파일을 생성하려면 다음 작업이 필요하다:

* 센서데이터에 대한 파일명을 지정한다.
* 파일 시작부에 필드명을 추가한다.
* 리스트 데이터를 파일에 텍스트 행으로 변환시킨다.
* 주기적으로 파일에 데이터 배치형태로 저장한다.

1. 가장 먼저해야할 작업은 **Setting** 영역에 다음 두줄을 추가하는 것이다:

~~~ {.python}
FILENAME = ""
WRITE_FREQUENCY = 50
~~~

첫번째 행은 센서데이터 출력결과를 저장할 파일명을 지정하는 것이고, 두번째 행은 프로그램이 얼마나 자주 센서데이터를 파일에 저장할지 설정하는 것이다. 이번 경우에 센서데이터 50줄을 선택해서 파일에 한번에 추가한다.

2. 다음으로, **log_data** 함수를 추가한다. `log_data` 함수는 **sense_data** 를 파일에 바로 저장할 수 있는 콤마구분값(CSV)으로 변환한다. 텍스트 한줄씩 **batch_data** 리스트에 추가되는데, 파일에 전달되어 저장될 때까지 센서데이터를 저장하는 역할을 한다.

**get_sense_data** 함수 앞에 다음 코드를 **Function** 함수 영역에 추가한다.

~~~ {.python}
def log_data():
  output_string = ",".join(str(value) for value in sense_data)
  batch_data.append(output_string)
~~~

첫번째 줄은 **sense_data** 리스트에 각 값을 받아 **문자열(string)** 로 변환하고, `,` 콤마기호로 결합한다. 이 작업 결과 다음 리스트가 

~~~ {.output}
[26.7224178314209, 25.068750381469727, 53.77205276489258, 1014.18017578125, 3.8002126669234286, 306.1720338870328, 0.3019065275890227, 71.13333892822266, 59.19926834106445, 39.75812911987305, 0.9896639585494995, 0.12468399852514267, -0.004147999919950962, -0.0013064055237919092, -0.0006561130285263062, -0.0011542239226400852, datetime.datetime(2015, 9, 23, 11, 53, 9, 267584)]
~~~

콤마 구분값으로 다음과 같이 변환된다.

~~~ {.output}
26.7224178314209,25.068750381469727,53.77205276489258,1014.18017578125,3.8002126669234286,306.1720338870328,0.3019065275890227,71.13333892822266,59.19926834106445,39.75812911987305,0.9896639585494995,0.12468399852514267,-0.004147999919950962,-0.0013064055237919092,-0.0006561130285263062,-0.0011542239226400852,2015-09-23 11:53:09.267584
~~~

3. 필요한 또다른 함수는 **file_setup** 함수로 어떤 센서데이터라도 앞서서 파일에 저장되는데 필요한 필드명 리스트를 생성시킨다. 아래 함수가 나와 있고, 물론 **Function** 함수 영역에 추가시킨다.

~~~ {.python}
def file_setup(filename):
  header  =["temp_h","temp_p","humidity","pressure",
  "pitch","roll","yaw",
  "mag_x","mag_y","mag_z",
  "accel_x","accel_y","accel_z",
  "gyro_x","gyro_y","gyro_z",
  "timestamp"]

  with open(filename,"w") as f:
      f.write(",".join(str(value) for value in header)+ "\n")
~~~

상기 함수는 이전 함수와 다소 차이가 나는데, 함수를 동작시키는데 입력(혹은 **매개변수**)가 필요하기 때문이다.
이 함수에 입력값은 `filename`이 된다. 주프로그램에서 `file_setup` 함수를 호출할 때, 함수명과 함께 저장할 파일명을 전달해야 된다. `file_setup("output.csv")`와 같이 호출되면, 함수가 자동으로 `output.csv` 파일을 생성한다.

함수 그자체로 헤더라고 불리는 헤더명을 갖는 리스트를 생성한다. 그리고 나서 **쓰기(write)** 모드(어떤 이전 데이터도 덮어쓴다)로 파일을 열고 해당 파일을 `f`로 참조한다. 파일이 열려있는 동안, 콤마를 사용해서 리스트 헤더를 모두 결합시키고, 해당 라인을 파일에 저장한다.

4. 이제 추가된 함수와 환경설정한 것이 주프로그램에서 사용되게 만든다.

다음 주프로그램에 다음에 

~~~ {.python}
##### Main Program #####
sense = SenseHat()
~~~

다음을 추가한다:

~~~ {.python}
batch_data= []

if FILENAME == "":
  filename = "SenseLog-"+str(datetime.now())+".csv"
else:
  filename = FILENAME+"-"+str(datetime.now())+".csv"

file_setup(filename)
~~~

첫번째 행은 50줄(혹은 `WRITE_FREQUENCY`에서 지정한 값)에 도달할 때까지 `sense_data` 행을 계속 추가하는데 사용될 빈리스트를 생성시킨다.

`if/else` 블록은 `FILENAME` 파일명이 설정되었는지 점검한다. 만약 어떤 파일명도 설정되지 않았다면, `SenseLog`가 기본디폴트 설정값으로 적용된다. 현재 날짜와 시간이 파일명에 추가된다.

마지막으로, **file_setup** 함수가 호출되어 바로 앞 `if/else` 블록에서 정해진 파일명을 인자로 넣어준다.

5. 마지막 타계는 `while True:` 루프 내부 로직 일부를 수정한다.

* **sense_data** 를 수집하게 만든다.
* **log_data** 함수를 사용해서 `sense_data`를 `CSV` 형태로 변환하고, **batch_data** 데이터에 추가한다.
* 데이터가 로그로 기록되면, 프로그램이 **batch_data** 크기가 이전에 설정한 `WRITE_FREQUENCY` 설정값을 넘어가는지 검사한다. 검사결과 설정값을 넘어서게 되면, 파일에 기록해서 저장하고 **batch_data** 를 다시 재설정한다.

`while True:` 루프는 다음 코드와 같이 갱신된다:

~~~ {.python}
while True:
  sense_data = get_sense_data()
  log_data()

  if len(batch_data) >= WRITE_FREQUENCY:
      print("Writing to file..")
      with open(filename,"a") as f:
          for line in batch_data:
              f.write(line + "\n")
          batch_data = []
~~~

* `print("Writing to file..")` 행은 선택사항으로 데이터가 파일에 기록될 때마다 화면에 메시지로 출력된다.
* `with open(filename,"a") as f:` 행은 파일을 **append** 덧붙이기 모드로 열어 덮어쓰는 대신에 파일 마지막 지점에 센서데이터를 추가한다.

전체 코드는 [여기](code/Sense_Logger_v2.py)에서 확인가능하다.

프로그램을 실행시키면, `Writing to file..` 메시지가 쭉 출력된다.

<img src="fig/rpi-run2.png" alt="로거 센서데이터 수집 실행화면" width="50%">

**Ctrl+C** 키를 눌러 로깅을 종료시킨다.

### 4. 부팅시점에 데이터 로거 시작

센서데이터를 로그로 남겨 저장하고자 할 때, 마우스/키보드/모니터를 갖추지 못할 경우도 많다.
이런 문제를 회피하는 방식중 하나가 라즈베리파이가 부팅될 때마다 작성한 프로그램을 실행시키는 것이다.
이런 작업을 위해서, 다음과 같은 터미널 윈도우를 먼저 열고, `sudo leafpad /etc/rc.local` 명령어로 편집기를 연다.
`rc.local` 스크립트는 라즈베리파이가 부팅되서 시장될 때 가장 마지막으로 호출되어 시작되는 스크립트다.
스크립트에 작성한 어떤 명령어도 부팅되는 시점에 적재되어 실행된다.

<img src="fig/rpi-terminal.png" alt="라즈베리파이 터미널" width="50%">

`Leafpad`가 실행되면, 다음과 같이 두 행을 추가하면 된다:

<img src="fig/rpi-rc_local.png" alt="라즈베리파이 rc.local 파일 설정" width="50%">

* 첫번째 행은 센서데이터 로거 스크립트가 저장된 디렉토리로 경로를 변경한다.
* 두번째 행은 `pi` 사용자로 바꾸고 나서 `python3 Sense-Logger.py` 명령어를 실행시킨다.
`&` 기호는 명령어를 백그라운드 작업으로 실행시켜, 라즈베리파이가 다른 작업을 계속하도록 만든다.

프로그램이 저장된 위치와 명칭이 다른 경우 `rc.local` 파일을 수정한다.

다음번 라즈베리파이가 부팅될 때 자동으로 센서데이터 수집 작업이 시작된다.

### 5. 데이터 수집

센서데이터 측정과 수집을 위해서 조건중 하나를 바꾸는 실험을 수행한다.

* 라즈베리파이를 냉장고에 넣고 냉장고 내부 온도를 측정한다. 냉장고문을 열게 되면 어떻게 될까?
얼마나 빨리 냉장고 내부온도가 외부정상온도로 돌아갈까?
* 키높이에서 라즈베리파이를 떨어뜨려 방향과 가속도에 변경사항을 추적하라(물론, 라즈베리파이를 낙하시키기 전에 충분한 안전장치를 두어서 고장나지 않도록 주의한다)
* 라즈베리파이를 고고도 풍선을 사용해서 대기중으로 높이 보내서, 상승비행중에 온도, 압력, 습도 변화를 탐색한다.

