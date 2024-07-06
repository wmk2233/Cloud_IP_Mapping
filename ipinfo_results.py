# 使用IPinfo API服务来查询IP归属信息，并保存结果到Excel文件ip_ownership_results.xlsx

import pandas as pd
import ipinfo

# IPinfo API Token，在IPinfo官网注册账号可以获得API Token
API_TOKEN = 'ee3148ece15c7c'

# 初始化IPinfo客户端
ipinfo_client = ipinfo.getHandler(API_TOKEN)

# 读取nmap扫描结果
input_file = 'nmap_scan_results.xlsx'
df = pd.read_excel(input_file)

# 函数：获取IP归属信息
def get_ip_details(ip):
    details = ipinfo_client.getDetails(ip)
    return details.all

# 遍历DataFrame，获取每个IP的归属信息
ip_details_list = []
for ip in df['IP'].unique():
    print(f"正在查询IP: {ip}")
    details = get_ip_details(ip)
    ip_details_list.append({
        'IP': ip,
        'Organization': details.get('org', ''),
        'City': details.get('city', ''),
        'Region': details.get('region', ''),
        'Country': details.get('country', '')
    })

# 创建IP归属信息的DataFrame
ip_details_df = pd.DataFrame(ip_details_list)

# 将IP归属信息合并到原始nmap扫描结果中
result_df = pd.merge(df, ip_details_df, on='IP', how='left')

# 保存合并后的结果到Excel文件
output_file = 'ali_results.xlsx'
result_df.to_excel(output_file, index=False)
print(f"结果已保存到 {output_file}")
