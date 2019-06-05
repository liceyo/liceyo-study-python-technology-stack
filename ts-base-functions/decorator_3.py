from functools import wraps


# 装饰器类
class Logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        print('打印日志')
        pass


@Logit()
def func1():
    pass


class EmailLogit(Logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', logfile='out.log'):
        super(Logit, self).__init__()
        self.email = email
        self.logfile = logfile

    def notify(self):
        print('发送邮件')
        pass


@EmailLogit()
def func2():
    pass


func1()
func2()
