# import random
# lst=[item for item in range(1,11)]
# print(lst)
#
# lst=[item*item for item in range(1,11)]
# print(lst)
#
# lst=[random.randint(1,10) for x in range(0,10)]
# print(lst)
#
# lst=[i for i in range(10) if i%2==0]
# print(lst)

# lst=[
#     ['城市','环北','同比'],
#     ['北京',102,103],
#     ['上海',104,504]
#     ['深圳',100,39]
# ]
# print(lst)
#
# for row in lst:
#     for item in row:
#         print(item,end='\t')
#     print()
#
# lst2=[[j for j in range(5)] for i in range(4)]
# print(lst2)


# t=('hello',[10,20,30],'python','world')
# print(t)
# # 使用内置函数tuple()创建元组
# t=tuple('helloword')
# print(t)
#
# t=tuple([10,20,30,40])
# print(t)
#
# print('10在元组中是否存在',(10 in t))
# print('10在元组中是不存在',(10 not in t))
# print('最大值',max(t))
# print('最小值',min(t))
# print('len',len(t))
# print('t.index:',t.index(10))
# print('t.count',t.count(10))
#
# t=(10,)
# print(t,type(t))
# y=(10,)
# print(y,type(y))

t=('python','hello','world')
# 根据索引访问元组
print(t[0])
t2=t[0:3:2]
print(t2)

# 元组的遍历
for item in t:
    print(item)

# for+range()len()
for i in range(len(t)):
    print(i,t[i])

for index,item in enumerate(t):
    print(index,'------>',item)
for index,item in enumerate(t,start=11):
    print(index,'------>',item)

