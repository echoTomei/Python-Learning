#####python内置的os模块可直接调用操作系统提供的接口函数#####
```
import os
os.name #os的类型
```
#####操作文件和目录的函数一部分放在os模块中，一部分放在os.path中#####
```
os.path.abspath('.')  #查看当前目录的绝对路径
os.path.abspath('..')  #查看当前目录上层目录的绝对路径
os.path.join('c:\\','test')  #创建新目录第一步：首先将新目录的完整路径表示出来
os.mkdir('c:\\test')  #2.创建目录
os.rmdir('c:\\test')  #删除一个目录
os.path.split('c:\\python\\hello\\hello.py')  #拆分路径为两部分，后一部分是最后级别的目录和文件名
```
#####合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。#####
```
#文件操作
os.rename('test.txt','test.py')  #文件重命名
os.remove('test.py')  #删除文件
```
#####列出当前目录下的所有目录#####
`[x for x in os.listdir('.') if os.path.isdir(x)]`

#####列出当前目录下的所有.py文件：#####
`[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']`
