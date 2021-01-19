

# 粒子群优化算法（PSO）

❃粒子群算法(particleswarm optimization，PSO)由Kennedy和Eberhart在1995年提出，该算法对于Hepper的模拟鸟群(鱼群)的模型进行修正，以使粒子能够飞向解空间，并在最好解处降落，从而得到了粒子群优化算法。

❃同遗传算法类似，也是一种基于群体叠代的，但并没有遗传算法用的交叉以及变异，而是粒子在解空间追随最优的粒子进行搜索。

❃PSO的优势在于简单，容易实现，无需梯度信息，参数少，特别是其天然的实数编码特点特别适合于处理实优化问题。同时又有深刻的智能背景，既适合科学研究，又特别适合工程应用。



### 算法介绍、

（1）

❃每个寻优的问题解都被想像成一只鸟，称为“粒子”。所有粒子都在一个D维空间进行搜索。

❃所有的粒子都由一个fitness-function确定适应值以判断目前的位置好坏。

❃每一个粒子必须赋予记忆功能，能记住所搜寻到的最佳位置。

❃每一个粒子还有一个速度以决定飞行的距离和方向。这个速度根据它本身的飞行经验以及同伴的飞行经验进行动态调整。 



(2) 基本PSO算法

 a.  D维空间中，有m个粒子；

 粒子i位置：xi=(xi1,xi2,…xiD)

 粒子i速度：vi=(vi1,vi2,…viD)，1≤i≤m,1 ≤d ≤D

 粒子i经历过的历史最好位置：pi=(pi1,pi2,…piD)

 群体内（或领域内）所有粒子所经历过的最好位置：

 pg =(pg1,pg2,…pgD)

 PS:一般来说，粒子的位置和速度都是在连续的实数空间内进行取值。



![1.jpeg](https://github.com/metaphysicser/picture/blob/master/note/PSO/1.jpeg?raw=true)



![2.jpeg](https://github.com/metaphysicser/picture/blob/master/note/PSO/2.jpeg?raw=true)



![3.jpeg](https://github.com/metaphysicser/picture/blob/master/note/PSO/3.jpeg?raw=true)



![4.jpeg](https://github.com/metaphysicser/picture/blob/master/note/PSO/4.jpeg?raw=true)





## 自适应因子的引入

![3d48e53700078e35a26e0ec439a6913.png](https://github.com/metaphysicser/picture/blob/master/note/PSO/3d48e53700078e35a26e0ec439a6913.png?raw=true)

自适应调整法将每个粒子当前适应度作为变量加入调整策略中，通过动态调整惯性因子w，就可以对全局寻优性能进行调整，从而提高收敛速度，便于快速得到全局最优解。











参考博客：

[粒子群算法详解]([https://blog.csdn.net/zuochao_2013/article/details/53431767?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160274405919724838515556%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160274405919724838515556&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v28-2-53431767.first_rank_ecpm_v3_pc_rank_v2&utm_term=%E7%B2%92%E5%AD%90%E7%BE%A4%E7%AE%97%E6%B3%95&spm=1018.2118.3001.4187](https://blog.csdn.net/zuochao_2013/article/details/53431767?ops_request_misc=%7B%22request%5Fid%22%3A%22160274405919724838515556%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=160274405919724838515556&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v28-2-53431767.first_rank_ecpm_v3_pc_rank_v2&utm_term=粒子群算法&spm=1018.2118.3001.4187))



