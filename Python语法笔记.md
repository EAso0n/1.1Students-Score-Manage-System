# Python语法

## 一、输入和输出

1. **print():** 括号内可填任意数量，任意类型 Python 对象，逗号分隔，四个可选的关键字参数 `sep`​、`end`​、`file`​、`flush` 来控制输出的格式、去向和刷新行为，直接计算表达式或 format 格式化输出
2. ​`input()` ​返回的数据类型是 `str`

   >>> name = input('请输入')
   >>> 请输入
   >>>
   >>> 张三
   >>> name
   >>> '张三'
   >>>
   >>
   >

## 二、Python 基础

​ **​`#`​**  ​开头的语句是**注释**，语句以冒号  **​`:`​** ​**结尾**时，**缩进**的语句**视为代码块**，坚持使用 ***4 个空格***的缩进

#### 数据类型和变量

1. 单引号或双引号引起的文本叫**字符串**
2. 字符串内部想保留单引号双引号，在引号前面加 **\转义字符**保留
3. \n 换行，\t tab,\\\代表\
4. ​**​`r''`​** ​ 表示 `''` 内部的字符串默认不转义

   >>> print(r'\\n')
   >>> \\n
   >>> print('\\\n')
   >>> \n
   >>>
   >>
   >
5. **三引号**  **​`'''`​** ​ **或**  **​`"""`​** ：用于创建多行字符串，内部的换行和引号都无需转义，换行为形式上的换行

   p = '''aaa's'a'''

   >>> print(p)
   >>> aaa's'a
   >>>
   >>
   >
6. **空值**用 **​`None`​** 表示
7. **变量名**必须是**大小写英文、数字和**  **​`_`​** ​**的组合**，且**不能用数字开头**
8. ​`is`​ 比较的是**对象身份**（是否指向同一块内存），`==`​ 比较的是**值**（可以被子类重写）：a is b
9. **变量的本质**：Python 变量是"**标签"** ，**变量赋值本质**：把标签从一个对象撕下来，贴到另一个对象上，**小整数缓存，** Python 在启动时会预创建 `-5`​ 到 `256` 之间的整数对象，所有引用这些值的变量都指向同一份

   > a \= [1, 2, 3]
   >
   > b \= a              # b 和 a 贴在了同一个列表对象上
   >
   > b.append(4)
   >
   > print(a)           # [1, 2, 3, 4] —— a 也变了！
   >
10. Python 为**动态语言**，可把任意数据类型赋给变量，可反复赋值，也可变类型

    >>> a =123
    >>> print(a)
    >>> 123
    >>> a='abc'
    >>> print(a)
    >>> abc
    >>>
    >>
    >
11. **多重赋值**：Python 支持一行给多个变量赋值，背后是**元组打包与解包**

    >>> x,y = 1,2
    >>> print(x,y)
    >>> 1 2
    >>>
    >>> 一行交换两个变量的值，不需要临时变量
    >>>
    >>> x,y = y,x
    >>> print(x,y)
    >>> 2 1
    >>>
    >>> 元组解包
    >>>
    >>> name,age = ('tom',78)
    >>> print(name,sge)
    >>> tom 78
    >>>
    >>
    >
12. **元组打包** ：不用加圆括号，标志为逗号，自动创建元组对象

    >>> t = 1,2,3
    >>> t
    >>> (1, 2, 3)
    >>> type(t)
    >>> <class 'tuple'>
    >>> a = 1,
    >>> type(a)
    >>> <class 'tuple'>
    >>>
    >>
    >
13. ​**​`return`​**​ **语句**其实是**元组打包**最常见的隐性触发点，返回打包的元组

    >>> def r():
    >>> ...     return 1,2
    >>> ...
    >>> p = r()
    >>> p
    >>> (1, 2)
    >>> type(p)
    >>> <class 'tuple'>
    >>>
    >>
    >
14. <table>
    <colgroup><col /><col /><col /></colgroup><thead><tr>
    <th colspan="3" rowspan="1">解包是打包的反向操作：将右侧可迭代对象（不限于元组，列表、字符串、生成器都可以）的元素，<span data-type="strong">逐一拆开并绑定到左侧对应位置的变量上</span>​</th>
    </tr>
    </thead><tbody><tr>
    <td>方向</td>
    <td>语法</td>
    <td>效果</td>
    </tr>
    <tr>
    <td>打包</td>
    <td>​<span data-type="code">t = a, b, c</span>​</td>
    <td>多个值 → 一个元组</td>
    </tr>
    <tr>
    <td>解包</td>
    <td>​<span data-type="code">x, y, z = iterable</span>​</td>
    <td>可迭代对象 → 多个独立变量</td>
    </tr>
    <tr>
    <td>星号解包</td>
    <td>​<span data-type="code">a, *b, c = iterable</span>​</td>
    <td>贪婪吸收中间元素为列表</td>
    </tr>
    <tr>
    <td>函数调用解包</td>
    <td>​<span data-type="code">f(*args)</span>​/<span data-type="code">f(**kwargs)</span>​</td>
    <td>可迭代/字典 → 独立的位置/关键字参数</td>
    </tr>
    </tbody>
    </table>
    >>> m,n = 'gh'
    >>> m
    >>> 'g'
    >>> n
    >>> 'h'
    >>> t = (1,2,3)
    >>> m,n,v = t
    >>> print(m,n,v)
    >>> 1 2 3
    >>>
    >>> head, \*tail \= "Python"
    >>>
    >>> head \= 'P'
    >>>
    >>> tail \= ['y', 't', 'h', 'o', 'n']   #注意：是列表，不是字符串
    >>>
    >>> ‍
    >>>
    >>
    >> #函数参数的逆操作
    >>
    >> args \= [3, 5]
    >>
    >> result \= pow(\*args)    # \*args 把列表解包成 pow(3, 5) 的两个位置参数
    >>
    >
15. 全部大写的变量名表示**常量**，`PI = 3.14159265359`，不是强制不会改变，约定俗成
16. **除法**：\和\\\，\的结果永为浮点数，最后一位**二进制尾数截断后转回十进制显示的自然结果**，\\\为地板除，只保留整数部分

    >>> 17/3
    >>> 5.666666666666667
    >>> 17//3
    >>> 5
    >>> 17%3
    >>> 2
    >>>
    >>
    >

#### 字符串和编码

1. **单字符**编码 **​`ord()`​**  ​函数获取字符的**整数**表示，**​`chr()`​**  ​函数把编码转换为对应的**字符**
2. ​**​`bytes`​**​**类型**的数据用**带** **​`b`​**​**前缀**的单引号或双引号表示

   >>> x = 'abc'
   >>> x
   >>> 'abc'
   >>> x = b'abc'
   >>> x
   >>> b'abc'
   >>>
   >>
   >
3. Unicode 表示的 `str` ​通过 **​`encode()`​** ​**方法->**​**​`bytes`​**​**类型**

   >>> 'abc'.encode('ascii')
   >>> b'abc'
   >>> '中午呢'.encode('UTF-8')
   >>> b'\xe4\xb8\xad\xe5\x8d\x88\xe5\x91\xa2'
   >>>
   >>
   >
4. 在 `bytes` ​中，**无法显示**为 ASCII 字符的字节，用 `\x##` ​显示
5. ​**​`bytes->str`​**​ **，**​**​`decode()`​** ​**方法,**​`errors='ignore'` ​忽略错误的字节：

   >>> b'kkk'.decode('UTF-8')
   >>> 'kkk'
   >>>
   >>> b'\xe4\xb8'.decode('UTF-8',errors='ignore')
   >>> ' '
   >>>
   >>
   >
6. **len()** 统计 **str 字符数，bytes 字符数，1 个中文字符**经过 **UTF-8** 编码后通常会占用 **3 个字节**，而 1 个英文字符只占用 1 个字节 **。**
7. **字符串格式化：% 实现**，单个替换内容省略括号

   |占位符|替换内容|
   | ------| ------------|
   |%d|整数|
   |%f|浮点数|
   |%s|字符串|
   |%x|十六进制整数|

   >>> 'hello,%s' % 'ww'
   >>> 'hello,ww'
   >>> 'my name is %s,age is %d' % ('li',36)
   >>> 'my name is li,age is 36'
   >>>
   >>
   >
8. **占位符完整结构：%[(key)][标志][最小宽度][.精度]转换类型，
   宽度--------** 填充的个数，右对齐，
   **标志** —— 控制对齐和填充，0-> 宽度空格 0 填充，'-'-> 左对齐，
   **精度** —— 小数保留几位

   <table>
   <colgroup><col /><col /><col /></colgroup><thead><tr>
   <th>类型字符</th>
   <th>含义</th>
   <th>示例 <span data-type="code">'%x' % val</span>​→</th>
   </tr>
   </thead><tbody><tr>
   <td>​<span data-type="code">d</span>​/<span data-type="code">i</span>​</td>
   <td>有符号十进制整数</td>
   <td>​<span data-type="code">'%d' % 3</span>​→<span data-type="code">3</span>​</td>
   </tr>
   <tr>
   <td>​<span data-type="code">f</span>​</td>
   <td>浮点数（小数形式）</td>
   <td>​<span data-type="code">'%f' % 3.14</span>​→<span data-type="code">3.140000   </span>​</td>
   </tr>
   <tr>
   <td>​<span data-type="code">s</span>​</td>
   <td>字符串（自动调 <span data-type="code">str()</span>​）</td>
   <td>​<span data-type="code">'%s' % 42</span>​→<span data-type="code">42</span>​  把任何类型转换为字符串</td>
   </tr>
   <tr>
   <td>​<span data-type="code">%%</span>​</td>
   <td rowspan="1" colspan="2"><span data-type="code">%%</span>​ 是转义的百分号本身，它不消耗右边的值<br /></td>
   </tr>
   </tbody>
   </table>
   > print('%2d' % 1)      # ' 1'  （空格填充，默认）
   > print('%02d' % 1)     # '01'  （0 填充）
   > print('%-2d' % 1)     # '1 '  （- 标志：左对齐，空格补在右边）
   > print('%.3s' % 'Hello')        # 'Hel'  对于 `s`​ 类型，`.精度`​ 的含义变成**截取前几个字符**：
   > print('%f' % 3.1)              # '3.100000'  `不写精度默认保留6位小数，补0`
   > print('%5d' % 3)      # '    3'  （总共占 5 个字符，右对齐）
   >
9. 字符串格式化：**str.format（）** 实现：传入的参数依次替换字符串内的占位符 `{0}`​、`{1}`

   >>> '{0}aaab{1:.2f}dd'.format(12,34.45453)
   >>> '12aaab34.45dd'
   >>>
   >>
   >
10. 字符串格式化：**f-string** 实现  以 `f`​ 开头的字符串，称之为 `f-string`​ **变量替换**字符串内{ }的内容 **（重要）**

    >>> r = 1.23
    >>> b= 23
    >>> print(f'{r:.1f}asda{b}')
    >>> 1.2asda23
    >>>
    >>
    >

#### list、tuple

1. **list:** 有序集合，可增删改查，
2. **len()** 获取列表个数，
3. 索引 **[ ]** 访问列表元素，
4. 列表**最后一个元素[-1]索引**
5. list 是一个可变的有序表,**append()** 往 list 中**追加元素到末尾，insert（）把元素插入到指定的位置，pop()默认删除末尾并返回其值，pop(i)删除指定并返回，通过索引直接替换对应元素**

   >>> l = [1,2,3,4]
   >>> l.append(5)
   >>> l
   >>> [1, 2, 3, 4, 5]
   >>> l.insert(0,9)
   >>> l
   >>> [9, 1, 2, 3, 4, 5]
   >>> l.pop()
   >>> 5
   >>> l
   >>> [9, 1, 2, 3, 4]
   >>> l.pop(0)
   >>> 9
   >>> l
   >>> [1, 2, 3, 4]
   >>>
   >>
   >
6. **tuple 元组：有序列表，tuple 一旦初始化就不能修改，没有增删改，只有通过索引[ ]查，代码安全**
7. 定义一个 tuple 时，在**定义**的时候，**tuple 的元素就必须被确定**下来
8. 定义一个**空的 tuple**，可以写成  **​`()`​** ​，有 **1 个元素**的 tuple 定义时必须加一个**逗号**  **​`,`​** 

   >>> t = (1,2)
   >>> t
   >>> (1, 2)
   >>> t = ()
   >>> t
   >>> ()
   >>> t = (1,)
   >>> t
   >>> (1,)
   >>>
   >>
   >
