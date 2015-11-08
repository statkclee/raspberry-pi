---
layout: page
title: $100 달러 오픈 컴퓨터
subtitle: 로봇 운영체제(ROS) 
minutes: 10
---

> ### 로봇 운영체제(ROS) {.objectives}
>
> * 로봇 운영체제를 설치한다.

### 로봇 운영체제 설치

오로카 로보틱스 커뮤니티에 오른 ROS 준비한 스크립트를 사용한다.

[ROS 설치 이보다 편할순 없다! (오픈소스 소프트웨어 & 하드웨어: 로봇 기술 공유 카페 (오로카)), 표윤석](http://oroca.org/)

~~~ {.python}
wget https://raw.githubusercontent.com/oroca/oroca-ros-pkg/master/ros_install.sh && chmod 755 ./ros_install.sh && ./ros_install.sh catkin_ws indigo
~~~

[Ubuntu install of ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu)


### catkin

[catkin](https://github.com/ros/catkin)은 ROS 환경에서 개발된 응용프로그램의 빌드를 용이하기 위해서 개발된 파이썬 빌드도구다.

~~~ {.python}
sudo apt-get install python-catkin-tools
~~~

[참고: 오로카 ROS 튜토리얼](http://jihoonl.github.io/slides/how_to_ros/)


rqt_graph


### 거북이 실행

> roscore
# 새창을 열어서
> rosrun turtlesim turtlesim_node
# 또 다른 창을 열어서
> rostopic list
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
> rosrun turtlesim turtle_teleop_key


