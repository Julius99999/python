# d={1001:'李梅',1002:'王华',1003:'张锋'}
# print(d)
# # 向字典中中添加元素
# d[1002]='张丽丽'
# print(d)

# # 获取字典中所有的key
# keys=d.keys()
# print(keys)
# print(list(keys))
# print(tuple(keys))
#
# # 获取字典中所有的value
# values=d.values()
# print(values)
# print(list(values))
# print(tuple(values))

# 如果将字典中的数据转成key-value的形式，以元组的方式进行展现
# lst=list(d.items())
# print(lst)
#
# d=dict(lst)
# print(d)
#
# # 使用pop函数
# print(d.pop(1001))
# print(d)
#
# print(d.pop(1008,'不存在'))
# # 随机删除
# print(d.popitem())
# print(d)
#
# # 清空字典中所有的元素
# d.clear()
# print(d)
# # Python中一切皆对象，每一个对象都有一个布尔值
# print(bool(d))#空字典的布尔值为False
#
# import random
# d={item:random.randint(1,100) for item in range(4)}
# print(d)
#
# # 创建两个表
# lst=[1001,1002,1003]
# lst2=['陈梅梅','王一一','王丽丽']
# d={key:value for (key,value) in zip(lst,lst2)}
# print(d)

def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的累加和为{s}')

# 函数的调用
get_sum(10)
get_sum(100)
get_sum(1000)