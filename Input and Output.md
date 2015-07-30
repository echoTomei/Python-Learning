1.输出字符串：
print('hello') 或者 print("hello")
输出多个字符串：print('hello','world','!!!')   //print()会依次打印每个字符串，遇到‘，’用空格代替。
            结果为： hello world !!!
还可直接输出表达式的值：print(2*4*6)  

2.输入：input()
eg: name=input()   //从键盘读入的值会存到变量name中
    print(name)   //可打印出name的值
 input函数也可加入输入的提示信息：
    name = input('please enter your name: ')
    print('hello,', name)

3.Python大小写敏感，注意缩进。

4.Python是动态语言，java是静态语言。

 a = 123 # a是整数
 print(a)
 a = 'ABC' # a变为字符串
 print(a)
 
动态语言变量本身类型不固定，静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

5.Python的两种除法：
  a.'\'除法
     除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数，
  b.'\\'除法
     称为 地板除，两个整数的除法仍然是整数，只取结果的整数部分
