import csv

def find_duplicate_ips(csv_file, output_file):
    ip_count = {}  # 用于存储 IP 地址和它们的出现次数

    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过标题行

        for row in reader:
            ip = row[0]  # 假设 IP 地址在每行的第一个位置
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

    # 按照出现次数倒序排序
    sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)

    # 写入到输出文件
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['IP地址', '重复次数']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ip, count in sorted_ips:
            writer.writerow({'IP地址': ip, '重复次数': count})

if __name__ == "__main__":
    find_duplicate_ips("attack.csv", "tt1.csv")#输出到tt1.csv文件
