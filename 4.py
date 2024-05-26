# 直接使用[]创建列表
lst=['hello','world',98,100.5]
print(lst)

#可以使用内置的函数list()创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2))# 从1开始到10结束，步长为2，不包含10
print(lst2)
print(lst3)
# 列表是序列中的一部分，对序列的操作符，运算符，函数均可以使用
print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o'))
print(lst2.index('o'))
# 列表的删除操作
