# 解析masscan的输出文件masscan_output_iie.xml，提取ip和端口到文件ip_port_list.txt

import xml.etree.ElementTree as ET
# 解析Masscan的XML输出，提取IP地址和端口
def extract_masscan_results(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    ip_port_pairs = []
    for host in root.findall('host'):
        ip_addr = host.find('address').attrib['addr']
        for port in host.find('ports').findall('port'):
            port_id = port.attrib['portid']
            ip_port_pairs.append((ip_addr, port_id))

    return ip_port_pairs


# Masscan的XML输出文件
masscan_output_file = 'masscan_results.xml'

# 提取IP地址和端口
ip_port_pairs = extract_masscan_results(masscan_output_file)

# 将IP地址和端口保存到文本文件
ip_port_list_file = 'ip_port_list.txt'
with open(ip_port_list_file, 'w') as f:
    for ip, port in ip_port_pairs:
        f.write(f"{ip} {port}\n")

print(f"Extracted IP and port pairs have been saved to {ip_port_list_file}")
