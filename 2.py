s = "hello world"
s1 = s[0:5:2]
print(s1)
# 省略开始位置
s2 = (s[:5:1])
# 省略结束位置
print(s[0:7:1])
# 省略步长
print(s[0:6:])
# 省略开始位置，结束位置、步长
print(s[::])
