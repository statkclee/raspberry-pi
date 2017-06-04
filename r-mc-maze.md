# xwMOOC 데이터과학




## 1. R 미로 [^minecraft-maze]

[^minecraft-maze]: [Generate a maze in Minecraft](https://ropenscilabs.github.io/miner_book/generate-a-maze-in-minecraft.html)

마인크래프트 미로를 생성하기 전에 R에서 풀수 있는 미로를 만드는 실습을 먼저한다.
다행히도 `Rmaze` 팩키지가 있어서 자동으로 다양한 미로를 생성할 수 있게 해준다.

- 설치방법: `devtools::install_github('Vessy/Rmaze')`
- 예제 돌려보기: Rmaze::runExample()

행과 열이 $5 \times 5$ 미로를 만드는데 `makeGraph` 함수를 생성시키고, `plotMaze()` 함수로 생성된 미로를 살펴본다.
하지만 이것은 진정한 미로라고 할 수 없다.



~~~{.r}
# 0. 환경설정 ----------------------------------------------
# devtools::install_github('Vessy/Rmaze')
library(Rmaze)

# 1. 미로 예제 ---------------------------------------------
# Rmaze::runExample()

## 1.1. 단순 미로 ------------------------------------------
n <- 5
set.seed(77)
maze <- makeGraph(n, n)
plotMaze(maze, n, n)
~~~

<img src="fig/minecraft-r-maze-1.png" style="display: block; margin: auto;" />

### 1.1. 다양한 미로

알고리즘별로 풀수 있는 즉, 입구와 출구가 존재하고 이를 통한 경로도 존재하는 미로를 자동으로 만들 수 있는 알고리즘이 몇개 있다.

- Recursive Backtracker 알고리즘: `makeMaze_dfs()`
- 크루스칼(Kruskal) 알고리즘: `makeMaze_kruskal()`
- 프림(Prim) 알고리즘: `makeMaze_prim()`

이에 대한 해법을 보고자 한다면 생성된 미로를 입력값으로 넣어두고 나서, `plotMazeSolution()` 함수를 사용한다.


~~~{.r}
## 1.2. 알고리즘 별 미로 ------------------------------------------
# Recursive Backtracker 
rb_maze <- makeMaze_dfs(maze)
plotMaze(rb_maze, n, n)
~~~

<img src="fig/minecraft-r-maze-algorithm-1.png" style="display: block; margin: auto;" />

~~~{.r}
# Kruskal
kruskal_maze <- makeMaze_kruskal(maze)
plotMaze(kruskal_maze, n, n)
~~~

<img src="fig/minecraft-r-maze-algorithm-2.png" style="display: block; margin: auto;" />

~~~{.r}
# Prim
prim_maze <- makeMaze_prim(maze)
plotMaze(prim_maze, n, n)
~~~

<img src="fig/minecraft-r-maze-algorithm-3.png" style="display: block; margin: auto;" />

~~~{.r}
## 1.3. 알고리즘 별 단계로 보는 미로 --------------------------
# Recursive Backtracker 
# makeMaze_dfs(maze, stepBystep = TRUE, n, n)
# Kruskal
# makeMaze_kruskal(maze, stepBystep = TRUE, n, n)
# Prim
# makeMaze_prim(maze, stepBystep = TRUE, n, n)

## 1.4. 미로 풀이 ---------------------------------------------
plotMazeSolution(rb_maze, n, n)
~~~

<img src="fig/minecraft-r-maze-algorithm-4.png" style="display: block; margin: auto;" />