9. tuple 所谓的“不变”是说，tuple 的每个元素，**tuple 本身的结构不可变：不能增删改元素（引用）。但引用指向的对象如果是可变的（如 list），那个对象内部可以自由修改，创建一个内容也不变的 tuple 怎么做？那就必须保证 tuple 的每一个元素本身也不能变**

‍

#### 条件判断 if

1. if < 条件判断 1>:
   < 执行 1>
   elif < 条件判断 2>:
   < 执行 2>
   elif < 条件判断 3>:
   < 执行 3>
   else:
   < 执行 4>
2. ​`if` ​语句执行有个特点，它是从上往下判断，如果在**某个判断上是** **​`True`​**​，把该判断对应的语句执行后，就**忽略掉剩下的** **​`elif`​**​**和** **​`else`​**
3. ​`if` ​判断条件还可以**简写，** 只要 `x` ​是**非零数值、非空字符串、非空 list** 等，就判断为 `True`​，否则为 `False`
   if x:
   print('True')
4. ​**​`int()`​** ​ **函数** 转换成整数

‍

#### 模式匹配 `match`

1. **match 匹配**

   score = 'B'

   match score:
   case 'A':
   print('score is A.')
   case 'B':
   print('score is B.')
   case 'C':
   print('score is C.')
   case _: # _表示匹配到其他任何情况
   print('score is ???.')

   ‍

#### 循环

1. ​**​`for x in ...`​**  ​循环就是把每个元素代入变量 `x`，然后执行缩进块的语句

   >>> l = (1,2,3)
   >>> for i in l:
   >>> ...     print(i)
   >>> ...
   >>> 1
   >>> 2
   >>> 3
   >>>
   >>
   >
2. **while 循环**，只要条件满足，就不断循环，条件不满足时退出循环

   >>> sum = 0
   >>> n = 10
   >>> while n >0:
   >>> ...     sum = sum +n
   >>> ...     n = n-1
   >>> ... print(sum)
   >>> ...
   >>> 55
   >>>
   >>
   >
3. ​**​`range()`​**  ​函数，可以生成一个整数序列，**​`list()`​**  ​函数可以转换为 list，`range(5)` ​生成的序列是从 0 开始小于 5 的整数

   >>> list(range(5))
   >>> [0, 1, 2, 3, 4]
   >>> list(range(2,5))
   >>> [2, 3, 4]
   >>>
   >>
   >
4. 在循环中，**​`break`​** ​语句可以提前退出循环，通过 **​`continue`​** ​语句，跳过当前的这次循环，直接开始下一次循环

#### dict、set { }

1. **dict 字典：** 使用**键-值（key-value）** 存储，具有极快的**查找速度，根据 key 可修改 value**

   >>> d = {'zs':78,'ls':89,'ww':58}
   >>> d
   >>> {'zs': 78, 'ls': 89, 'ww': 58}
   >>> d['ww']
   >>> 58
   >>> d['ls'] = 100
   >>> d
   >>> {'zs': 78, 'ls': 100, 'ww': 58}
   >>>
   >>
   >
2. dict :**​`in`​** ​判断 key 是否存在，或 dict 提供的 **​`get()`​** ​**方法**，如果 **key 不存在**，可以**返回** **​`None`​**​，或者自己**指定的 value**

   >>> 'jj' in d
   >>> False
   >>> d.get('jj',-1)
   >>> -1
   >>>
   >>
   >
3. 要删除一个 key，用 **​`pop(key)`​** ​**方法**，对应的 value 也会从 dict 中**删除，返回对应 value**
4. 和 list 比较，dict 特点：**查询、插入快**，不会因 key 增加变慢，**占内存**，空间换时间
5. dict 的 key 必须是**不可变对象，dict 根据 key 来哈希算法**计算 value 的存储位置，字符串、整数等都是不可变，list 是可变的
6. **set:只有 key,不存 value,无重复 key**
7. **创建一个 set**，用 `{x,y,z,...}` ​列出每个元素，**set()方法**转换为 set 类型

   >>> ss = {3,4,5}
   >>>
   >>> l = [1,2,3]
   >>>
   >>> s = set(l)
   >>> s
   >>> {1, 2, 3}
   >>> s= set((1,23))
   >>> s
   >>> {1, 23}
   >>>
   >>
   >
8. set 中**重复元素自动过滤**，**​`add(key)`​** ​**方法**可以添加元素到 set 中，**​`remove(key)`​** ​**方法**可以删除元素

   >>> s
   >>> {1, 23}
   >>> s.add(5)
   >>> s
   >>> {1, 5, 23}
   >>> s.remove(23)
   >>> s
   >>> {1, 5}
   >>>
   >>
   >
9. **set 不可以放入可变对象,和 dict 原理相同**

## 三、函数

#### 调用函数

1. **函数名指向函数对象**，可以把**函数名赋给一个变量**，相当于给这个**函数起“别名”** ，**abs()绝对值，max()最大值**

   >>> m = max
   >>> m(1,2,3)
   >>> 3
   >>>
   >>
   >

#### 定义函数

1. **定义函数** **​`def`​**​**语句**，依次写出**函数名**、**括号**、括号中的**参数**和**冒号**  **​`:`​** ​，然后，在**缩进块中编写函数体**，函数的返回值用 **​`return`​**​**语句返回**。

   >>> def fun():
   >>> ...     return -1
   >>> ...
   >>> fun()
   >>> -1
   >>>
   >>
   >
2. **没有 return，返回 none,**​`return None` ​可以简写为 `return`
3. ​**​`pass`​** ​可以用来作为**占位符 定义空函数**

   >>> def nop():
   >>> ...     pass
   >>> ...
   >>>
   >>
   >
4. **函数返回多值**其实就是**返回一个 tuple**

#### 函数参数

1. **位置参数**，调用函数时，传入的值按照**位置先后顺序**依次**赋给参数**

   >>> def power(x,n):
   >>> ...     s=1
   >>> ...     while n>0:
   >>> ...         n = n-1
   >>> ...         s = s*x
   >>> ...     return s
   >>>
   >>> power(5,2)
   >>> 25
   >>>
   >>
   >
2. **默认参数**：给**位置参数以默认值**，简化函数调用，**必选参数在前，默认参数在后**
3. 当函数有**多个参数**时，把**变化大的参数放前面**，**变化小的参数放后面**。**变化小**的参数就可以**作为默认参数**

   >>> def enroll(name, gender, age=6, city='Beijing'):
   >>> ...     print('name:', name)
   >>> ...     print('gender:', gender)
   >>> ...     print('age:', age)
   >>> ...     print('city:', city)
   >>> ...
   >>>
   >>> enroll('zs','F')
   >>> name: zs
   >>> gender: F
   >>> age: 6
   >>> city: Beijing
   >>>
   >>> enroll('ls','M',7)
   >>> name: ls
   >>> gender: M
   >>> age: 7
   >>> city: Beijing
   >>>
   >>> ‍
   >>>
   >>> enroll('ls','M',city='shanghai')
   >>> name: ls
   >>> gender: M
   >>> age: 6
   >>> city: shanghai
   >>>
   >>
   >
4. 定义默认参数要牢记一点：**默认参数必须指向不可变对象**！默认参数的值在函数定义时被计算一次，而不是每次调用时重新计算

   def add_to_list(item, target=[]):      # [] 在 def 语句执行时创建
   target.append(item)
   return target

   print(add_to_list(1))    # [1]
   print(add_to_list(2))    # [1, 2]  ← 预期是 [2]！同一个列表对象
   print(add_to_list(3))    # [1, 2, 3]  ← 持续累积
5. **可变参数：在参数前面加了一个**  **​`*`​** ​**号，*参数接收到的是一个 tuple，调用该函数时，可以传入任意个参数，包括 0 个参数**
6. 如果已经有一个 list 或者 tuple，可以在 **list 或 tuple 前面加一个**  **​`*`​** ​**号**，把 list 或 tuple 的元素变成**可变参数**传进去

   >>> def cal(**num)
   >>> :...     sum = 0
   >>> ...     for i in num
   >>> :...         sum = sum + i*i*
   >>> ...     return sum
   >>> ...
   >>> cal(1,2,3)
   >>> 14
   >>>
   >>> n = [4,5,6]
   >>>
   >>> cal(*n)
   >>> 77
   >>>
   >>
   >
7. **关键词参数：关键字参数允许你传入 0 个或任意个含参数名的参数（也就是 dict），这些关键字参数在函数内部自动组装为一个 dict**
8. ​`**extra`​ 表示把 dict 的所有 key-value 用关键字参数传入到函数的 `**kw`​ 参数，`kw`​ 将获得一个 dict，`kw`​ 获得的 dict 是 `extra`​ 的一份**拷贝**，对 `kw`​ 的改动不会影响到函数外的 `extra`

   >>> def person(name,age,**kw):
   >>> ...     return(name,age,kw)
   >>> ...
   >>>
   >>> person('zhangsan',30)
   >>> ('zhangsan', 30, {})
   >>>
   >>> person('zhangsan',30,city = 'bj')
   >>> ('zhangsan', 30, {'city': 'bj'})
   >>>
   >>> extra = {'job':'engineer','city':'sh' }
   >>> person('zhangsan',30,**extra)
   >>> ('zhangsan', 30, {'job': 'engineer', 'city': 'sh'})
   >>>
   >>
   >
9. **命名关键词参数：限制传入的关键词参数**
10. 和关键字参数 `**kw` ​不同，**命名关键字参数需要一个特殊分隔符**  **​`*`​** ​， **​`*`​** ​**后面的参数被视为命名关键字参数**

    >>> def person(name,age,*,city,job):
    >>> ...   return(name,age,city,job)
    >>> ...
    >>> person('zs',45,city='sh',job='en')
    >>> ('zs', 45, 'sh', 'en')
    >>>
    >>
    >
11. 如果函数定义中已经有了一个**可变参数**，后面跟着的**命名关键字参数就不再需要一个特殊分隔符**  **​`*`​** ​，**命名关键字参数必须传入参数名**

    >>> def person(name,age,*args,city,job):
    >>> ...   return(name,age,args,city,job)
    >>> ...
    >>> person('ls',78,0,city = 'sh',job = 'en')
    >>> ('ls', 78, (0,), 'sh', 'en')
    >>>
    >>
    >
12. 命名关键字参数**可以给默认值**，从而简化调用
13. **参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数**

## 四、高级特性

#### 切片 Slice

