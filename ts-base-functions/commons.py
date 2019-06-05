# abs
print(abs(-12000.7))
print(abs(0))

# all
print(all([]))  # True
print(all(()))  # True
print(all([0, 1, 2, 3]))  # False
print(all(['', 'a', 'b']))  # False
print(all([1, 2, 3, 4]))  # True
print(all(['a', 'b', 'c']))  # True

# any
print(any([]))  # False
print(any(()))  # false
print(any([0, 1, 2, 3]))  # true
print(any(['', 'a', 'b']))  # true
print(any([1, 2, 3, 4]))  # true
print(any(['a', 'b', 'c']))  # true
print(any([0, '', False]))  # false

# bin 转为二进制字符串
print(bin(521))  # 0b1000001001


class MyType:
    def __index__(self):
        return 35  # 0b100011


mt = MyType()
print(bin(mt))

# bool
print(bool())  # false
print(bool(''))  # false
print(bool(100))  # true
print(bool(0))  # false
print(bool('xx'))  # true

# bytearray 返回一个byte数组
print(bytearray(3)[1])  # bytearray(b'\x00\x00\x00') 数组
print(bytearray('abcd'.encode('utf-8'))[2])  # bytearray(b'abcd')
print(bytearray([1, 2, 3])[1])  # bytearray(b'\x01\x02\x03')

# callable 检查对象object是否可调用。
print(callable(0))  # false
print(callable("xxx"))  # false


def test():
    print('test hello')


print(callable(test))  # true
print(callable(MyType))  # true
print(callable(mt))  # false


class B:
    def __call__(self):
        return 0


b = B()
print(callable(b))  # true

# chr and ord  ASCII
print(chr(97))  # a
print(chr(98))  # b
print(ord('a'))  # 97
print(ord('b'))  # 98

# compile
code = "for i in range(0, 10): print(i)"
cmpcode = compile(code, '', 'exec')
print(cmpcode)  # <code object <module> at 0x0000023E88FB7150, file "", line 1>
s = "3 * 4 + 5"
a = compile(s, '', 'eval')
print(eval(a))  # 17

# complex 转为复数
print(complex(1))  # (1+0j)
print(complex(1, 2))  # (1+2j)
print(complex("1"))  # (1+0j)
print(complex("1+2j"))  # (1+2j)

# dir
print(dir(b))

# divmod
print(divmod(9, 2))  # (4,1) (a//b,a%b)

# id 返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，可能会出现相同的id值。
print(id(b))  # 1694775240072
print(id('s'))  # 2186061369504
print(id(1))  # 140719144592016

# int
print(int(3.14))  # 3
print(int(2e2))  # 200
print(int('23', base=16))  # 35
print(int('10', base=2))  # 2

# enumerate
print(list(enumerate("abcd")))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# eval 该函数易被黑客利用
x = 1
y = 1
num1 = eval("x+y")
print(num1)  # 2


def g():
    x = 2
    y = 2
    print(globals())
    print(locals())
    num3 = eval("x+y")
    print(num3)  # 4
    num2 = eval("x+y", globals())
    print(num2)  # 2
    num4 = eval("x+y", globals(), locals())
    print(num4)  # 4


g()
a = 1
gg = {'a': 20}
print(eval("a+1", gg))  # 21

# exec exec(object[, globals[, locals]])
exec('print(1+2)')

# filter(function, iterable)
print(list(filter(lambda x: x > 5, [1, 2, 4, 8, 16])))
print(''.join(list(filter(str.isdigit, 'test2019'))))
print(''.join(list(filter(lambda char: char in '0123456789.', 'test.2019'))))

# float
print(float('+123'))  # 123.0
print(float('+1.23'))  # 1.23
print(float('   -12345\n'))  # -12345.0
print(float('1e-003'))  # 0.001
print(float('+1E6'))  # 1000000.0
print(float('-Infinity'))  # -inf
print(float('inf'))  # inf
print(float('-inf'))  # -inf
print(float('+inf'))  # inf
print(float('nan'))  # nan
print(float('+nan'))  # nan
print(float('-nan'))  # nan
print(float())  # 0.0


class C:
    def __init__(self, score):
        self.score = score

    def __float__(self):
        return 1.0


c = C(100)
print(float(c))  # 1.0

# format(value[, format_spec])
# format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# fill        ::=  <any character>
# align       ::=  "<" | ">" | "=" | "^"
# sign        ::=  "+" | "-" | " "
# width       ::=  integerprecision   ::=
# integertype ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
# fill是表示可以填写任何字符。
# align是对齐方式，<是左对齐， >是右对齐，^是居中对齐。
# sign是符号， +表示正号， -表示负号。w
# idth是数字宽度，表示总共输出多少位数字。
# precision是小数保留位数。
print(format(2918))  # 1918
print(format(0x500, 'X'))  # 500
print(format(3.14, '0=10'))  # 0000003.14
print(format(3.14159, '05.3'))  # 03.14
print(format(3.14159, 'E'))  # 3.141590E+00
print(format('test', '*<20'))  # test****************
print(format('test', '*>20'))  # ****************test
print(format('test', '*^20'))  # ********test********
# Web Server Info :192.168.1.1:8888
print("{server}{1}:{0}".format(8888, '192.168.1.1', server='Web Server Info :'))
print("{0[1]}.{0[0]}".format(('google', 'com')))  # com.google
print("{0}*{1}={2:0>6}".format(3, 2, 2 * 3))  # 3*2=000006
print("{:.3f}".format(2.1415))
print('Coordinates: {latitude}, {longitude}'.format(**{}))

# frozenset([iterable]) 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
