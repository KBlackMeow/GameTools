# -*- coding: utf-8 -*-
from pyshark import FileCapture
import tqdm
# 读取 pcap 文件并创建一个FileCapture对象
capture = FileCapture('crawler.pcap')

# 查看前10个数据包的信息摘要
ans = 0
ids = []
for i,packet in enumerate(tqdm.tqdm(capture)):
    if "http" in packet :
        http_layer = packet['http']
        if "python-requests" in str(packet):
            ans += 1
            if ans==100:
                print(packet.tcp.stream,i+1)
            # if packet.tcp.stream == "189":
            #     print(http_layer)   
            # ids.append(packet.tcp.stream)

print(ans)


from scapy.all import rdpcap

# 定义关键字
keyword = b"python"  # 注意：关键字需要是字节类型

# 初始化计数器
packet_count = 0

# 读取 PCAP 文件
packets = rdpcap("crawler.pcap")

# 遍历每个数据包
for i, packet in tqdm.tqdm(enumerate(packets)):
    # 检查数据包是否包含关键字
    if keyword in bytes(packet):
        packet_count += 1
        if packet_count == 100:
            print(f"The 100th packet containing the keyword is packet number: {i+1}")

print(f"Total packets containing the keyword: {packet_count}")