1. **L[ 0:4 ]都是索引，索引 0 取到索引 4，前闭后开，**
2. 切片描述的是"**从哪开始、到哪结束、跨多大步**"
3. 第一个索引是 **​`0`​**​，还可以**省略，**​`[:]` ​就可以原样复制一个 list，第二个空代表到最后
4. **倒数第一个元素**的索引是  **​`-1`​**

   >>> l[-10:]
   >>> [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
   >>>
   >>
   >
5. **第二个数/第三个数**也相当于**取出的个数**
6. **步长** `L[0:10:2]`​-->[0.2.4.6.8]  **每两个取一个**，
7. **tuple** 也可以用切片操作，只是**操作的结果仍是 tuple**

   >>> (0,1,2,3,4)[:2]
   >>> (0, 1)
   >>>
   >>
   >
8. **字符串**也可以用切片操作，只是**操作结果仍是字符串**

   >>> 'abcd'[0:2]
   >>> 'ab'
   >>>
   >>
   >
9. 切片赋值：**批量替换任意长度的内容**

   L \= [0, 1, 2, 3, 4, 5]

   L[2:4] \= [99, 100]          # [0, 1, 99, 100, 4, 5]

#### 迭代（遍历）Iteration

1. 通过 **​`for`​**​**循环**来**遍历**这个 **​`list`​**​**或** **​`tuple`​**​，这种遍历我们称为**迭代**
2. **for 循环**可用在**可迭代对象**上，可迭代对象，**无论有无下标**，都可以迭代
3. 默认情况下，**​`dict`​**​**迭代**的是 **key**。**迭代 value**，可以用 **​`for value in d.values()`​** ​，如果要**同时迭代 key 和 value**，可以用 **​`for k, v in d.items()`​** 

   >>> d = {'a': 1, 'b': 2, 'c': 3}
   >>> for key in d:
   >>> ...     print(key)
   >>> ...
   >>> a
   >>> c
   >>> b
   >>>
   >>
   >
4. **字符串也可迭代**

   >>> for ch in 'ABC':
   >>> ...     print(ch)
   >>> ...
   >>> A
   >>> B
   >>> C
   >>>
   >>
   >
5. ​`collections.abc` ​模块的 **​`Iterable`​**​**类型判断**是否是**可迭代对象（list,tuple,dict,字符串,generator，set）**

   >>> from collections.abc import Iterable
   >>> isinstance([ ],Iterable)
   >>> True
   >>> isinstance('',Iterable)
   >>> True
   >>> isinstance((1,),Iterable)
   >>> True
   >>> isinstance({ },Iterable)
   >>> True
   >>>
   >>
   >
6. ​**​`enumerate`​**​**函数**可以把一个 **​`list`​** ​变成**索引-元素对，类似于为每个元素加索引**

   >>> for x,y in enumerate(['a','b']):
   >>> ...     print(x,y)
   >>> ...
   >>> 0 a
   >>> 1 b
   >>>
   >>
   >

#### 列表生成式（用来创建 list 的生成式）

1. **语法：[表达式   for  变量  in  可迭代对象   if 条件]，表达式**：对每个元素做什么运算，**if 条件**（可选）：过滤满足条件元素
2. **类似于数学中**

   $$
   \{x^2 \ |\ x \in \mathbb{Z},\ 0 \le x < 10,\ x \text{ 是偶数}\}
   $$
3. **多个过滤条件**：多个 `if`​ 不是嵌套判断，而是**连续过滤，相当于 and**

   >>>  **[i  for i in range(10)  if i%2==0 if i%3 == 0]
   >>> [0, 6]**
   >>>
   >>
   >
4. 需要一个**表达式**在**条件分支**下**取不同的值**,把条件判断放到**表达式部分,进行分支**

   三元表达式放在左侧表达式位置

   [i if i % 2 == 0 else -i for i in range(10)]

   [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

#### 生成器 generator

1. **列表元素按照算法计算，在循环中不断计算后续元素，称为生成器：generator,不必创建完整的 list，从而节省大量的空间**
2. **创建 generator**:把**列表生成式**的  **​`[]`​** ​**改成**  **​`()`​** ，就创建了一个 generator：

   >>> g = (x*x for x in range(5))
   >>> g
   >>> <generator object <genexpr> at 0x0000020397ED2330>
   >>>
   >>
   >
3. 通过 **​`next()`​**  ​函数获得 generator 的**下一个返回值**
4. **generator 保存**的是**算法,** 每次**调用** **​`next(g)`​** ​，就**计算**出 `g` ​的**下一个元素的值**，**没有更多的元素**时，抛出 **​`StopIteration`​** ​的错误
5. **使用** **​`for`​**​**循环迭代遍历，generator 也是可迭代对象**

   >>> g = (x*x for x in range(5))
   >>> for i in g:
   >>> ...     print(i)
   >>> ...
   >>> 0
   >>> 1
   >>> 4
   >>> 9
   >>> 16
   >>>
   >>
   >
6. **定义 generato**r 的**另一种方法**。函数定义中包含 **​`yield`​** ​关键字，这个函数就是一个 **generator 函数**，**调用**一个 **generator 函数**调用它**不会执行函数体**，将**返回一个 generator 生成器对象，**
7. **普通函数**是**顺序执行**，遇到 **​`return`​**​**语句**或者**最后一行函数语句**就**返回**
8. **generator 函数**，在每次**调用** **​`next()`​**  ​的时候**执行**，遇到 **​`yield`​**​**语句返回**，再次执行时从**上次返回**的 **​`yield`​**​**语句处继续执行**
9. **调用 generator 函数**会**创建**一个 **generator 对象**，**多次调用** generator 函数会**创建多个相互独立**的 **generator**

#### 迭代器

1. **可迭代对象：**​**​`Iterable`​**​：`list`​、`tuple`​、`dict`​、`set`​、`str`​，`generator`​（生成器，带 `yield` ​的 generator function）
2. **迭代器** **​`Iterator`​**​ ：可以被 **​`next()`​** ​**函数调用**并**不断返回下一个值**的**对象**称为**迭代器：**​**​`Iterator`​**
3. **生成器都是** **​`Iterator`​**​**对象**，但 **​`list`​**​ **、**​**​`dict`​**​ **、**​**​`str`​** ​虽然是 `Iterable`​，却**不是** **​`Iterator`​**
4. ​**​`iter()`​** ​**函数：** 把 `list`​、`dict`​、`str` ​等 `Iterable` ​变成 `Iterator`
5. ​**​`Iterator`​**​**对象**表示的是一个**数据流**，数据流**看做**是一个**有序序列，** 却**不能**提前**知道**序列的**长度**，**只能不断**通过 `next()` ​函数实现按需**计算**下一个数据，**​`Iterator`​** ​的**计算是惰性**的，**只有在需要返回下一个数据时它才会计算**
6. ​**​`Iterator`​**​**甚至**可以表示一个**无限大的数据流**，例如全体自然数。而使用 list 是永远不可能存储全体自然数的。
7. **所有生成器都是迭代器，但并非所有迭代器都是生成器**
8. **迭代器 (iterator)**   像一条**传送带**。物品从源头一个一个被推到你面前，你只能**取走当前的这一个**，取完它就过去了，传送带继续往前推下一个。你想回头看刚才那个？不好意思，传送带不会倒转，那个东西也**没有被保存在任何地方**。

## 五、函数式编程

**函数式编程**的一个**特点**就是，允许把**函数本身作为参数传入另一个函数**，还**允许返回一个函数**

#### 高阶函数

1. **变量可以指向函数，即函数名可以赋给变量，也可调用**

   >> f = abs
   >> f
   >> <built-in function abs>
   >> f(-1)
   >> 1
   >>
   >
2. **函数名**其实**就是**指向函数的**变量**
3. **把函数作为参数传入，这样的函数称为高阶函数**

   >>> def gao(x,y,f):
   >>> ...     return f(x)+f(y)
   >>> ...
   >>> gao(1,-2,abs)
   >>>
   >>
   >

#### map/reduce

1. ​**​`map`​**​ 是 Python 内置的**高阶函数**，它对**可迭代对象**中的**每个元素应用同一个函数**，返回一个**惰性求值的迭代器，"横向转换"（元素数量不变）**
2. **语法：map(function, iterable, ...)，**​**​`map`​**​ **对象只能遍历一次**，因为它就是迭代器本身，想象成传送带，单向

   >>> m = map(str,[1,2,3])
   >>> m
   >>> <map object at 0x000002008B3F3EE0>
   >>> list(m)
   >>> ['1', '2', '3']
   >>> type(m)
   >>> <class 'map'>
   >>> next(m)
   >>> Traceback (most recent call last):
   >>> File "<python-input-9>", line 1, in <module>
   >>> next(m)
   >>>
   >>> ~~~~^^^
   >>> StopIteration
   >>> list(m)
   >>> []
   >>> {: fold="1" heading-fold="1" id="20260601142621-1c9sa2p" updated="20260601142641"}
   >>>
   >>> ~~~~
   >>>
   >>
   >
3. **reduce 函数：**​`reduce`​ 是 化多为少"的函数——它把一个**可迭代对象**中的元素**逐个累积**，最终归约为一个**单一值，纵向折叠"（把序列折叠成一个结果）**
4. **reduce 语法：**​**​`function`​**​：一个接受**两个参数**的函数。第一个参数是累积值，第二个参数是序列中的当前元素，**​`iterable`​**​：可迭代对象，**​`initializer`​**（可选）：累积的初始值。不提供时，默认用序列的第一个元素

   from functools import reduce

   reduce(function, iterable[, initializer])

   >>> reduce(lambda sum,x:sum+x,[1,2,3,4,5])
   >>> 15
   >>>
   >>
   >
5. 函数式编程中经典的 **​`foldl`​**​ **（左折叠）** ——从左向右逐级收拢。它也解释了为什么 `reduce`​ 的回调函数必须接受两个参数：**一个代表左侧的累积成果，一个代表右边的新元素。**

   f

   /   \\

   f     4

   /   \\

   f     3

   /   \\

   1     2

   等价于: f(f(f(1, 2), 3), 4)

‍

#### filter

1. ​**​`filter`​**​ 是 Python 内置的**高阶函数**，它对**可迭代对象**中的**每个元素**执行一个"**判断函数**"，**只保留判断为 True 的元素**，返回一个**惰性迭代器**。它是数据流中的"筛子"。
2. **filter 语法：filter(function, iterable)**

   - ​**​`function`​**​​：一个接受**单个参数**、**返回布尔值**的**判断函数**。也可以是 **​`None`​**。
   - ​**​`iterable`​**：可迭代对象。
   - ​**返回值**​：一个 `filter` 对象（迭代器），惰性产出通过判断的元素。

     >>> f = filter(lambda x:x%2==1,[1,2,3,4,5,6,7,8,9])
     >>> f
     >>> <filter object at 0x000002008B420DF0>
     >>> for i in f:
     >>> ...     print(i)
     >>> ...
     >>> 1
     >>> 3
     >>> 5
     >>> 7
     >>> 9
     >>>
     >>
     >
3. ​**​`filter(None, iterable)`​** ​  **—— 快速剔除假值，剔除所有假值：0、空字符串、None、空列表等**

   list(filter(None, [1, 0, 'hello', '', None, [], [1, 2], False]))

   [1, 'hello', [1, 2]]

‍

#### sorted

1. ​**​`sorted`​**​  是 Python 内置的**排序函数**。它接收一个**可迭代对象**，返回一个**全新的、排好序的列表**，原数据毫发无损。
2. **语法：sorted(iterable, key=None, reverse=False)**

   - ​**​`iterable`​**：可迭代对象
   - ​**​`key`​**​​（可选）：一个**单参数函数**，为每个元素计算"**排序依据**"。默认 **​`None`​**​ 表示**直接比较元素本身**
   - ​**​`reverse`​**​​（可选）：`True`​ 为降序，默认 `False` 为升序
   - ​**返回值**​：一个​**新的列表**，包含所有元素并按指定顺序排列

     >>> sorted('python',key=None,reverse=False)
     >>> ['h', 'n', 'o', 'p', 't', 'y']
     >>>
     >>
     >

‍

#### <span data-type="text" style="color: var(--b3-font-color8);">*</span>返回函数

1. **返回函数**是指在**函数内**部**定义另一个函数**，**把函数作为结果返回**。

   >>> def outer():
   >>> ...     def inner():
   >>> ...         print('我是内部函数')
   >>> ...     return inner
   >>>
   >>> outer()
   >>> <function outer.<locals>.inner at 0x000001D5E5EA6480>
   >>> f = outer()
   >>> f()
   >>> 我是内部函数
   >>>
   >>
   >
2. **闭包 (Closure)：带记忆的内部函数** 当内部函数**引用了外部函数的变量**时，这个**内部函数**就成为了**闭包**。闭包不仅"记住"了自己的代码逻辑，还"记住"了它诞生时所在的**外部环境中的变量值**。
3. **把** **​`n`​**​ **连同** **内部函数 inner 一起打包保存下来**。这个被保存的变量环境被称为"**闭包捕获**"，**​`n`​**​ 就是闭包中的**自由变量**

   >>> def outer(n):
   >>> ...     def inner(x):
   >>> ...         return x*n
   >>> ...     return inner
   >>> ...
   >>> t1 = outer(3)
   >>> t2 = outer(5)
   >>>
   >>> print(t1(10))
   >>> 30
   >>> print(t2(10))
   >>> 50
   >>>
   >>
   >
4. ​ **​`__closure__`​**   属性查看闭包捕获了哪些变量

   >>> t1.__closure__
   >>> (<cell at 0x000001D5E5E93CD0: int object at 0x00007FF814B243E8>,)
   >>> t1.__closure__[0].cell_contents
   >>> 3
   >>>
   >>
   >
5. ​**​`nonlocal`​** ​用于在**嵌套函数内部**声明某个变量**不是本地的，而是来自外层（封闭作用域）的**，从而可以对该变量进行**重新赋值**
6. 如果一个**变量**在**函数内部**有**赋值语句**，编译器就**认定**它是**该函数**的**局部变量**，除非显式声明为 **​`global`​**​ **或** **​`nonlocal`​**
7. #### `nonlocal` 与 LEGB 的精确关系

   |层级|全称|声明关键字|说明|
   | ----| --------| ----------| -------------|
   |L|Local|—|当前函数内部|
   |**E**|**Enclosing**|**​`nonlocal`​**|**外层函数（可以多层）**|
   |G|Global|​`global`|模块顶层|
   |B|Built-in|—|Python 内置名|

   - **只读不用声明：**  如果只是读取外层变量的值，Python 自动沿 LEGB 链向上查找，不需要任何声明。
   - **赋值必须声明：**  一旦要对外层变量做​**重新赋值**​（`=`​、`+=`​、`-=`​ 等），就必须用 `nonlocal`​（E 层）或 `global`（G 层）告诉 Python 你指向的是哪一层的变量。
8. ||​`nonlocal`|​`global`|
   | ------------| -------------------------------------------| ----------------------|
   |查找起点|跳过 Local，从 Enclosing 第一层向外逐层搜索|直接定位 Global 层|
   |变量不存在时|抛​ **​`SyntaxError`​**（语法错误，定义时即报）|在 Global 层**创建新变量**|
   |设计语义|只操作已存在的封闭作用域变量|允许动态扩展模块级状态|

   ​**​`global`​**​ **会"无中生有"** ——即使 Global 层没有这个变量，`global x` 也会在模块命名空间中创建它。
   ​**​`nonlocal`​**​ **不会**——它要求外层必须已经存在这个变量，否则语法层面直接拒绝。这是两者设计哲学的根本差异。

‍

#### 匿名函数 lambda

1. **语法：lambda 参数 1, 参数 2, ... : 表达式**

   - ​`lambda`：关键字，标记这是一个匿名函数
   - 参数列表：和 `def`​ 的参数语法完全一致（位置参数、默认参数、`*args`​、`**kwargs` 都支持）
   - ​`:`​ 后面：一个**表达式**，它的值就是这个函数的返回值
   - ​`表达式`​：函数的返回值，**只能是一个表达式**，不能包含 `=`​ 赋值、`if`​ 块、`for` 循环等语句
2. ​`lambda`​ 本质上是一个**表达式，**​`lambda`​ 本质上是一个**表达式，lambda 可以**直接嵌在函数调用的参数里、列表元素里、甚至另一个表达式的中间

#### 装饰器

1. **装饰器就是一个接收函数、返回新函数的函数。**  它允许你在不修改原函数代码的前提下，**给函数增加额外的行为**

   >>> def log(func):  
   >>> ...     def wrapper(**args,**kw):...        
   >>> 		print(f'调用{func.__name__}({args},{kw})')...       
   >>> 		return func(** args,**kw)  
   >>> ...     return wrapper  
   >>> ...  
   >>> def add(a,b):  
   >>> ...     return a+b  
   >>> ...  
   >>> add = log(add)
   >>>
   >>> add(3,5)  
   >>> 调用 add((3, 5),{})  
   >>> 8
   >>>
   >>
   >
2. ​ **​`@log`​**​ **等价于** **​`add = log(add)`​** ，{__name__}获取函数名

   >>> def log(func):  
   >>> ...     def wrapper(**args,**kw):...*
   >>>
   >>> 		*print(f'调用{func.__name__}({args},{kw})')...*
   >>>
   >>> 		*return func(** args,**kw)  
   >>> ...     return wrapper  
   >>> ...  
   >>> @log  
   >>> ... def add(a,b):  
   >>> ...     return a+b  
   >>> ...  
   >>> add(3,4)  
   >>> 调用 add((3, 4),{})  
   >>> 7
   >>>
   >>
   >
3. **计时装饰器**

   >>> def metric(func):  
   >>> ...     def wrapper(**args,**kw):...*
   >>>
   >>> *start=time.time()...*
   >>>
   >>> *r=func(** args,**kw)  
   >>> ...         end=time.time()  
   >>> ...         t = end - start  
   >>> ...         print(f'{func.__name__}总计消耗{t}ms')  
   >>> ...         return r  
   >>> ...     return wrapper
   >>>
   >>>>>> @metric  
   >>>>>> ... def add(a,b):  
   >>>>>> ...     return a+b
   >>>>>>
   >>>>>> add(3242,42424)  
   >>>>>> add 总计消耗 1.1920928955078125e-06ms  
   >>>>>> 45666
   >>>>>>
   >>>>>
   >>>>
   >>>
   >>
   >
4. ​**​`functools.wraps`​**​ **：修复元数据，**​`add`​ 现在指向 `wrapper`​，所以 `__name__`​ 和 `__doc__`​ 都变成了 `wrapper` 的

   >>> def log(func):  
   >>> ...     def wrapper(*args,**kw):...         print(f'调用{func.__name__}({args},{kw})')...         return func(* args,**kw)  
   >>> ...     return wrapper  
   >>> ...  
   >>> @log  
   >>> ... def add(a,b):  
   >>> ...     return a+b  
   >>> ...  
   >>> add(4,5)  
   >>> 调用add((4, 5),{})  
   >>> 9  
   >>> print(add.__name__)  
   >>> wrapper  
   >>> print(add.__doc__)  
   >>> None
   >>>
   >>
   >
5. ​ **​`@wraps(func)`​** ​ 做了三件事：把 `func`​ 的 `__name__`​、`__doc__`​、`__module__`​ 等元数据原样复制到 `wrapper`​ 上。**写装饰器时一律加上**  **​`@wraps`​**​ **，这是一个不需要思考的规则。**   
   from functools import wraps

   def log(func):  
       @wraps(func)                    # 把 func 的元数据复制到 wrapper  
       def wrapper(*args, **kwargs):*         

           *print(f"调用 {func.__name__}")*

            *return func(* args, **kwargs)  
       return wrapper

   @log  
   def add(a, b):  
       """返回两数之和"""  
       return a + b

   print(add.__name__)      # add      ✅  
   print(add.__doc__)       # 返回两数之和 ✅
6. **带参数的装饰器：三层嵌套**

   >>> def log_with_level(level):  
   >>> ...     def decorator(func):  
   >>> ...         @wraps(func)  
   >>> ...         def wrapper(*args,**kw):...*
   >>>
   >>> 		*print(f'{level},{func.__name__}')...*
   >>>
   >>> 		 *return func(* args,**kw)  
   >>> ...         return wrapper  
   >>> ...     return decorator  
   >>> ...  
   >>> @log_with_level('debug')  
   >>> ... def add(a,b):  
   >>> ...     return a+b  
   >>> ...  
   >>> add(3,4)  
   >>> debug,add  
   >>> 7
   >>>
   >>
   >
7. 多个装饰器的**叠加顺序**  
     

   @decorator\_a

   @decorator\_b

   def func():

       pass  
   等同于

   func \= decorator\_a(decorator\_b(func))

‍

#### 偏函数 functools.partial

1. ​**​`int()`​** ​**函数**可以把**字符串转换为整数，默认转换为10进制，base参数指定转换进制**

   >>> int('12345',base=16)  
   >>> 74565  
   >>> int('12345',base=8)  
   >>> 5349  
   >>> int('12345')  
   >>> 12345
   >>>
   >>
   >
2. **partial 的本质：提前"锁死"一部分参数，接收一个函数和一些预先填入的参数，返回一个新函数，** 新函数被调用时，`partial` 把你事先填入的参数和调用时传入的参数合并，一起传给原函数。

   >>> from functools import partial  
   >>> def power(x,n):  
   >>> ...     return x**n  
   >>> ...  
   >>> square = partial(power,n=2)  
   >>> square(3)  
   >>> 9  
   >>>   
   >>>
   >>> square.func  
   >>> <function power at 0x000001B103176A20>  
   >>> square.args  
   >>> ()  
   >>> square.keywords  
   >>> {'n': 2}
   >>>
   >>
   >
3. 位置参数与关键字参数都能固定  
     

   固定位置参数

   square = partial(power, 2)        # 把第一个位置参数 base 固定为 2  
   square(3)                         # power(2, 3) → 8

   固定关键字参数

   square = partial(power, exponent=2)  
   square(3)                         # power(3, exponent=2) → 9

   同时固定

   double = partial(power, exponent=2, base=10)  
   double()                          # power(10, 2) → 100

‍

## 六、模块

.**py文件**就称之为一个**模块（Module）**   
**按目录来组织模块**的方法，称为**包（Package）**   
mycompany  
├─ __init__.py  
├─ abc.py  
└─ xyz.py  
每一个包目录下面都会有一个 **__init__.py的文件**，这个文件是**必须存在的**，否则，Python就把这个目录当成普通目录，而不是一个包。 **__init__.py可以是空文件，也可以有Python代码**，因为__init__.py**本身就是一个模块**，而它的模块名就是mycompany。

#### 使用模块

1. 任何模块代码的**第一个字符串**都被视为模块的**文档注释**
2. ​`__author__`变量把作者写进去
3. **import写法：**   
   **import 模块名   使用时 模块名.方法（）
   from 模块 import 名字   直接使用方法，导入的变量会覆盖本地变量
    import 模块 as 别名**
4. |​ **​`__name__`​** |直接运行时为`"__main__"`，被导入时为模块名|
   | ------| ----------------------------------|
5. 类似`_xxx`​和`__xxx`​这样的函数或变量就是**非公开的（private）**

## 七、面向对象编程

#### 类（Class）和实例（Instance）

1. **类是抽象模板，实例是具体实现对象**

   >>> class Student(object):  
   >>> ...     pass  
   >>> ...  
   >>> Student()  
   >>> <__main__.Student object at 0x0000017093B84C20>  
   >>> Student  
   >>> <class '__main__.Student'>  
   >>> class Student(object):  
   >>> ...     def __init__(self,name,score):  
   >>> ...         self.name = name  
   >>> ...         self.score = score  
   >>> ...  
   >>> bart = Student('losi',98)  
   >>> bart.name  
   >>> 'losi'  
   >>> bart.score  
   >>> 98
   >>>
   >>
   >
2. 定义类是通过**​`class`​**​**关键字**，**​`class`​**​**后面**紧接着是**类名**，类名通常是**大写开头**的单词，紧接着是 **​`(object)，keshenglue`​**​，表示该类是从**哪个类继承**下来的，如果没有合适的继承类，就使用`object`类，这是所有类最终都会继承的类。
3. **创建实例**是通过**类名+()** 实现的，可以自由地给一个**实例变量绑定属性**​`__init__`​方法的**第一个参数永远是**​**​`self`​**​，表示创建的实例本身，在`__init__`​方法内部，就可以把各种属性绑定到`self`​，因为`self`就指向创建的实例本身
4.  **__init__在创建对象时自动执行，初始化对象的初始状态**
5. **self代表调用者对象**
6. **实例属性和类属性，实例属性各存各自的值，类属性共享，类属性还可通过类名调用，d1.species   # 先在 d1 自己的空间里找 "species" → 没找到 → 去 Dog 类里找 → "犬科"**

   >>> class Dog:  
   >>> ...     species='犬科'  
   >>> ...     def __init__(self,name):  
   >>> ...         self.name = name  
   >>> ...  
   >>> d1 = Dog('来福')  
   >>> d2 = Dog('旺财')  
   >>> d1.name  
   >>> '来福'  
   >>> d2.name  
   >>> '旺财'  
   >>> d1.species  
   >>> '犬科'  
   >>> d2.species  
   >>> '犬科'  
   >>> Dog.species  
   >>> '犬科'
   >>>
   >>
   >
7. **数据封装：用命名约定区分"公共"和"内部"，单下划线** `_score`​ 的意思是： **"我是内部实现细节，通过公共方法操作我，别直接碰，但非强制约束**

   >>> class Student:  
   >>> ...     def __init__(self,name,score):  
   >>> ...         self.name = name  
   >>> ...         self._score = score  
   >>> ...     def set_score(self,value):  
   >>> ...         if not 0<=value<=100:  
   >>> ...             raise ValueError('成绩必须再0-100之间啊')  
   >>> ...         self._score = value  
   >>> ...     def get_score(self):  
   >>> ...         return self._score  
   >>> ...     def print_info(self):  
   >>> ...         print(f'{self.name},{self._score}')  
   >>> ...     def ispass(self):  
   >>> ...         return self._score>60  
   >>> ...
   >>>
   >>> d1 = Student('lasoi',88)  
   >>> d1  
   >>> <__main__.Student object at 0x0000026DF1F5CAD0>  
   >>> d1.get_score()  
   >>> 88  
   >>> d1._score  
   >>> 88  
   >>> d1.set_score(77)  
   >>> d1.get_score()  
   >>> 77  
   >>> d1.get_score(909)  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-35>", line 1, in <module>  
   >>>
   >>
   >

#### 访问限制

1. 让**内部属性不被外部访问**，可以把属性的名称**前加上两个下划线**​ **​`__`​** ​实例的变量名如果以`__`​开头，就变成了一个**私有变量（private**），无法从外部访问`实例变量.__name`​和`实例变量.__score`

   >>> class Student:  
   >>> ...     def __init__(self,name,score):  
   >>> ...         self.__name = name  
   >>> ...         self.__score = score  
   >>> ...     def print_info(self):  
   >>> ...         print(f'{self.__name},{self.__score}')  
   >>> ...  
   >>> d1 = Student('kimi',89)  
   >>> d1.print_info()  
   >>> kimi,89  
   >>> d1.__name  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-39>", line 1, in <module>  
   >>> d1.__name  
   >>> AttributeError: 'Student' object has no attribute '__name'
   >>>
   >>> ‍
   >>>
   >>
   >
2. **外部代码获取内部属性（私有变量），请提供get/set方法**
3. 变量名类似`__xxx__`​的，也就是以双下划线开头，并且以双下划线结尾的，是**特殊变量**，特殊变量是可以直接访问的
4. **私有变量也可以从外部访问，但不要这么做，通过_类名__私有变量名**

   >>> d1._Student__name  
   >>> 'kimi'
   >>>
   >>
   >
5. 表面上看，外部代码“成功”地设置了`__gender`​变量，但实际上这个`__gender`​变量和class内部的`__gender`​变量*不是*一个变量！内部的`__gender`​变量已经被Python解释器自动改成了`_Student__gender`​，而外部代码给`bart`​新增了一个`__gender`变量

   >>> class Student(object):  
   >>> ...     def __init__(self, name, gender):  
   >>> ...         self.name = name  
   >>> ...         self.__gender = gender  
   >>> ...     def get_gender(self):  
   >>> ...         return self.__gender  
   >>> ...     def set_gender(self,value):  
   >>> ...         self.__gender = value
   >>>
   >>
   >

   >>> bart.get_gender()  
   >>> 'female'  
   >>> bart.__gender = 'new gender'  
   >>> bart.__gender  
   >>> 'new gender'  
   >>> bart.get_gender()  
   >>> 'female'
   >>>
   >>
   >

#### 继承和多态

1. **定义一个class**的时候，可以从某个现有的class**继承**，新的class称为**子类**（Subclass），而被继承的class称为**基类、父类或超类**（Base class、Super class）
2. **子类和父类都存在相同的**​**​`run()`​** ​**方法**时，我们说，**子类的**​**​`run()`​** ​**覆盖了父类的**​**​`run()`​** ​，在代码运行的时候，总是会调用子类的`run()`

   >>> class Animal:  
   >>> ...     def run(self):  
   >>> ...         print('Animal is running...')
   >>>
   >>>> class Dog(Animal):  
   >>>> ...     def run(self):  
   >>>> ...         print('dog is running...')  
   >>>> ...     def eat(self):  
   >>>> ...         print('dog is eating...')  
   >>>> ...  
   >>>> dog1 = Dog()  
   >>>> dog1.eat()  
   >>>> dog is eating...  
   >>>> dog1.run()  
   >>>> dog is running...
   >>>>
   >>>
   >>
   >
3. **多态：定义class就是定义数据类型，和自带的数据类型（list,tuple...）一样**
4. **在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类**

   >>> isinstance(dog1,Animal)  
   >>> True  
   >>>   
   >>> isinstance(dog1,Dog)  
   >>> True
   >>>
   >>
   >
5. **多态开闭原则：** 当我们需要传入`Dog`​、`Cat`​、`Tortoise`​……时，我们只需要接收`Animal`​类型就可以了，因为`Dog`​、`Cat`​、`Tortoise`​……都是`Animal`​类型，然后，按照`Animal`​类型进行操作即可，多态真正的威力：调用方只管调用，不管细节，而当我们新增一种`Animal`​的子类时，只要确保`run()`方法编写正确，不用管原来的代码是如何调用的

   对扩展开放：允许新增`Animal`子类；

   对修改封闭：不需要修改依赖`Animal`​类型的`run_twice()`等函数。

   >>> def run_twice(animal):  
   >>> ...     animal.run()  
   >>> ...     animal.run()  
   >>> ...  
   >>> ...  
   >>> run_twice(Animal())  
   >>> Animal is running...  
   >>> Animal is running...  
   >>> run_twice(Dog())  
   >>> dog is running...  
   >>> dog is running...  
   >>> class Tortoise(Animal):  
   >>> ...     def run(self):  
   >>> ...         print('t is running slowly...')  
   >>> ...  
   >>> run_twice(Tortoise())  
   >>> t is running slowly...  
   >>> t is running slowly...
   >>>
   >>
   >
6. **对于Python这样的动态语言来说，则不一定需要传入**​**​`Animal`​**​**类型。我们只需要保证传入的对象有一个**​**​`run()`​** ​**方法就可以了：这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。**

   >>> class Timer:  
   >>> ...     def run(self):  
   >>> ...         print('tttt')  
   >>> ...  
   >>> run_twice(Timer())  
   >>> tttt  
   >>> tttt
   >>>
   >>
   >
7. **方法查找路径**：查找路径叫 **MRO**（Method Resolution Order，方法解析顺序）

   >>> Dog.__mro__  
   >>> (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
   >>>
   >>
   >
8. **super():返回当前类在 MRO 链上的下一个类,子类调用父类方法**

‍

#### 获取对象信息

1. 判断对象类型，使用**​`type()`​** ​**函数**：

   >>> type(1223) == int  
   >>> True  
   >>> type('aaa') == str  
   >>> True
   >>>
   >>
   >
2. **判断一个对象是否是函数**怎么办？可以使用**​`types`​**​**模块中定义的常量**

   >>> import types  
   >>> def func():  
   >>> ...     pass  
   >>> ...  
   >>> type(func) == types.FunctionType  
   >>> True  
   >>> type(abs) == types.BuiltinFunctionType  
   >>> True  
   >>> type(lambda x : x**x) == types.LambdaType  
   >>> True  
   >>> type((x for x in range(4))) == types.GeneratorType  
   >>> True
   >>>
   >>
   >
3. **判断一个变量是否是某些类型中的一种，** 优先使用`isinstance()`判断类型

   >>> isinstance([1,2,3],(list,tuple))  
   >>> True
   >>>
   >>
   >
4. **dir():获得一个对象的所有属性和方法，可以使用**​**​`dir()`​** ​**函数,返回一个包含字符串的list**
5. ​**​`getattr()`​** ​ **、**​**​`setattr()`​** ​**以及**​**​`hasattr()`​** ，我们可以直接操作一个对象的状态

   >>> class MyObject(object):  
   >>> ...     def __init__(self):  
   >>> ...         self.x = 9  
   >>> ...     def power(self):  
   >>> ...         return self.x * self.x  
   >>> ...  
   >>> o = MyObject()
   >>>
   >>> hasattr(o,'x')  
   >>> True  
   >>> setattr(o,'x',7)  
   >>> getattr(o,'x)  
   >>> File "<python-input-109>", line 1
   >>>
   >>> getattr(o,'x')  
   >>> 7  
   >>> getattr(o,'y',222)  
   >>> 222  
   >>> hasattr(o,'power')  
   >>> True  
   >>> fn = getattr(o,'power')  
   >>> fn()  
   >>> 49
   >>>
   >>
   >

## 八、面向对象高级编程

#### __**slot__**

1. **每个 类，实例都有一个字典属性__dict__,每次添加属性，字典会记录，字典本身比较占内存**  
   class Dog:  
       def __init__(self, name, age):  
           self.name = name  
           self.age = age

   d = Dog("旺财", 3)  
   print(d.__dict__)    # {'name': '旺财', 'age': 3}
2.  **__slots__ = ("属性1", "属性2", ...)注意是元组，小心单个元素需加，号，用紧凑数组替代**​ **​`__dict__`​** ​ **，限定实例可有的属性**  
   class Dog:  
       **slots** = ("name", "age")      # 只允许这两个属性

       def __init__(self, name, age):  
           self.name = name  
           self.age = age  
     

   d = Dog("旺财", 3)  
   print(d.name)    # 旺财  
   print(d.age)     # 3

   第一个副作用：不能添加 **slots** 之外的属性

   d.color = "黄色"           # AttributeError: 'Dog' object has no attribute 'color'

   第二个副作用：没有 **dict**

   print(hasattr(d, "__dict__"))    # False
3. ​ **​`__slots__`​** ​ **只影响定义它的那个类，不会自动（注意自动）传给子类（在子类中没有定义__solts__的前提下），子类没有__slots__,分配__dict__,**​`name`​ 存于父类的 slot 中，`age`​ 存于子类的 `__dict__`​ 中——**同一个实例，属性存在两个地方**

   >>> class Animal:  
   >>> ...     def __init__(self,name):  
   >>> ...         self.name = name  
   >>> ...     __slots__=('name',)  
   >>> ...  
   >>> class Dog(Animal):  
   >>> ...     pass  
   >>> ...
   >>>
   >>> d = Dog('旺财')  
   >>> d.color = 'yellow'  
   >>> d.__dict__  
   >>> {'color': 'yellow'}  
   >>> d.name  
   >>> '旺财'  
   >>> d.__slots__  
   >>> ('name',)
   >>>
   >>
   >
4. **子类自己也定义**  **​`__slots__`​** ​,**最终允许的属性 = 所有祖先类的**  **​`__slots__`​** ​ **的并集**。**每个**  **​`__slots__`​** ​ **只声明该类新增的属性，不重复声明父类已有的。**

   >>> class Animal:  
   >>> ...     **slots** = ('name',)  
   >>> ...     def __init__(self,name):  
   >>> ...         self.name = name  
   >>> ...  
   >>> class Dog(Animal):  
   >>> ...     **slots** = ('breed',)  
   >>> ...     def __init__(self,name,breed):  
   >>> ...         self.breed = breed  
   >>> ...         super().__init__(name)  
   >>> ...  
   >>> d = Dog('旺财','金毛')
   >>>
   >>> hasattr(d,'__dict__')  
   >>> False  
   >>> d.__slots__  
   >>> ('breed',)  
   >>> d.color = 'green'  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-63>", line 1, in <module>  
   >>> d.color = 'green'  
   >>> ^^^^^^^  
   >>> AttributeError: 'Dog' object has no attribute 'color' and no **dict** for setting new attributes
   >>>
   >>
   >
5. **多重继承中的**  **​`__slots__`​** ​，**如果一个类有多个定义**  **​`__slots__`​** ​ **的父类，这个类自己的**  **​`__slots__`​** ​ **不能同时继承两个非空的 slot 集合。**  Python 会报 `TypeError`​，对于多重继承场景，要么所有父类中最多只有一个有非空 `__slots__`​，要么子类自己定义 `__slots__`（即使是空元组）。

   class A:  
       **slots** = ("x",)

   class B:  
       **slots** = ("y",)

   ❌ 不行——Python 不知道该用哪种 slot 布局

   class C(A, B):  
       pass

   TypeError: multiple bases have instance lay-out conflict

   ✅ 解决办法：C 自己定义 **slots**

   class C(A, B):  
       **slots** = ()
6. **给**​**​`class`​**​**绑定方法后，所有实例均可调用**

   >>> def set_score(self, score):  
   >>> ...     self.score = score  
   >>> ...  
   >>> Student.set_score = set_score
   >>>
   >>
   >

‍

#### @property

1. ​ **​`@property`​**​**装饰器就是负责把一个方法伪装成属性调用，简化方法调用，简化方法命名**
2. **@<property名>.setter，**​ **​`@property`​**​ **作为 getter，加上 setter：可读可写，带校验**

   >>> class Student:  
   >>> ...     @property  
   >>> ...     def score(self):  
   >>> ...         return self._score  
   >>> ...     @score.setter  
   >>> ...     def score(self,value):  
   >>> ...         if not isinstance(value,int):  
   >>> ...             raise ValueError('分数必须是整形')  
   >>> ...         if value>100 or value<0:  
   >>> ...             raise ValueError('分数输入范围有误')  
   >>> ...         self._score = value  
   >>> ...  
   >>> s = Student()  
   >>> s.score = 68  
   >>> s.score  
   >>> 68  
   >>> s.score = 999  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-76>", line 1, in <module>  
   >>> s.score = 999  
   >>> ^^^^^^^  
   >>> File "<python-input-72>", line 10, in score  
   >>> raise ValueError('分数输入范围有误')  
   >>> ValueError: 分数输入范围有误
   >>>
   >>
   >
3. **加上 deleter：控制删除行为**
4. |**只读属性**|只写`@property`​，不写`@xxx.setter`|
   | --| ----------------|

#### 多重继承

1. **多重继承就是一个子类同时继承多个父类**

   >>> class Flyable:  
   >>> ...      def fly(self):  
   >>> ...           print('我能飞')  
   >>> ...
   >>>
   >>> class Swimmable:  
   >>> ...      def swim(self):  
   >>> ...           print('我能游泳')  
   >>> ...  
   >>>   
   >>> class Duck(Flyable,Swimmable):  
   >>> ...      def quack(self):  
   >>> ...           print('嘎嘎')  
   >>> ...  
   >>> d = Duck()  
   >>> d.fly()  
   >>> 我能飞  
   >>> d.swim()  
   >>> 我能游泳  
   >>> d.quack()  
   >>> 嘎嘎
   >>>
   >>
   >
2. **方法查找顺序：MRO,多个父类有同名方法,根据子类中父类的先后顺序寻找，找到一个就停止，两个方法__mro__,mro(),每个类在 MRO 中只出现一次,不会因为两条路径而重复出现**

   >>> class A:  
   >>> ...      def greet(self):  
   >>> ...           print('a')  
   >>> ...  
   >>> class B:  
   >>> ...      def greet(self):  
   >>> ...           print('b')  
   >>> ...  
   >>> class C(A,B):  
   >>> ...      pass  
   >>> ...  
   >>> c = C()  
   >>> c.greet()  
   >>> a  
   >>> C.__mro__  
   >>> (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)  
   >>> C.mro()  
   >>> [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
   >>>
   >>
   >
3. **多重继承中，**​**​`super()`​** ​ **的行为发生了根本变化：它不再指向某一个特定的父类，而是按照 MRO 顺序，返回 MRO 链上的下一个类。**

   >>> class Animal:  
   >>> ...     def speak(self):  
   >>> ...         print("Animal.speak 被调用")  
   >>> ...  
   >>> ... class LandAnimal(Animal):  
   >>> ...     def speak(self):  
   >>> ...         print("LandAnimal.speak 开始")  
   >>> ...         super().speak()                    # 不是直接调 Animal！  
   >>> ...         print("LandAnimal.speak 结束")  
   >>> ...  
   >>> ... class WaterAnimal(Animal):  
   >>> ...     def speak(self):  
   >>> ...         print("WaterAnimal.speak 开始")  
   >>> ...         super().speak()  
   >>> ...         print("WaterAnimal.speak 结束")  
   >>> ...  
   >>> ... class Frog(LandAnimal, WaterAnimal):  
   >>> ...     def speak(self):  
   >>> ...         print("Frog.speak 开始")  
   >>> ...         super().speak()  
   >>> ...         print("Frog.speak 结束")  
   >>> ...  
   >>> f = Frog()  
   >>> ... f.speak()  
   >>> ...  
   >>> Frog.speak 开始  
   >>> LandAnimal.speak 开始  
   >>> WaterAnimal.speak 开始  
   >>> Animal.speak 被调用  
   >>> WaterAnimal.speak 结束  
   >>> LandAnimal.speak 结束  
   >>> Frog.speak 结束  
   >>> Frog.mro()  
   >>> [<class '__main__.Frog'>, <class '__main__.LandAnimal'>, <class '__main__.WaterAnimal'>, <class '__main__.Animal'>, <class 'object'>]
   >>>
   >>
   >
4. **C3 线性化：MRO 如何计算**

   - ​**子类优先于父类**：子类一定排在所有父类前面
   - ​**父类保持定义顺序**​：`class Child(A, B)`​ 中，`A`​ 和它的祖先一定排在 `B` 和它的祖先前面
5. **Mixin(混入) 模式：多重继承的最佳实践，Mixin 是一个只提供额外功能、不设计为单独实例化，只提供方法，不为自己实例化，即插即用，类似接口**
6. **Mixin 的命名习惯**：类名末尾常加 `Mixin`​ 后缀——`LoggerMixin`​、`SerializeMixin`​、`AuthMixin`

#### *特殊用途函数

1. **__str__:**​**​`print()`​** ​ **一个对象时先找**  **​`__str__`​** ​ **，没有就找**  **​`__repr__`​** ​ **，再没有就用默认的内存地址格式,** 没有 `__str__`​ 时，输出的是**类名 + 内存地址**,**至少写__repr__**   
   直接显示变量调用的不是`__str__()`​，而是`__repr__()`​，两者的区别是`__str__()`​返回用户看到的字符串，而`__repr__()`返回程序开发者看到的字符串

   >>> class Student:  
   >>> ...      def __init__(self,name):  
   >>> ...           self.name = name  
   >>> ...  
   >>> Student('lisi')  
   >>> <__main__.Student object at 0x000001A2B80ED010>  
   >>> class Student:  
   >>> ...      def __init__(self,name):  
   >>> ...           self.name = name  
   >>> ...      def __str__(self):  
   >>> ...           return 'Student object name:%s' % self.name  
   >>> ...      __**repr__**  = __**str__**   
   >>> ...  
   >>> Student('lisi')  
   >>> Student object name:lisi  
   >>> s = Student('wangwu')  
   >>> s  
   >>> Student object name:wangwu
   >>>
   >>
   >
2.  **__iter__：** 如果一个类想被用于`for ... in`​循环，类似list或tuple那样，就必须实现一个`__iter__()`​方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的`__next__()`​方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环。
3. ​ **​`__getitem__`​** ​ **：让对象支持方括号索引，**​ **​`__getitem__`​** ​ **在每次你用** **​`obj[key]`​** ​ **时被调用。Python 把方括号里的内容原样传给你：**

   >>> class MyList:  
   >>> ...     def __init__(self,data):  
   >>> ...         self._data = list(data)  
   >>> ...     def __getitem__(self,index):  
   >>> ...         print(f'__getitem__被调用，index= {index}')  
   >>> ...         return self._data[index]  
   >>> ...  
   >>> ml = MyList([10,20,30,40])  
   >>> ml[2]  
   >>> __getitem__被调用，index= 2  
   >>> 30
   >>>
   >>
   >
4. ​ **​`__getitem__`​** ​ **：当你写** **​`obj[1:3]`​** ​ **时，Python 不是传一个整数，而是传一个** **​`slice`​**​ **对象，**​`slice`​ 对象有三个属性：`start`​、`stop`​、`step`

   >>> class MyList:  
   >>> ...     def __init__(self,data):  
   >>> ...         self._data = list(data)  
   >>> ...     def __getitem__(self,index):  
   >>> ...         if isinstance(index,slice):  
   >>> ...             print(f'切片start={index.start},stop={index.stop},step={index.step}')  
   >>> ...             return self._data[index]  
   >>> ...         else:  
   >>> ...             print(f'索引，index= {index}')  
   >>> ...             return self._data[index]  
   >>> ...  
   >>> ml = MyList([10,20,30,40])  
   >>> ml[1:3]  
   >>> 切片start=1,stop=3,step=None  
   >>> [20, 30]
   >>>
   >>
   >
5. ​`__getattr__`​：属性查找失败的兜底， **​`__getattr__`​** ​ **是最后一道防线。**  属性查找的完整路径

   1. 在实例的 **dict** 中查找
   2. 在类及其父类的 **dict** 中查找（包括描述符、方法）
   3. 全部失败 → 调用 __getattr__(self, name)
   4. 如果连 **getattr** 都没有 → 抛 AttributeError

      >>> class Config:  
      >>> ...     def __init__(self):  
      >>> ...         self.name = 'lisi'  
      >>> ...  
      >>> class Config:  
      >>> ...     def __init__(self):  
      >>> ...         self.name = 'lisi'  
      >>> ...     def __getattr__(self,name):  
      >>> ...         return name  
      >>> ...  
      >>> ...  
      >>> c = Config()  
      >>> c.name  
      >>> 'lisi'  
      >>> c.aa  
      >>> 'aa'
      >>>
      >>
      >
6. ​ **​`__call__`​** ​ **：让实例像函数一样被调用，实例名（）调用，** 实例加括号，触发 \_\_call\_\_

   >>> class Multiplier:  
   >>> ...     def __init__(self,factor):  
   >>> ...         self.factor = factor  
   >>> ...     def __call__(self,x):  
   >>> ...         return x*self.factor  
   >>> ...  
   >>> d  = Multiplier(2)  
   >>> d(5)  
   >>> 10
   >>>
   >>
   >
7. ​ **​`__call__`​** ​ **的本质：带状态的函数**

   普通函数没有记忆——每次调用都是独立、无状态的。但 `__call__` 的实例可以通过实例属性保留配置和历史：
8. **判断对象是否可以调用**，`callable()`​ 内置函数检查对象是否定义了 `__call__` 方法（或者是函数/方法/类等天然可调用的对象）。

   >>> callable(print)  
   >>> True  
   >>> callable(Multiplier)  
   >>> True  
   >>> callable('sss')  
   >>> False
   >>>
   >>
   >

‍

#### 枚举类

1. **给一组有限、固定的值起上有意义的名字**

   >>> from enum import Enum  
   >>> class OrderStatus(Enum):  
   >>> ...     PENDING = 'pending'  
   >>> ...     PAID = 'paid'  
   >>> ...     SHIPPED = 'shipped'  
   >>> ...     COMPLETED = 'completed'  
   >>> ...     CANCELLED = 'canceled'  
   >>> ...  
   >>> current = OrderStatus.PENDING  
   >>> current  
   >>> <OrderStatus.PENDING: 'pending'>  
   >>> print(current)  
   >>> OrderStatus.PENDING  
   >>> print(current.name)  
   >>> PENDING  
   >>> print(current.value)  
   >>> pending  
   >>> s = OrderStatus('paid')  
   >>> s  
   >>> <OrderStatus.PAID: 'paid'>  
   >>> print(s)  
   >>> OrderStatus.PAID
   >>>
   >>
   >
2. **枚举类的保护点：**   
   **值唯一**，两个枚举成员不能有相同的值（除非用 `@verify(UNIQUE)`​ 明确不要求唯一，或者用 `Flag`​ 允许重叠）  
   **类型安全**：不同类型的枚举即使值相同，结果比较也不同，  
   **不可变**：枚举成员一旦赋值不可改变，真正意义上的常量集合

   >>> class Color(Enum):  
   >>> ...     RED = '1'  
   >>> ...     GREEN = '2'  
   >>> ...  
   >>> class Direction(Enum):  
   >>> ...     UP = '1'  
   >>> ...     DOWN = '2'  
   >>> ...  
   >>> print(Color.RED==Direction.UP)FalseColor.RED==Direction.UP  
   >>> False  
   >>>   
   >>>   
   >>>
   >>> Color.RED='2'  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-41>", line 1, in <module>  
   >>> Color.RED='2'  
   >>> ^^^^^^^^^  
   >>> File "D:\anaconda\Lib\enum.py", line 839, in **setattr**  
   >>> raise AttributeError('cannot reassign member %r' % (name, ))  
   >>> AttributeError: cannot reassign member 'RED'
   >>>
   >>
   >
3. **枚举成员的属性:获取枚举成员的名字（字符串），值，__str__返回类名.成员名，__repe__返回详细信息**

   >>> s = Color.RED  
   >>> print(s)  
   >>> Color.RED  
   >>> print(s.name)  
   >>> RED  
   >>> print(s.value)  
   >>> 1  
   >>> print(repr(s))  
   >>> <Color.RED: '1'>
   >>>
   >>
   >
4. **遍历枚举成员使用for..in..,获取枚举成员字典使用__members__,**​ **​`__members__`​** ​ **是一个有序的只读字典，映射成员名到成员对象。当需要按名字查找成员时，**​**​`OrderStatus.__members__["PENDING"]`​** ​ **比** **​`OrderStatus("pending")`​** ​ **更直接。**

   >>> for s in Color:  
   >>> ...     print(s.name)  
   >>> ...  
   >>> RED  
   >>> GREEN  
   >>> Color.__members__  
   >>> mappingproxy({'RED': <Color.RED: '1'>, 'GREEN': <Color.GREEN: '2'>})  
   >>> Color.__members__['RED']  
   >>> <Color.RED: '1'>
   >>>
   >>
   >
5. **自动赋值：**​**​`auto()`​** ​,`auto()`​ 会自动生成递增的整数值。你想给自定义生成逻辑的话，可以重写 `_generate_next_value_`：

   >>> from enum import Enum,auto  
   >>> class Color(Enum):  
   >>> ...     RED = auto()  
   >>> ...     GREEN = auto()  
   >>> ...     YELLOW = auto()  
   >>> ...  
   >>> for i in Color:  
   >>> ...     print(i.value)  
   >>> ...  
   >>> 1  
   >>> 2  
   >>> 3  
   >>>   
   >>> class OrderStatus(Enum):  
   >>> ...     def _generate_next_value_(name, start, count, last_values):  
   >>> ...         return name.lower()         # 用成员名的小写作为值  
   >>> ...  
   >>> ...     PENDING = auto()       # 值为 'pending'  
   >>> ...     PAID = auto()          # 值为 'paid'  
   >>> ...
   >>>
   >>> for i in OrderStatus:  
   >>> ...     print(i.value)  
   >>> ...  
   >>> pending  
   >>> paid
   >>>
   >>
   >
6. **枚举的比较规则，is或=都可，偏向于is,枚举成员在定义时就是单例——**​**​`OrderStatus.PENDING`​**​ **在程序的任何地方都是同一个对象,不能比较大小，集成IntEnum可以比较大小**
7. **Flag：标志枚举（位掩码）** 当枚举值需要**组合使用**时

   >>> from enum import Flag,auto  
   >>> class Permission(Flag):  
   >>> ...     READ = auto()  
   >>> ...     WRITE = auto()  
   >>> ...     EXECUTE = auto()  
   >>> ...     ADMIN = READ|WRITE|EXECUTE  
   >>> ...  
   >>> Permission.__members__  
   >>> mappingproxy({'READ': <Permission.READ: 1>, 'WRITE': <Permission.WRITE: 2>, 'EXECUTE': <Permission.EXECUTE: 4>, 'ADMIN': <Permission.ADMIN: 7>})
   >>>
   >>> user_perm = Permission.READ|Permission.WRITE  
   >>> print(user_perm)  
   >>> Permission.READ|WRITE  
   >>>   
   >>> print(Permission.READ in user_perm)                  in 操作符检查是否包含某个权限  
   >>> True  
   >>> user_perm |=Permission.EXECUTE              添加执行权限  
   >>> print(user_perm)  
   >>> Permission.ADMIN  
   >>> user_perm ^=Permission.WRITE                 切换写权限（有就移除，没有就添加）  
   >>> print(user_perm)  
   >>> Permission.READ|EXECUTE  
   >>> user_perm &= ~Permission.READ              移除读权限  
   >>> print(user_perm)  
   >>> Permission.EXECUTE
   >>>
   >>
   >
8. ​`Flag`​ 和 `Enum` 的区别：

   ||​`Enum`|​`Flag`|
   | --| --------------------| --------------------------------------------|
   |**成员值**|任意|必须是 2 的幂（auto() 自动保证）|
   |**组合**|不允许（`RED \| GREEN`无意义）|允许（`READ \| WRITE`是新成员）|
   |**成员检查**|​`==`|​`in`|
   |**去重**|值必须唯一|允许多个组合产生同一数值（通过`@verify(UNIQUE)`要求唯一）|
9. ​ **​`@unique`​**​ **装饰器，如果你不允许枚举中出现重复的值，加上**  **​`@unique`​**​ **：**​`@unique`​ 在类定义完成时检查所有值是否唯一。如果没有 `@unique`​，`BLUE`​ 会静默地成为 `GREEN`​ 的别名（`Color.BLUE is Color.GREEN`​ 为 `True`），这通常是 bug 的来源。

   >>> from enum import Enum,unique  
   >>> @unique  
   >>> ... class Color(Enum):  
   >>> ...     RED = '1'  
   >>> ...     GREEN = '1'  
   >>> ...  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-77>", line 1, in <module>  
   >>> @unique  
   >>> ^^^^^^  
   >>> File "D:\anaconda\Lib\enum.py", line 1668, in unique  
   >>> raise ValueError('duplicate values found in %r: %s' %  
   >>> (enumeration, alias_details))  
   >>> ValueError: duplicate values found in <enum 'Color'>: GREEN -> RED  
   >>> class Color(Enum):  
   >>> ...     RED = '1'  
   >>> ...     GREEN = '1'  
   >>> ...  
   >>> Color.RED is Color.GREEN  
   >>> True
   >>>
   >>
   >

#### 元类

1. ​**​`type`​**​ **就是 Python 内置的元类，它是所有类的默认元类，用来动态创建类**
2. ​**​`type()`​** ​**函数可以查看一个类型或变量的类型，**​**​`type()`​** ​**函数既可以返回一个对象的类型，又可以动态创建一个新类,**​**​`class`​**​ **关键字不过是** **​`type()`​** ​ **的语法糖,** Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用`type()`函数创建出class
3. **要创建一个class对象，**​**​`type()`​** ​**函数依次传入3个参数：**

   1. class的名称；
   2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
   3. class的方法名称与函数绑定，这里我们把函数`fn`​绑定到方法名`hello`上。

      >>> def fn(self,name = 'lisi'):  
      >>> ...     print('hello,%s' % name)  
      >>> ...  
      >>>   
      >>> Hello = type('Hello',(object,),dict(hello = fn))  
      >>> h = Hello()  
      >>> h.hello()  
      >>> hello,lisi  
      >>> type(Hello)  
      >>> <class 'type'>  
      >>> type(h)  
      >>> <class '__main__.Hello'>
      >>>
      >>
      >

‍

## 九、错误、调试和测试

#### 错误处理

1. **try语法**  
   try:  
       # 尝试执行的代码块  
       # 这里放置可能引发异常的代码  
       ...  
   except [ExceptionType [as alias]]:  
       # 异常处理代码块  
       # 当 try 块中发生指定类型的异常时，执行此块  
       ...  
   else:  
       # 可选：当 try 块中没有发生异常时执行  
       ...  
   finally:  
       # 可选：无论是否发生异常，最终都会执行的代码块  
       # 常用于清理资源（如关闭文件、网络连接）

   >>> try:  
   >>> ...     print('try...')  
   >>> ...     r = 10/int('2')  
   >>> ...     print('result:',r)  
   >>> ... except ValueError as e:  
   >>> ...     print('ValueError:',e)  
   >>> ... except ZeroDivisionError as e:  
   >>> ...     print('ZeroDivisionError:',e)  
   >>> ... else:  
   >>> ...     print('no error')  
   >>> ... finally:  
   >>> ...     print('finally...')  
   >>> ... print('end')  
   >>> ...  
   >>> try...  
   >>> result: 5.0  
   >>> no error  
   >>> finally...  
   >>> end
   >>>
   >>
   >
2. **跨层捕获**：异常可以在调用栈的任意层级被捕获。你不需要在每一层都写 `try...except`，只需要在能够恰当处理错误的地方捕获即可。

   >>> def foo(s):  
   >>> ...     return 10/int(s)  
   >>> ...  
   >>> def bar(s):  
   >>> ...     return foo(s)*2  
   >>> ...  
   >>> def main():  
   >>> ...     try:  
   >>> ...         bar('0')  
   >>> ...     except Exception as e:  
   >>> ...         print(e)  
   >>> ...     finally:  
   >>> ...         print('final')  
   >>> ...  
   >>> main()  
   >>> division by zero  
   >>> final
   >>>
   >>
   >
3. **异常是 class，存在继承关系，若父类异常在前，子类异常在后，异常被父类捕获后，子类不会触发**
4. **Python 所有内置异常都继承自** **​`BaseException`​**​，捕获异常时尽量指定具体类型，避免使用裸 `except:`​**使用** **​`except Exception:`​** ​ **可以捕获大多数程序层面的异常**，但不会捕获 `SystemExit`​ 或 `KeyboardInterrupt`
5. **记录错误：**​**​`logging`​**​ **模块，捕获了错误之后，如果想让程序继续运行，同时又保留错误的完整信息用于排查，应该使用** **​`logging`​**​ **而非** **​`print`​**​，通过配置 `logging`，还可以将错误输出到文件、设置日志级别等

   >>> def main():  
   >>> ...     try:  
   >>> ...         r = 10/0  
   >>> ...     except Exception as e:  
   >>> ...         logging.exception(e)  
   >>> ... main()  
   >>> ... print('end')  
   >>> ...  
   >>> ERROR:root:division by zero  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-13>", line 3, in main  
   >>> r = 10/0  
   >>> ~~^~  
   >>> ZeroDivisionError: division by zero  
   >>> end
   >>>
   >>
   >
6. **主动抛出错误：**​**​`raise`​**​，**​`raise`​**​ **来中断当前流程，并将错误信息传递给上层调用者，** Python 会立即中断当前函数的执行，异常沿调用栈向上传播，直到被某个 `try...except` 捕获，或到达顶层使程序退出
7. 在 `except`​ 块中重新 `raise`​，**​`raise`​**​ **不带参数时**，它会将当前被捕获的异常**原样重新抛出**，往上抛

‍

#### 调试

1. ​`assert`​ —— 断言，`assert`​ 的意思是：表达式 `n != 0`​ 必须为 `True`​。如果为 `False`​，立即抛出 `AssertionError`：

   >>> def foo(s):  
   >>> ...     x = int(s)  
   >>> ...     assert x!=0,'x is zero'  
   >>> ...     return 10/x  
   >>> ...  
   >>> foo(0)  
   >>> Traceback (most recent call last):  
   >>> File "<python-input-21>", line 1, in <module>  
   >>> foo(0)  
   >>> ~~~^^^  
   >>> File "<python-input-20>", line 3, in foo  
   >>> assert x!=0,'x is zero'  
   >>> ^^^^  
   >>> AssertionError: x is zero
   >>>
   >>
   >
2. ​**​`logging`​**​ **是 Python 内置的日志记录模块，** ：必须先调用 `logging.basicConfig(level=logging.INFO)`​ 进行配置，否则 `logging.info()`​ 默认不会输出任何内容。这是因为 `logging`​ 的默认级别是 `WARNING`​，低于该级别的 `DEBUG`​ 和 `INFO` 会被自动过滤。

   import logging  
   logging.basicConfig(level=logging.INFO)

   s = '0'  
   n = int(s)  
   logging.info('n = %d' % n)  
   print(10 / n)  
     
   INFO:root:n = 0  
   Traceback (most recent call last):  
     File "err.py", line 8, in <module>  
       print(10 / n)  
   ZeroDivisionError: division by zero
3. ​**​`basicConfig()`​** ​ **是最简单的配置方式，**   
     

   import logging

   logging.basicConfig(  
       level=logging.DEBUG,          # 最低输出级别  
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 输出格式  
       datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式  
       filename='app.log',           # 输出到文件（不指定则输出到控制台）  
       filemode='a'                  # 文件写入模式（a=追加，w=覆盖）  
   )  
     

   |字段|含义|
   | ------| --------------------|
   |​`%(asctime)s`|时间戳|
   |​`%(name)s`|logger 名称|
   |​`%(levelname)s`|日志级别|
   |​`%(message)s`|日志消息|
   |​`%(filename)s`|调用日志的源文件名|
   |​`%(lineno)d`|调用日志的代码行号|
   |​`%(funcName)s`|调用日志的函数名|

‍

‍

## Ⅹ、IO编程

#### 文件读写

1. ​`open()`​ 函数，`open()`​ 返回一个**文件对象**

   file = open("data.txt", "r")    # 打开文件用于读取  
   content = file.read()          # 读取全部内容  
   file.close()                   # 关闭文件
2. **打开模式：**​**​`mode`​**​ **参数**

   |模式|含义|文件不存在时|文件存在时|
   | ------| --------------| --------------| ------------------|
   |​`"r"`|只读（默认）|报错|从开头读取|
   |​`"w"`|只写|创建新文件|**清空**原有内容|
   |​`"a"`|追加|创建新文件|在末尾追加|
   |​`"x"`|独占创建|创建新文件|报错（防止覆盖）|
   |​`"r+"`|读写|报错|从开头读写|
   |​`"w+"`|读写|创建新文件|清空原有内容|
   |​`"a+"`|读写|创建新文件|从末尾读写|

   ​**二进制模式**​：在模式后加 `b`​，如 `"rb"`​、`"wb"`​。二进制模式下，数据以 `bytes` 对象读写，不进行编码转换。

   ​**编码指定**​：文本模式下可指定编码，如 `open("file.txt", "r", encoding="utf-8")`。

   >>> f = open('file.txt','r')  
   >>> f.read()  
   >>> 'filefile\n'  
   >>> f.close()  
   >>> f = open('file.txt','w')  
   >>> f.write('nihao')  
   >>> 5  
   >>> f.close()  
   >>> f = open('file.txt','w')  
   >>> f.write('yayay')  
   >>> 5  
   >>> f = open('file.txt','r')  
   >>> f.read()  
   >>> 'yayay'  
   >>> f = open('file.txt','a')  
   >>> f.write('hello')  
   >>> 5  
   >>> f.close()  
   >>> f = open('file.txt','r')  
   >>> f.read()  
   >>> 'yayayhello'  
   >>> f.close()  
   >>> f = open('file.txt','r',encoding='UTF-8')  
   >>> f.read()  
   >>> 'yayayhello'
   >>>
   >>
   >
3. ​**​`with`​**​ **语句：自动资源管理，**​**​`with`​**​ **语句确保文件在使用后自动关闭**，即使块内发生异常，文件也会被正确关闭。**这是文件操作的标准写法**

   with open("data.txt", "r") as file:   # 进入 with 块时打开文件  
       content = file.read()              # 使用文件

   退出 with 块时自动调用 file.close()  
     

   >>> with open('file.txt','r') as f:  
   >>> ...     content = f.read()  
   >>> ...
   >>>
   >>> content  
   >>> 'yayayhello'
   >>>
   >>
   >
4. **读文件**  
   ​**​`read()`​** ​：读取全部内容 ,返回整个文件内容的字符串,对于大文件，这可能耗尽内存  
   ​**​`readline()`​** ​：逐行读取,读取第一行（包括换行符）,到达文件末尾时返回空字符串 ""  
   ​**​`readlines()`​** ​：读取所有行,返回列表，每行一个元素,同样可能耗尽内存  
   **直接迭代文件对象（推荐**）,文件对象本身是可迭代的,逐行处理，内存友好  
   **指定读取大小**,适合读取二进制文件或分块处理

   >>> with open('file.txt','r') as f:  
   >>> ...     c = f.read()  
   >>> ...  
   >>> c  
   >>> 'yayayhello\nadadada\nwewewew\newewe'  
   >>> with open('file.txt','r') as f:  
   >>> ...     l1 = f.readline()  
   >>> ...     l2 = f.readline()  
   >>> ...  
   >>> l1  
   >>> 'yayayhello\n'  
   >>> l2  
   >>> 'adadada\n'  
   >>> with open('file.txt','r') as f:  
   >>> ...     ls = f.readlines()  
   >>> ...  
   >>> ls  
   >>> ['yayayhello\n', 'adadada\n', 'wewewew\n', 'ewewe']  
   >>> with open('file.txt','r') as f:  
   >>> ...     for l in f:  
   >>> ...         print(l.strip())  
   >>> ...  
   >>> yayayhello  
   >>> adadada  
   >>> wewewew  
   >>> ewewe  
   >>> with open('file.txt','r') as f:  
   >>> ...     c = f.read(4)  
   >>> ...  
   >>> c  
   >>> 'yaya'
   >>>
   >>
   >
5. **写文件**  
   ​**​`write()`​** ​ **：写入字符串，**​**​`write()`​** ​ **不会自动添加换行符**​**​`writelines()`​** ​ **：写入字符串序列，**​**​`writelines()`​** ​ **不会自动加换行符，列表中的每个字符串需要自己包含换行符。**

   >>> with open('a.txt','w') as f:  
   >>> ...     f.write("nihao")  
   >>> ...     f.write("bonjue")  
   >>> ...  
   >>> 5  
   >>> 6  
   >>> with open('a.txt','r') as f:  
   >>> ...     f.read()  
   >>> ...  
   >>> 'nihaobonjue'  
   >>>   
   >>>
   >>> lines = ['aaaa','bbbb','cccc']  
   >>>   
   >>>
   >>> with open('a.txt','w') as f:  
   >>> ...     f.writelines(lines)  
   >>> ...  
   >>> with open('a.txt','r') as f:  
   >>> ...     f.read()  
   >>> ...  
   >>> 'aaaabbbbcccc'
   >>>
   >>
   >
6. ​**​`pathlib`​**​ **：现代的文件路径操作**

   from pathlib import Path

   创建 Path 对象

   p = Path("data.txt")          # 相对路径  
   p = Path("/home/user/data.txt")  # 绝对路径

   常用操作

   print(p.exists())             # 文件是否存在  
   print(p.is_file())            # 是否是文件  
   print(p.is_dir())             # 是否是目录  
   print(p.name)                 # 文件名（含扩展名）  
   print(p.stem)                 # 文件名（不含扩展名）  
   print(p.suffix)               # 扩展名  
   print(p.parent)               # 父目录  
   print(p.absolute())           # 绝对路径

   读写文件（替代 open()）

   content = p.read_text(encoding="utf-8")      # 读取文本  
   p.write_text("Hello", encoding="utf-8")      # 写入文本

   data = p.read_bytes()                        # 读取二进制  
   p.write_bytes(b"binary data")                # 写入二进制

   路径操作

   new_path = p.with_name("new.txt")            # 修改文件名  
   new_path = p.with_suffix(".json")            # 修改扩展名
7. **文件位置：seek() 和 tell()，文件对象内部有一个"当前位置"指针。读取或写入都会移动这个指针。**

   >>> with open('file.txt','r') as f:  
   >>> ...     f.tell()  
   >>> ...     f.read(8)  
   >>> ...     f.tell()  
   >>> ...     f.read(8)  
   >>> ...     f.tell()  
   >>> ...     f.seek(0)  
   >>> ...     f.tell()  
   >>> ...  
   >>> 0  
   >>> 'yayayhel'  
   >>> 8  
   >>> 'lo\nadada'  
   >>> 17  
   >>> 0  
   >>> 0
   >>>
   >>
   >
8. ​`seek(offset, whence)` 参数：

   - ​`whence=0`（默认）：从文件开头计算偏移
   - ​`whence=1`：从当前位置计算偏移
   - ​`whence=2`：从文件末尾计算偏移

     f.seek(0, 2)          # 跳到文件末尾  
     f.seek(-10, 2)        # 从末尾向前 10 字节

#### StringIO和BytesIO

1. **StringIO 和 BytesIO：内存中的文件**，**在内存中模拟文件对象的行为**。当你需要一个"文件"来读写，但不想真的创建磁盘文件时，就用它们。
2. **StringIO：处理文本数据，**​**​`StringIO`​**​ **在内存中创建一个文本文件的模拟对象。**

   >>> from io import StringIO  
   >>> f = StringIO()  
   >>> f.write('hello')  
   >>> 5  
   >>> f.getvalue()  
   >>> 'hello'
   >>>
   >>
   >
3. **StringIO初始化时传入数据**

   from io import StringIO

   创建时直接传入初始内容（就像打开一个已有文件）

   data = "Hello  
   World  
   Python"  
   f = StringIO(data)

   像读文件一样读取

   print(f.read())          # Hello  
                            # World  
                            # Python  
   print(f.read())          # '' （指针已到末尾）

   f.seek(0)                # 回到开头  
   print(f.readline())      # Hello  
   print(f.readline())      # World
4. **支持文件对象操作的所有方法**
5. ​**​`StringIO`​**​ **只处理 Unicode 字符串，如果你有字节数据，需要先解码**

   >>> f = StringIO('aaaa')  
   >>> f.getvalue()  
   >>> 'aaaa'  
   >>> b = b'byte'  
   >>> f = StringIO(b.decode('utf-8'))  
   >>> ...
   >>>
   >>> f.getvalue()  
   >>> 'byte'
   >>>
   >>
   >
6. **BytesIO：处理二进制数据，**​**​`BytesIO`​**​ **在内存中创建一个二进制文件的模拟对象。**   
     

   from io import BytesIO

   1. 创建空的 BytesIO

   f = BytesIO()

   2. 写入二进制数据

   f.write(b"Hello")      # 注意：参数必须是 bytes  
   f.write(b" World")

   3. 获取数据

   data = f.getvalue()  
   print(data)            # b'Hello World'  
   print(type(data))      # <class 'bytes'>  
     

   >>> p = BytesIO()  
   >>>   
   >>> p.write('中文'.encode('utf-8'))  
   >>> 6  
   >>> p.getvalue()  
   >>> b'\xe4\xb8\xad\xe6\x96\x87'  
   >>>   
   >>>
   >>>>>> from io import BytesIO  
   >>>>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')  
   >>>>>> f.read()  
   >>>>>> b'\xe4\xb8\xad\xe6\x96\x87'
   >>>>>>
   >>>>>
   >>>>
   >>>
   >>
   >

‍

#### 序列化

1. **把变量从内存中变成可存储或传输的过程称之为序列化，序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。**​**​`pickle`​**​**模块来实现序列化**
2. ​**​`pickle.dumps()`​** ​**方法把任意对象序列化成一个**​**​`bytes`​**​ **，然后，就可以把这个**​**​`bytes`​**​**写入文件。或者用另一个方法**​**​`pickle.dump()`​** ​**直接把对象序列化后写入一个file-like Object：**

   >>> import pickle  
   >>> d = dict(name='Bob', age=20, score=88)  
   >>> pickle.dumps(d)  
   >>> b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'  
   >>>   
   >>>
   >>> f = open('dump.txt', 'wb')  
   >>> pickle.dump(d, f)  
   >>> f.close()
   >>>
   >>
   >
3. **当我们要把对象从磁盘读到内存时，可以先把内容读到一个**​**​`bytes`​**​ **，然后用**​**​`pickle.loads()`​** ​**方法反序列化出对象，也可以直接用**​**​`pickle.load()`​** ​**方法从一个**​**​`file-like Object`​**​**中直接反序列化出对象**

   >>> f = open('dump.txt', 'rb')  
   >>> d = pickle.load(f)  
   >>> f.close()  
   >>> d  
   >>> {'age': 20, 'score': 88, 'name': 'Bob'}
   >>>
   >>
   >
4. ​**​`json`​**​**模块提供了非常完善的Python对象到JSON格式的转换。**​**​`dumps()`​** ​**方法返回一个**​**​`str`​**​ **，内容就是标准的JSON。类似的，**​**​`dump()`​** ​**方法可以直接把JSON写入一个**​**​`file-like Object`​**​ **，要把JSON反序列化为Python对象，用**​**​`loads()`​** ​**或者对应的**​**​`load()`​** ​**方法，前者把JSON的字符串反序列化，后者从**​**​`file-like Object`​**​**中读取字符串并反序列化：**

   >>> import json  
   >>> d = dict(name='Bob', age=20, score=88)  
   >>> json.dumps(d)  
   >>> '{"age": 20, "score": 88, "name": "Bob"}'  
   >>>   
   >>>
   >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'  
   >>> json.loads(json_str)  
   >>> {'age': 20, 'score': 88, 'name': 'Bob'}
   >>>
   >>
   >
5. ‍

‍
