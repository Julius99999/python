s = "hello world"
print("e在s中存在吗？", 'e' in s)
print("v在s中存在吗？", 'v' in s)
print("e在s中不存在吗？", 'e' not in s)
print("v在s中不存在吗？", 'v' not in s)
# 内置函数的使用
print('len():', len(s))
print('max():', max(s))
print('min():', min(s))
print('s.index(0):', s.index('o'))
# print('s.count(v):', s.count("v"))# 元素不存在时，报错如下:ValueError: substring not found
print('s.count(l):', s.count("l"))
