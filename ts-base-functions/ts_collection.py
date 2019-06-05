from collections import Counter, defaultdict, deque, namedtuple
from enum import Enum

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)
favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)
print(favourite_colours)

# 双向队列
d = deque()
d.append('1')
d.append('2')
d.append('3')
print(d.pop())  # 3
print(d.popleft())  # 1

# namedtuple 命名元组 namedtuple的每个实例没有对象字典
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)  # Animal(name='perry', age=31, type='cat')
print(perry.name)  # perry
print(perry[0])  # perry


# enum
class Species(Enum):
    '''
    Species(1)
    Species['cat']
    Species.cat
    '''
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2  # (译者注：幼小的狗狗)


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)
