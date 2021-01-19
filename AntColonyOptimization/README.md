# 蚁群算法

参考博客：[蚁群算法原理和实现](https://blog.csdn.net/fanxin_i/article/details/80380733?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160561902619195264733525%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160561902619195264733525&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-80380733.first_rank_ecpm_v3_pc_rank_v2&utm_term=%E8%9A%81%E7%BE%A4%E7%AE%97%E6%B3%95+python&spm=1018.2118.3001.4449)

## 基本原理

![20201117220923.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117220923.png?raw=true)

1、蚂蚁在路径上释放信息素。

2、碰到还没走过的路口，就随机挑选一条路走。同时，释放与路径长度有关的信息素。

3、信息素浓度与路径长度成反比。后来的蚂蚁再次碰到该路口时，就选择信息素浓度较高路径。

4、最优路径上的信息素浓度越来越大。

5、最终蚁群找到最优寻食路径。

![20201117221029.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221029.png?raw=true)

基于TSP问题的基本蚁群算法：

## TSP求解

TSP求解中，假设蚁群算法中的每只蚂蚁是具有以下特征的简单智能体：

每次周游，每只蚂蚁在其经过的支路（i,j）上都留下信息素。

‚蚂蚁选择城市的概率与城市之间的距离和当前连接支路上所包含的信息素余量有关。

为了强制蚂蚁进行合法的周游，直到一次周游完成后，才允许蚂蚁游走已访问过的城市（这可由禁忌表来控制）。



基本蚁群的两个过程:

(1)状态转移

(2)信息素更新

(1)状态转移



为了避免残留信息素过多而淹没启发信息，在每只蚂蚁走完一步或者完成对所有n个城市的遍历(也即一个循环结束)后，要对残留信息进行更新处理。

由此，t+n时刻在路径(i,j)上的信息量可按如下规则进行调整：

![20201117221234.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221234.png?raw=true) 

## 信息素更新模型

蚁周模型（Ant-Cycle模型）

蚁量模型（Ant-Quantity模型）

蚁密模型（Ant-Density模型）



区别：

1.蚁周模型利用的是全局信息，即蚂蚁完成一个循环后更新所有路径上的信息素；

2.蚁量和蚁密模型利用的是局部信息，即蚂蚁完成一步后更新路径上的信息素。

![20201117221336.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221336.png?raw=true)

## 基本流程

![20201117221601.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221601.png?raw=true)

## 主要参数选择

![20201117221729.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221729.png?raw=true)

![20201117221648.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221648.png?raw=true)

## 优化

国内外，对于离散域蚁群算法的改进研究成果很多，例如自适应蚁群算法、基于信息素扩散的蚁群算法等，这里仅介绍离散域优化问题的自适应蚁群算法。

自适应蚁群算法：对蚁群算法的状态转移概率、信息素挥发因子、信息量等因素采用自适应调节策略为一种基本改进思路的蚁群算法。

自适应蚁群算法中两个最经典的方法：蚁群系统(AntColony System, ACS)和最大-最小蚁群系统(MAX-MINAnt System, MMAS)。

![20201117221837.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221837.png?raw=true)

![20201117221909.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221909.png?raw=true)

![20201117221933.png](https://github.com/metaphysicser/picture/blob/master/note/ASO/20201117221933.png?raw=true)