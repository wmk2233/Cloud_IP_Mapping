# 使用nmap扫描ip_port_list.txt中的IP和对应端口，探测服务保存到nmap_scan_results.xlsx

import subprocess
import pandas as pd

# 函数：从文件中读取IP地址和端口
def read_ip_port_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    ip_ports = [line.strip().split() for line in lines]
    return ip_ports

# 函数：执行Nmap扫描
def perform_nmap_scan(ip, port):
    command = f"nmap -p {port} {ip}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# 函数：解析Nmap扫描结果
def parse_nmap_result(scan_output):
    parsed_data = []
    lines = scan_output.split('\n')
    ip = None
    for line in lines:
        if 'Nmap scan report for' in line:
            ip = line.split()[-1]
        if '/tcp' in line:
            parts = line.split()
            port = parts[0].split('/')[0]
            state = parts[1]
            service = parts[2] if len(parts) > 2 else ''
            parsed_data.append([ip, port, service, state])
    return parsed_data

# 主程序
if __name__ == "__main__":
    ip_port_file = 'ip_port_list.txt'
    ip_ports = read_ip_port_file(ip_port_file)

    all_scan_results = []
    for ip, port in ip_ports:
        print(f"正在扫描 IP: {ip}, 端口: {port}")
        scan_output = perform_nmap_scan(ip, port)
        parsed_result = parse_nmap_result(scan_output)
        all_scan_results.extend(parsed_result)

    # 创建DataFrame
    columns = ['IP', 'Port', 'Service', 'State']
    df = pd.DataFrame(all_scan_results, columns=columns)

    # 保存到Excel文件
    output_file = 'nmap_scan_results.xlsx'
    df.to_excel(output_file, index=False)
    print(f"扫描结果已保存到 {output_file}")
