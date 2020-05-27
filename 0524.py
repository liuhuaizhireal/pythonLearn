# 输出与输入

print('输出所用的')

# a = input('这个是输入')
# print('刚才输入的是' + a)
# 输出多行内容

print('''
line1
line2
line3
''')

# 布尔值显示  注意布尔值是首字母大写
print( 1 > 2)

# list和tuple
listA = ['张三','李四','王五']
print(listA)
# list长度
tempListLen = len(listA)
print(tempListLen)
# list追加
listA.append('赵六')
print(listA)
# list插入
listA.insert(0,'徐悲鸿')
print(listA)
# list删除 pop

# tuple 元组 不可变数组