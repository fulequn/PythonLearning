# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:41:14 2021

@author: 23820
"""

def check(chessBoard, row, col):
    for i in range(row):
        if abs(col-chessBoard[i]) in (0, abs(row-i)):
            return False
    return True

def eightQueens(chessBoard, row):
    count = len(chessBoard)
    if row == count:
        print(chessBoard)
        return True
    for col in range(count):
        if check(chessBoard, row, col):
            chessBoard[row] = col
            if eightQueens(chessBoard, row+1): raise 1
    return False

result=[None]*8
try:
    eightQueens(result, 0)
except:
    pass

