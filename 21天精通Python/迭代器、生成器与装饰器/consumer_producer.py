# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:55:35 2020

@author: 23820
"""
#consumer_producer.py
def consumer():#定义一个消费者模型（生成器协程）
    print('等待接收处理任务')
    while True:
        data = (yield)
        print('收到任务', data)  #模拟接收并处理任务
        #此处可以执行函数调用来完成相关的任务
        
def producer():
    c = consumer()
    c.__next__()
    for i in range(3):
        print("发送一个任务……",'任务%d' % i)
        c.send('任务%d' % i)
        
if __name__ == "__main__":
    producer()
        
