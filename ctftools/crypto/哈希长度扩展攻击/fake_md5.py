import struct
import hashlib
# 一些常量
s = [
    7, 12, 17, 22,  # 第一轮
    5,  9, 14, 20,  # 第二轮
    4, 11, 16, 23,  # 第三轮
    6, 10, 15, 21   # 第四轮
]

K = [
    0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
]

# 初始化MD5的缓冲区
def md5_init():
    return [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

# 将输入数据填充到512位的倍数
def md5_pad(message):
    message = bytearray(message)
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += orig_len_in_bits.to_bytes(8, byteorder='little')
    return message

# 定义MD5的左旋转函数
def left_rotate(x, c):
    return (x << c) | (x >> (32 - c))

# 定义主要的MD5处理函数
def md5_compress(buf, chunk):
    a, b, c, d = buf

    # 将块划分为16个32位字
    X = list(struct.unpack('<16I', chunk))

    # 主循环
    for i in range(64):
        if 0 <= i <= 15:
            f = (b & c) | (~b & d)
            g = i
        elif 16 <= i <= 31:
            f = (d & b) | (~d & c)
            g = (5 * i + 1) % 16
        elif 32 <= i <= 47:
            f = b ^ c ^ d
            g = (3 * i + 5) % 16
        else:
            f = c ^ (b | ~d)
            g = (7 * i) % 16

        f = (f + a + K[i] + X[g]) & 0xffffffff
        a, b, c, d = d, (b + left_rotate((f & 0xFFFFFFFF), s[i % 4 + (i // 16) * 4])) & 0xFFFFFFFF, b, c

    # 加入到当前的散列值
    for i, val in enumerate([a, b, c, d]):
        buf[i] = (buf[i] + val) & 0xffffffff

def md5(message,state=None):
    message = md5_pad(message)
    if state is None:
        buf = md5_init()

    for chunk_ofst in range(0, len(message), 64):
        md5_compress(buf, message[chunk_ofst:chunk_ofst + 64])

    return buf

def md5_to_hex(digest):
    raw = struct.pack('<4I', *digest)
    return ''.join(f'{byte:02x}' for byte in raw)


def md5_length_extension_attack(original_data, original_md5, additional_data):
    buf = list(struct.unpack('<4I', bytes.fromhex(original_md5)))

    padding1 = md5_pad(original_data)
    padding2 = md5_pad(padding1+additional_data)
    message = padding2[len(padding1):]
    for chunk_ofst in range(0, len(message), 64):
        md5_compress(buf, message[chunk_ofst:chunk_ofst + 64])
    return md5_to_hex(buf),padding2[:len(padding1+additional_data)],padding2[len(original_data):len(padding1+additional_data)]


# 使用示例
original_data = b"hello"
original_md5 = md5_to_hex(md5(original_data))  # MD5("hello")
additional_data = b" world"
new_md5, new_data,new_append = md5_length_extension_attack(original_data, original_md5, additional_data)


def md5_append_attack(original_len,original_md5,additional_data,original=None):
    original_data = b"A"*original_len
    if not original is None:
        original_data = original
    new_md5, new_data,new_append = md5_length_extension_attack(original_data, original_md5, additional_data)
    # print("hex(new_data):", new_data.hex())
    print("hex(append_data):",new_append.hex())
    print("="*64)
    print(new_md5)
    if not original is None:
        print("hashlib.md5:",hashlib.md5(new_data).hexdigest())

if __name__ == "__main__":
    md5_append_attack(5,"5d41402abc4b2a76b9719d911017c592",b" world",b"hello")