#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，在源代码中写的中文输出可能会有乱码。

#print(u'中文测试！！')
#以unicode表示的str通过encode（）可编码为指定的bytes.
s='abc'
s.encode('ascii')
'中文'.encode('utf-8')

#'中文'.encode('ascii')  #报错，因为Unicode的编码范围大于ascii

#从网络或磁盘读取了字节流，读到的数据就是bytes，把bytes转换为str，使用decode（）方法，
s1=b'abc'
s1.decode('ascii')
print(s1)
#计算str包含多少字符，
print(len('abc'))
print(len('中文'))  #2

print(len(b'ABC'))   #bytes，计算的是字节数

print('中文'.encode('utf-8'))  #6 ,1个中文字符经过utf-8编码会占用3个字节，1个英文字符只占用1个字节

#python格式化表示：%
print('hello,%s,my age is %d' % ('zhangmei',24))

print ('%.2f' % 3.1415926) #小数点后保留两位整数

#example
s=(85-72)/72
print('%.1f' % s)

#若无特殊需求，使用UTF-8进行编码
