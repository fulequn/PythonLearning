# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:56:21 2020

@author: 23820
"""
'''
测试代码
'''
#测试函数
def get_formatted_name(first, last):
    '''
    生成整洁的名字
    '''
    full_name = first + ' ' + last
    return full_name.title()

print("Enter 'q' at any time to quit. ")
while True:
    first = input("\nPlease give me a first name. ")
    if first == 'q':
        break
    last = input("Please give me a last name. ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print('\tNeatly formatted name: '+formatted_name+'. ')

#单元测试和测试用例
import unittest

class NamesTestCase(unittest.TestCase):
    '''
    测试类
    '''
    
    def test_first_last_name(self):
        '''
        能够正确处理想Janis Joplin这样的名字吗？
        '''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
#不能通过的测试
#添加新测试

#测试类
#各种断言方法
#一个要测试的类
#要测试类的行为，就必须要创建其实例，也称测试实例
#方法setUp()

