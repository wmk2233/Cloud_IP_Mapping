# Cloud_IP_Mapping
# 文件说明

## ali_results文件夹

存储对阿里云IP范围为163.181.0.0/16做主动探测的结果。

- **masscan_results.xml**：使用Masscan进行快速扫描IP范围为163.181.0.0/16得到的1-1000范围内的IP对应开放端口
- **ip_port_list.txt**：从masscan_results.xml文件提取的server IP和开放端口的对应。
- **nmap_scan_results.xlsx**：使用nmap扫描ip_port_list.txt中的IP和对应端口，探测得到的服务类型结果。
- **ali_results.xlsx**：使用IPinfo API服务来查询IP归属信息结果，和原始nmap扫描结果nmap_scan_results.xlsx合并后得到最终的结果。

## dns_results、http_results、ssl_results文件夹

分别存储对三份被动流量日志进行分析的结果。

- **top_client_ips_ssl.csv**：日志文件中出现频率较高的10个客户端IP地址，可能是种子IP。
- **client_to_server.csv**：种子IP访问的所有服务器IP地址，客户端IP与服务端IP的交互。
- **filtered_server_ips.csv**：剔除常见流行服务IP地址，信工所的可能特定服务IP地址。
- **masscan_output_iie.xml**：使用Masscan进行快速扫描得到的server IP和开放端口。
- **ip_port_list.txt**：从masscan_output_iie.xml文件提取的server IP和开放端口的对应。
- **nmap_scan_results.xlsx**：使用nmap扫描ip_port_list.txt中的IP和对应端口，探测得到的服务类型结果。
- **ip_ownership_results.xlsx**：使用IPinfo API服务来查询IP归属信息结果，和原始nmap扫描结果nmap_scan_results.xlsx合并后得到最终的结果。

**aws_ip_ranges.xlsx**：

从云服务提供商aws提供的josn文件获取到的IP范围和服务类型。

# py文件说明

- aws.py：从aws官方公开的IP范围提取ip和对应服务到aws_ip_ranges.xlsx
- server_ip.py：从日志文件中提取出现频率较高的10个客户端IP地址、种子IP访问的所有服务器IP地址、剔除流行服务的IP后找到可能特定于信工所的服务IP地址。将最终过滤得到的server IP保存到filtered_server_ips.csv
- masscan.py：解析masscan的输出文件masscan_output_iie.xml，提取ip和开放端口到文件ip_port_list.txt
- nmap.py：使用nmap扫描ip_port_list.txt中的IP和对应端口，探测服务保存到nmap_scan_results.xlsx
- ipinfo_results.py：使用IPinfo API服务来查询IP归属信息，并保存结果到Excel文件ip_ownership_results.xlsx
