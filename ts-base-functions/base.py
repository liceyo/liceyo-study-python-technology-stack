# 可变长参数
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('a', 'b', 'c')


# 键值对的可变长参数
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


greet_me(name="liceyo", val='lee')


# 测试调用
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("two", 3, 5)
test_args_kwargs(*args)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)


# map
def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))

# reduce
from functools import reduce, wraps

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

# set
# 交集
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = {'red', 'brown'}
print(input_set.intersection(valid))
### 输出: set(['red'])
# 差集
print(input_set.difference(valid))
### 输出: set(['brown'])
print(valid.difference(input_set))
### 输出: set(['black', 'blue', 'green', 'yellow'])

# 三元运算符

is_fat = True
state = "fat" if is_fat else "not fat"
print(state)  # fat
fitness = ("skinny", "fat")[is_fat]  # True等于1，而False等于0 ,不推荐使用
print("Ali is ", fitness)
# 输出: Ali is fat

# 函数缓存
from functools import lru_cache


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(10)])  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# 函数缓存的实现
def memoize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(25))


# 上下文管理（实现）
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')


class File2(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True  # 如果返回true,表示异常已经被处理，with语句不会抛出异常


with File2('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output: Exception has been handled
