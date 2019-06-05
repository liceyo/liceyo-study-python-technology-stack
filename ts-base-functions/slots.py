class MyClass(object):
    # 为你的内存减轻负担。通过这个技巧，有些人已经看到内存占用率几乎40%~50%的减少。
    # 在Python中，每个类都有实例属性。
    # 默认情况下Python用一个字典来保存一个对象的实例属性。这非常有用，因为它允许我们在运行时去设置任意的新属性。会消耗掉很多内存
    # 需要使用__slots__来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


my_class = MyClass('liceyo', 2)
print(my_class.name)
