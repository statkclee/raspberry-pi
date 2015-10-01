---
layout: page
title: xwMOOC 컴퓨터
subtitle: 구글 애널리틱스
minutes: 10
---

> ### 학습 목표 {.objectives}
>
> * 구글 애널리틱스를 학습한다.


### 구글 애널리틱스 설치 

1. [구글 애널리틱스에 가입한다.](http://www.google.com/analytics/)
1. 해당 웹페이지에 추적 코드를 생성한다.
    1. 상단 `관리` 메뉴를 클릭한다.
    1. `속성`을 클릭하고 `새 속성 만들기`를 클릭한다.
        - `웹사이트 이름`: 기억하기 좋은 이름을 부여한다.
        - `웹사이트 URL`:  추적하고자 하는 해당 웹사이트 URL을 입력한다.
        - `업종 카테고리`: 웹사이트에 가장 근사한 업종을 선택한다.
        - `보고 시간대`: *대한민국*으로 설정한다. 

~~~ {.shell}
  <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-59XXXXXX-1', 'auto');
    ga('send', 'pageview');

  </script>
~~~

3. 생성된 추적 코드를 `<header>` `</header>` 태그 사이 복사해서 붙여 넣는다.
4. 상단 `보고서`를 클릭하고 좌측 메뉴의 `실시간` &rarr; `개요`를 클릭한다.
    - 추적코드를 심은 웹사이트 URL을 별도 웹브라우져에서 열고 접속한다.
    - `새로 고침`을 여러번 눌러 정상적으로 페이지뷰가 올라오는지 확인한다.


<img src="fig/data-science-ga.png" width="50%" />
