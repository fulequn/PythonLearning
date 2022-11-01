# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:59:21 2019

@author: 23820
"""
class Graph:    #图类
    '''
    构造具有vertex个顶点的图
    输入：顶点个数
    '''
    def __init__(self, vertex):
        self.vertex = vertex#为点集赋值
        self.graph = [[0] * vertex for i in range(vertex)]#使用列表生成器生成邻接矩阵
    '''
    加边，这里u，v是顶点序号
    输入：u、v顶点的序号
    '''
    def add_edge(self, u, v, weight=1):#
        self.graph[u][v] = weight#对u、v进行-1使之与存储位置对应上

    '''
    展示函数，用于显示点之间的联系
    输出：图类的边集显示
    '''
    def show(self): #

        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print(" ")

'''
g = Graph(5)

g.add_edge(0, 1, 100.5)
g.add_edge(0, 4, 320.5)
g.add_edge(1, 2, 40)
g.add_edge(1, 3, 85)
g.add_edge(2, 0, 125)
g.add_edge(2, 3, 75)
g.add_edge(3, 0, 125)
g.add_edge(4, 2, 125)

g.show()
'''
