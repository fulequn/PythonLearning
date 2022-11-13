# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:22:29 2021

@author: 23820
"""

def searchWord(filename, word):
    with open(filename, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line != "":
            idx = line.find('[解释]')
            if idx == -1:
                continue
            else:
                if word == line[:idx]:
                    return line[idx]
            line = file.readline()
    return ""

word = input("请输入单词或词组：")
line = searchWord("dict.txt", word)
if line != "":
    print(line)
else:
    print("查找失败")