# 读取文件
with open('1.txt', 'r') as file:
    ip_addresses = file.readlines()

# 去除每个IP地址末尾的换行符
ip_addresses = [ip.strip() for ip in ip_addresses]

# 找出重复的IP地址和计数
ip_count = {}
for ip in ip_addresses:
    ip_count[ip] = ip_count.get(ip, 0) + 1

# 找出重复的IP地址
duplicates = {ip: count for ip, count in ip_count.items() if count > 1}

# 按出现次数倒序排序
sorted_duplicates = sorted(duplicates.items(), key=lambda x: x[1], reverse=True)

# 写入到 CSV 文件
with open('tt2.csv', 'w') as csvfile:
    csvfile.write("IP地址,出现次数\n")
    for ip, count in sorted_duplicates:
        csvfile.write(f"{ip},{count}\n")
