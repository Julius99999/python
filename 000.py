import csv
from collections import Counter


def count_unique_duplicate_rows_in_csv(file_path):
    """
    计算CSV文件中不同重复行的数量（不考虑重复出现的次数）。

    参数:
    file_path (str): CSV文件的路径。

    返回:
    int: 不同重复行的数量。
    """
    rows = []
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # 将行转换为元组，因为列表是不可哈希的
            rows.append(tuple(row))

            # 使用Counter统计每个元组（即每行）出现的次数
    row_counts = Counter(rows)

    # 计算不同重复行的数量（即出现次数大于1的行的种类数）
    unique_duplicate_count = len([row for row, count in row_counts.items() if count > 1])

    return unique_duplicate_count


# 使用函数并计算CSV文件中不同重复项的数量
file_path = "D:/attack.csv"  # 使用双反斜杠转义
# 或者使用原始字符串
# file_path = r"D:/attack.csv"

unique_duplicate_count = count_unique_duplicate_rows_in_csv(file_path)
print(f"scv表中相同的项的个数为: {unique_duplicate_count}")