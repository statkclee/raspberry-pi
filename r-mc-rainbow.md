# xwMOOC 데이터과학




## 1. 무지개 그래프 [^minecraft-rainbow]

[^minecraft-rainbow]: [RaspberryJuice Bukkit Plugins](https://dev.bukkit.org/projects/raspberryjuice)

무지개를 마인크래프트에 구현하기 전에 무지개를 R Base 시각화 시스템으로 구현한다.

- 무지개 데이터를 쭉 생성시킨다.
- 무지개 색상을 준비한다.
- R Base 시각화 시스템으로 무지개를 도식화한다.

물론 `ggplot2` 시각화 시스템을 통해 무지개를 그려보는 것도 가능하다.


~~~{.r}
# 0. 환경설정 --------------------------------------------
library(miner)
mc_connect("127.0.0.1")

# 1. Rainbow plot --------------------------------------------
## 1.1. Rainbow Data
x <- seq(1,128,1)
y <- sin((x / 128.0) * pi)

## 1.2. Rainbow Color
n <- 7
color <- rainbow(n, s = 1, v = 1, start = 0, end = max(1, n - 1)/n, alpha = 1)

## 1.3. Draw Rainbow with Base Plot System

plot(x, y, type="n", ylim = c(0,10))
for(i in 1:7) {
  lines(x, y+i, col=color[i], lwd=7)
}
~~~

<img src="fig/minecraft-base-plot-1.png" style="display: block; margin: auto;" />

## 2. 마인크래프트 무지개 그래프

마인크래프트 세상에 무지개를 만들어 내려면, 다음 단계를 밟아 무지개를 완성해 나간다.

1. `getPlayerPos()` 함수를 활용하여 플레이어 현재 위치를 파악한다.
1. 무지개 높이, 색상, 무지개를 구성하게 될 아이템 블록을 설정한다.
1. 현재 플레이어 위치와 앞 단계에서 설정한 아이템 블록을 참조하여 무지개를 완성한다.
1. 마지막으로 현재 플레이어 위치에서 약간 떨어진 위치에서 전지적 작가시점으로 무지개를 지켜본다.


~~~{.r}
# 2. Minecraft Plot --------------------------------------------

## 2.1. Current Player Position
cur_pos <- getPlayerPos()

## 2.2. Rainbow Configuration

height <- 50
colors  <- c(14, 1, 4, 5, 3, 11, 10)

blue_block <- find_item("Blue Wool")

## 2.3. Build a Rainbow

for (x in 1:128){
  for (color in seq_along(colors)) {
    y  <- sin((x / 128.0) * pi) * height + color
    setBlock(cur_pos[1] + x - 64, cur_pos[2] + y, cur_pos[3], blue_block[2], colors[color])
  }
}

## 2.4. Watch a Rainbow

setPlayerPos(cur_pos[1], cur_pos[2], cur_pos[3]-50, tile=TRUE)
~~~

<img src="fig/minecraft-rainbow.png" alt="마인크래프트 무지개" width="57%" />
