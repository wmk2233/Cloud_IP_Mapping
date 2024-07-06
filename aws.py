# 从aws官方公开的IP范围提取ip和对应服务到aws_ip_ranges.xlsx

import json
import requests
import pandas as pd

# 获取 AWS IP 范围 JSON 文件
url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()
    print("成功获取JSON数据")
else:
    print(f"请求失败，状态码：{response.status_code}")
    exit()

# 提取所需信息
ip_ranges = []

# 处理 IPv4 前缀
for prefix in data['prefixes']:
    ip_ranges.append({
        'ip_prefix': prefix['ip_prefix'],
        'region': prefix['region'],
        'service': prefix['service'],
        'network_border_group': prefix.get('network_border_group', 'N/A')
    })

# 处理 IPv6 前缀
for prefix in data['ipv6_prefixes']:
    ip_ranges.append({
        'ip_prefix': prefix['ipv6_prefix'],
        'region': prefix['region'],
        'service': prefix['service'],
        'network_border_group': prefix.get('network_border_group', 'N/A')
    })

# 打印调试信息
print(f"提取了 {len(ip_ranges)} 条 IP 范围信息")

# 创建 DataFrame
df = pd.DataFrame(ip_ranges)

# 检查 DataFrame 内容
print(df.head())

# 将结果导出到 Excel 文件
output_file = "aws_ip_ranges.xlsx"
df.to_excel(output_file, index=False)

print(f"IP 归属列表已导出到 {output_file}")
