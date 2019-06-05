from functools import wraps


# 一切皆对象


def hi(name="yasoob"):
    return "hi " + name


print(hi())
# output: 'hi yasoob'
greet = hi
print(greet())
# output: 'hi yasoob'
del hi
# print(hi())
# outputs: NameError
print(greet())


# outputs: 'hi yasoob'


# 函数中定义函数并使用
def hi():
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()


# output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# 函数中返回函数
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)
# outputs: <function greet at 0x7f2143c01500>

print(a())


# outputs: now you are in the greet() function


# 装饰器
def a_new_decorator(a_func):
    @wraps(a_func)  # s使wrap_the_function不重写a_func的名字和注释文档(docstring)
    def wrap_the_function():
        print("前置处理")
        a_func()
        print("后置处理")

    return wrap_the_function


def a_function_requiring_decoration():
    print("业务处理")


a_function_requiring_decoration()
# outputs: "业务处理"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()


# outputs:前置处理
#         业务处理
#         后置处理

@a_new_decorator
def b_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("业务处理-2")


b_function_requiring_decoration()


# 装饰器蓝本


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func(name):
    return "Function is running --%s" % name


can_run = True
print(func('a'))
# Output: Function is running

can_run = False
print(func('b'))
# Output: Function will not run
