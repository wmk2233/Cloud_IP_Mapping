# 从日志文件中提取出现频率较高的10个客户端IP地址、种子IP访问的所有服务器IP地址、剔除流行服务的IP后找到可能特定于信工所的服务IP地址
# 将最终过滤得到的server IP保存到filtered_server_ips.csv
import pandas as pd

# 加载被动流量日志文件
file_path = "C:\\Users\\wmk\\Desktop\\雁栖湖-夏\\网络空间测绘与安全应用\\被动流量日志\\DNS_COLLECT_LOG.csv"

# 使用 'ISO-8859-1' 编码加载文件
try:
    ssl_log_df = pd.read_csv(file_path, encoding='ISO-8859-1')
except UnicodeDecodeError:
    # 如果失败，尝试使用 'latin1' 编码
    try:
        ssl_log_df = pd.read_csv(file_path, encoding='latin1')
    except UnicodeDecodeError:
        # 如果仍然失败，输出错误信息
        print("使用 'ISO-8859-1' 和 'latin1' 编码格式均无法读取文件。")
        exit()

# 步骤1：提取出现频率较高的10个客户端IP地址
top_client_ips = ssl_log_df['CLIENT_IP'].value_counts().head(10)
top_client_ips_list = top_client_ips.index.tolist()

# 打印前10个出现频率最高的客户端IP地址
print("Top 10 客户端IP地址:")
print(top_client_ips)

# 步骤2：记录种子IP访问的所有服务器IP地址
seed_ip_records = ssl_log_df[ssl_log_df['CLIENT_IP'].isin(top_client_ips_list)]
client_to_server = seed_ip_records[['CLIENT_IP', 'SERVER_IP']].drop_duplicates()

# 打印每个种子IP访问的所有服务器IP地址
print("\n客户端到服务器IP映射:")
print(client_to_server)

# 常见的公共服务IP地址列表
popular_services_ips = [
    '8.8.8.8', '8.8.4.4',  # Google DNS
    '1.1.1.1', '1.0.0.1',  # Cloudflare DNS
    '208.67.222.222', '208.67.220.220',  # OpenDNS
    # 更多公共服务IP地址可以根据实际情况添加
]

# 步骤3：剔除流行服务的IP，找到可能特定于信工所的服务IP地址
filtered_server_ips = client_to_server[~client_to_server['SERVER_IP'].isin(popular_services_ips)]
server_ip_intersection = filtered_server_ips['SERVER_IP'].value_counts()

# 打印剔除后的可能特定于信工所的服务IP地址
print("\n剔除后的服务器IP地址:")
print(server_ip_intersection)

# 保存结果到CSV文件
top_client_ips.to_csv('top_client_ips.csv', header=True)
client_to_server.to_csv('client_to_server.csv', index=False)
server_ip_intersection.to_csv('filtered_server_ips.csv', header=True)

print("\n结果已保存到CSV文件。")
