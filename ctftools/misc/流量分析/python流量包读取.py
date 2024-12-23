import pyshark
import tqdm
def analyze_pcap_with_pyshark(file_path):
    # 打开 PCAP ⽂件
    capture = pyshark.FileCapture(file_path, display_filter="http")
    sub = 0
    # 初始化计数器
    python_requests_count = 0
    normal_requests_count = 0
    key = 0
    flag_100 = 0
    # 遍历数据包
    ans_stream = 0
    for packet in tqdm.tqdm(capture):
        try:
            # 获取 HTTP 请求头中的 User-Agent
            user_agent = packet.http.get('User-Agent', '')
            # 判断 User-Agent 类型
            if "python-requests/2.29.0" in user_agent:
                python_requests_count += 1
                if python_requests_count == 100:
                    ans_stream =  packet.tcp.stream
                    flag_100 = 1
                    print(ans_stream)
            elif "Mozilla/5.0" in user_agent:   
                normal_requests_count += 1
        except AttributeError:
            # 如果数据包不包含 HTTP 层或 User-Agent，跳过
            continue

        if packet.tcp.stream == ans_stream and "http" in packet:
            try:
                body = packet.http.file_data
                if flag_100 == 1:
                    print('the 100 response length: '+packet.http.get('Content-Length', ''))
                    print('the 100 response length: ' + str(len(body)))
                    flag_100 = 0
            except:
                pass
    # 关闭捕获对象
    capture.close()
    return python_requests_count, normal_requests_count
# 使⽤示例
file_path = "crawler.pcap" # 替换为你的 PCAP ⽂件路径
python_count, normal_count = analyze_pcap_with_pyshark(file_path)
print(f"Python requests count: {python_count}")
print(f"Normal requests count: {normal_count}")