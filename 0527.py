# 条件判断
from collections import Iterable
import math
a = 17
if a > 18:
    print('a is bigger than 18')
else:
    print('a is not bigger than 18')

# 循环
listA = [1, 2, 3, 4, 5]
sum = 0
for key in listA:
    sum += key
print('数组求和%s' % (sum))

# dict
dictA = {'zhangsan': 23, 'lisi': 24}
print('wangwu' in dictA, dictA.get('zhangsan'),
      dictA.get('wangwu', -1), dictA['lisi'])

# set
s = set([1, 2, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(1)
print(s)

# 函数


def test():
    return 1, 2


print(test())  # 返回多个值时 返回的其实是个tuple

# 函数的参数
# 1.位置参数


def location(x):
    return x

# 2.默认参数


def location2(x, y=2):
    return x, y


print(location2(2))

# 3.可变参数


def changeParms(*nums):
    sum = 0
    for key in nums:
        sum += key
    return sum


print(changeParms(1, 2, 3))
print(changeParms(*[1, 2, 3]))

# 3.关键字参数


def textParm(a, b, **c):
    print(a, b, c)


textParm(1, 2)
textParm(3, 4, wangwu=2)

# 4.命名关键字


def textName(a, b, *, kk):
    print(a, b, kk)


textName(1, 2, kk=3)

# 高级特性
# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[-2:])
print(L[-3:-2])
Y = list(range(100))
# 每隔五个
print(Y[::5])
# 字符串也可以进行切片
cc = 'ABCDEFG'[:3]
print(cc)

# 迭代
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
canName = isinstance('abc', Iterable)
print(canName)
