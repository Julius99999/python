lst=['hello','world','python','pyp']
for item in lst:
    print(item)

for i in range(0,len(lst)):
    print(i,'-->',lst[i])
    #第三中遍历方法 enumearte()函数
for index,item in enumerate(lst):
    print(index,item)#index是序号，不是索引
    #手动修改序号的起始值
for index,item in enumerate(lst,start=9):
    print(index,item)
for index,item in enumerate(lst,1):
    print(index,item)