# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:27:46 2019

@author: 23820
"""
from graph import Graph


class Bank(Graph):    #银行类
    
    '''
    初始化方法，将对应个数的银行加入到抽象图中
    输入：bankNumber：银行个数
    '''
    def __init__(self, bankNumber):
        super().__init__(bankNumber)
    
    '''
    a银行借贷给b银行，抽象为有向图中的加边过程
    输入：a：a银行的编号，b：b银行的编号，Amount：贷款金额
    '''
    def loans(self, a, b, Amount):
        super().add_edge(a, b, Amount)
    
    '''
    检查是否安全
    输入：a:检测的银行，safe:安全的金额数
    '''
    def isSafe(self, a, safe=201):
        s = 0
        for i in self.graph[a]:
            s += i
        if(s < safe):
            print('no')
        else:
            print('yes')
        pass
    
g = Bank(5)
g.loans(0, 0, 25)
g.loans(0, 1, 100.5)
g.loans(0, 4, 320.5)
g.loans(1, 1, 125)
g.loans(1, 2, 40)
g.loans(1, 3, 85)
g.loans(2, 2, 175)
g.loans(2, 0, 125)
g.loans(2, 3, 75)
g.loans(3, 3, 75)
g.loans(3, 0, 125)
g.loans(4, 4, 181)
g.loans(4, 2, 125)

g.show()
g.isSafe(3)
g.isSafe(1)