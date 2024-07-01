import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('attack.csv')

# 清除列名中的空格
df.columns = df.columns.str.strip()

# 假设 IP 地址在 'ip' 列中
ip_column = 'ip'

# 检查 'ip' 列是否存在
if ip_column in df.columns:
    # 找出 IP 地址和它们的出现次数
    ip_counts = df[ip_column].value_counts()

    # 将 IP 地址和出现次数转换为 DataFrame
    result_df = ip_counts.reset_index()
    result_df.columns = [ip_column, 'count']

    # 将结果输出到新的 CSV 文件
    result_df.to_csv('tt.csv', index=False)

    # 输出重复的 IP 地址和重复个数
    duplicate_ips = result_df[result_df['count'] > 1]
else:
    print(f"列名 '{ip_column}' 不存在")
