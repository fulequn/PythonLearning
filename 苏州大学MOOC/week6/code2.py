# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:27:06 2021

@author: 23820
"""

LETTERS = 'ABCDEFGHIJKLM,OPQRSTUVWXYZ'

def encrypt(msg, key):
    return translate_msg(msg, key, 'encrypt')

def decrypt(msg, key):
    return translate_msg(msg, key, 'decrypt')

#维吉尼亚加密法的实现
def translate_msg(msg, key, mode):
    cipher = []
    key_index = 0
    key = key.upper()
    for c in msg:
        num = LETTERS.find(c.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])
            num %= len(LETTERS)
            if c.isupper():
                cipher.append(LETTERS[num])
            else:
                cipher.append(LETTERS[num].lower())
            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            cipher.append(c)
    return ''.join(cipher)
  
#加密文本文件
def encrypt_file(src_file, des_file, key):
    src_file_obj = open(src_file)
    msg = src_file_obj.read()
    src_file_obj.close()
    msg_en = encrypt(msg, key)
    des_file_obj = open(des_file, 'w')
    des_file_obj.write(msg_en)
    des_file_obj.close()
    
#解密文本文件
def decrypt_file(src_file, des_file, key):
    src_file_obj = open(src_file)
    msg = src_file_obj.read()
    src_file_obj.close()
    msg_de = decrypt(msg, key)
    des_file_obj = open(des_file, 'w')
    des_file_obj.write(msg_de)
    des_file_obj.close()
