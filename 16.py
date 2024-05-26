# 假设data是一个包含IP地址的字符串列表

file_path = '../address.txt'
data = [line.strip() for line in open(file_path, 'r') if line.strip()]

# 将数据转换为集合，自动去除重复项
unique_ips = set(data)

"""
# 使用集合来找出重复的IP地址
duplicate_ips = set()
for ip in data:
    if data.count(ip) > 1:
        duplicate_ips.add(ip)
"""

# 打印出所有重复的IP地址
print("Duplicate IPs:", unique_ips)