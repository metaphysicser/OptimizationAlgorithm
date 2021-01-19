# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time: 2020/11/9 9:53
# @USER: 86199
# @File: (1+1)-ES
# @Software: PyCharm
# @Author: 张平路
------------------------------------------------- 
# @Attantion：
#    1、
#    2、
#    3、
-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt

DNA_SIZE = 1             # DNA (real number)
DNA_BOUND = [0, 5]       # solution upper and lower bounds
N_GENERATIONS = 200
MUT_STRENGTH = 5.        # 统一定义的变异强度


def F(x): return np.sin(10*x)*x + np.cos(2*x)*x     # to find the maximum of this function


# find non-zero fitness for selection
def get_fitness(pred): return pred.flatten()


def make_kid(parent):
    # 无交叉仅变异
    k = parent + MUT_STRENGTH * np.random.randn(DNA_SIZE)  #根据父代基因信息以及变异强度进行变异
    k = np.clip(k, *DNA_BOUND)    #控制范围
    return k


def kill_bad(parent, kid):
    global MUT_STRENGTH
    fp = get_fitness(F(parent))[0]      #计算得分
    fk = get_fitness(F(kid))[0]
    p_target = 1/5                      #变异强度的变异规则所定
    if fp < fk:     # kid better than parent
        parent = kid
        ps = 1.     # kid win -> ps = 1 (successful offspring)
    else:
        ps = 0.
    # adjust global mutation strength
    MUT_STRENGTH *= np.exp(1/np.sqrt(DNA_SIZE+1) * (ps - p_target)/(1 - p_target))    #变异强度的变异规则
    return parent


parent = 5 * np.random.rand(DNA_SIZE)   # parent DNA

plt.ion()       # something about plotting
x = np.linspace(*DNA_BOUND, 200)

for _ in range(N_GENERATIONS):
    # ES part
    kid = make_kid(parent)           #生孩子
    py, ky = F(parent), F(kid)
    parent = kill_bad(parent, kid)   #淘汰不好的

    # something about plotting
    plt.cla()
    plt.scatter(parent, py, s=200, lw=0, c='red', alpha=0.5,)
    plt.scatter(kid, ky, s=200, lw=0, c='blue', alpha=0.5)
    plt.text(0, -7, 'Mutation strength=%.2f' % MUT_STRENGTH)
    plt.plot(x, F(x)); plt.pause(0.05)

plt.ioff(); plt.show()