#####python能表示的数据类型有：整数，浮点数，字符串，布尔型,空值，变量，常量。

+print (-8080)
+print(0xff00)
######浮点数
print(1.23e9)

print(" i'm ok!")

######字符串里既有'‘' 又有'“' 使用转义字符。
print('i \'m \"ok\"')     //i'm "ok"

######r''中''里的字符不需要转义
print(r'\\\t\\')

######打印多行字符
print('''line1
	...line2
	...line3''')
print(r'''line1
	...line2
	...line3''')

######布尔值：True,False
######可用and,or,not运算
print(True or False)
print(5>3 and 1>3)

#空值：一个特殊的值，用None表示，不能理解为0
后，理解变量在计算机内存中的表示也非常重要。当我们写：

#常量：Python没有

#变量在内存中的表示：
eg：a = 'ABC'
执行这条语句时时，Python解释器干了两件事情：在内存中创建了一个'ABC'的字符串；在内存中创建了一个名为a的变量，并把它指向'ABC'。

也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

a = 'ABC'   #解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：
b = a       #创建变量b，并指向a
a = 'XYZ'   #创建字符串'XYZ',且使a指向'XYZ'
print(b)    #此时b还指向'ABC'