import binascii
from math import ceil
from random import choice
from gmssl import sm3, func
import sys
xor = lambda a, b:list(map(lambda x, y: x ^ y, a, b))

rotl = lambda x, n:((x << n) & 0xffffffff) | ((x >> (32 - n)) & 0xffffffff)

get_uint32_be = lambda key_data:((key_data[0] << 24) | (key_data[1] << 16) | (key_data[2] << 8) | (key_data[3]))

put_uint32_be = lambda n:[((n>>24)&0xff), ((n>>16)&0xff), ((n>>8)&0xff), ((n)&0xff)]

padding = lambda data, block=16: data + [(16 - len(data) % block)for _ in range(16 - len(data) % block)]

unpadding = lambda data: data[:-data[-1]]

list_to_bytes = lambda data: b''.join([bytes((i,)) for i in data])

bytes_to_list = lambda data: [i for i in data]

random_hex = lambda x: ''.join([choice('0123456789abcdef') for _ in range(x)])

IV = [
    1937774191, 1226093241, 388252375, 3666478592,
    2842636476, 372324522, 3817729613, 2969243214,
]

T_j = [
    2043430169, 2043430169, 2043430169, 2043430169, 2043430169, 2043430169,
    2043430169, 2043430169, 2043430169, 2043430169, 2043430169, 2043430169,
    2043430169, 2043430169, 2043430169, 2043430169, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042, 2055708042, 2055708042,
    2055708042, 2055708042, 2055708042, 2055708042
]

def sm3_ff_j(x, y, z, j):
    if 0 <= j and j < 16:
        ret = x ^ y ^ z
    elif 16 <= j and j < 64:
        ret = (x & y) | (x & z) | (y & z)
    return ret

def sm3_gg_j(x, y, z, j):
    if 0 <= j and j < 16:
        ret = x ^ y ^ z
    elif 16 <= j and j < 64:
        #ret = (X | Y) & ((2 ** 32 - 1 - X) | Z)
        ret = (x & y) | ((~ x) & z)
    return ret

def sm3_p_0(x):
    return x ^ (rotl(x, 9 % 32)) ^ (rotl(x, 17 % 32))

def sm3_p_1(x):
    return x ^ (rotl(x, 15 % 32)) ^ (rotl(x, 23 % 32))

def sm3_cf(v_i, b_i):
    w = []
    for i in range(16):
        weight = 0x1000000
        data = 0
        for k in range(i*4,(i+1)*4):
            data = data + b_i[k]*weight
            weight = int(weight/0x100)
        w.append(data)

    for j in range(16, 68):
        w.append(0)
        w[j] = sm3_p_1(w[j-16] ^ w[j-9] ^ (rotl(w[j-3], 15 % 32))) ^ (rotl(w[j-13], 7 % 32)) ^ w[j-6]
        str1 = "%08x" % w[j]
    w_1 = []
    for j in range(0, 64):
        w_1.append(0)
        w_1[j] = w[j] ^ w[j+4]
        str1 = "%08x" % w_1[j]

    a, b, c, d, e, f, g, h = v_i

    for j in range(0, 64):
        ss_1 = rotl(
            ((rotl(a, 12 % 32)) +
            e +
            (rotl(T_j[j], j % 32))) & 0xffffffff, 7 % 32
        )
        ss_2 = ss_1 ^ (rotl(a, 12 % 32))
        tt_1 = (sm3_ff_j(a, b, c, j) + d + ss_2 + w_1[j]) & 0xffffffff
        tt_2 = (sm3_gg_j(e, f, g, j) + h + ss_1 + w[j]) & 0xffffffff
        d = c
        c = rotl(b, 9 % 32)
        b = a
        a = tt_1
        h = g
        g = rotl(f, 19 % 32)
        f = e
        e = sm3_p_0(tt_2)

        a, b, c, d, e, f, g, h = map(
            lambda x:x & 0xFFFFFFFF ,[a, b, c, d, e, f, g, h])

    v_j = [a, b, c, d, e, f, g, h]
    return [v_j[i] ^ v_i[i] for i in range(8)]

def getpadding(len1):
    msg=[]
    reserve1 = len1 % 64
    msg.append(0x80)
    reserve1 = reserve1 + 1
    # 56-64, add 64 byte
    range_end = 56
    if reserve1 > range_end:
        range_end = range_end + 64

    for i in range(reserve1, range_end):
        msg.append(0x00)
    bit_length = (len1) * 8
    bit_length_str = [bit_length % 0x100]
    for i in range(7):
        bit_length = int(bit_length / 0x100)
        bit_length_str.append(bit_length % 0x100)
    for i in range(8):
        msg.append(bit_length_str[7-i])
    return bytes(msg).hex()

def sm3_hash_fake(msg, length1=0,length2=0 ,hash=""):
    IV = []
    if len(hash)>0 :
        for i in range(8):
            IV.append(int(hash[i*8:(i+1)*8],16))
    else :
        IV = [
            1937774191, 1226093241, 388252375, 3666478592,
            2842636476, 372324522, 3817729613, 2969243214,
        ]
    len2 = length2
    len1 = len(msg) + length1
    reserve1 = len1 % 64
    msg.append(0x80)
    reserve1 = reserve1 + 1
    # 56-64, add 64 byte
    range_end = 56
    if reserve1 > range_end:
        range_end = range_end + 64

    for i in range(reserve1, range_end):
        msg.append(0x00)
    bit_length = (len1) * 8
    bit_length_str = [bit_length % 0x100]
    for i in range(7):
        bit_length = int(bit_length / 0x100)
        bit_length_str.append(bit_length % 0x100)
    for i in range(8):
        msg.append(bit_length_str[7-i])
    if len(hash)>0:
        msg=msg[len2:]
    group_count = round(len(msg) / 64)

    B = []
    for i in range(0, group_count):
        B.append(msg[i*64:(i+1)*64])

    V = []
    V.append(IV)
    for i in range(0, group_count):
        V.append(sm3_cf(V[i], B[i]))

    y = V[i+1]
    result = ""
    for i in y:
        result = '%s%08x' % (result, i)
    return result

def sm3_kdf(z, klen): # z为16进制表示的比特串（str），klen为密钥长度（单位byte）
    klen = int(klen)
    ct = 0x00000001
    rcnt = ceil(klen/32)
    zin = [i for i in bytes.fromhex(z.decode('utf8'))]
    ha = ""
    for i in range(rcnt):
        msg = zin  + [i for i in binascii.a2b_hex(('%08x' % ct).encode('utf8'))]
        ha = ha + sm3_hash_fake(msg)
        ct += 1
    return ha[0: klen * 2]

def test():
    MySecretInfo = b"B"*64
    len1 = len(MySecretInfo)
    HashValue = sm3_hash_fake(func.bytes_to_list(MySecretInfo))
    print('MySecretInfo Hash:', HashValue)
    print("="*64)
    ## 填入原始数据的padding
    padding = getpadding(len(MySecretInfo))
    print("padding:",padding)
    AppendData = bytes.fromhex(padding)
    len2=len(AppendData)
    ## 增加额外数据
    AppendData += b"Hello World"
    ## assert len(AppendData) == 64
    NewSecretInfo = MySecretInfo + AppendData
    ## 正版
    NewHashValue0 = sm3.sm3_hash(func.bytes_to_list(NewSecretInfo))
    ## 盗版
    NewHashValue1 = sm3_hash_fake(func.bytes_to_list(NewSecretInfo))
    ## 扩展后的字符串 原始字符长度  原始字符填充长度
    NewHashValue2 = sm3_hash_fake(func.bytes_to_list(AppendData),len1,len2,HashValue)
    print("="*64)
    print(f"{NewHashValue0}\n{NewHashValue1}\n{NewHashValue2}")    

def sm3_append_attack(hash_value,src_len,append_str_bytes):
    len1 = src_len
    ## 填入原始数据的padding
    padding = getpadding(len1)
    print("hex(padding):",padding)
    AppendData = bytes.fromhex(padding)
    len2=len(AppendData)
    ## 增加额外数据
    AppendData += append_str_bytes
    print("hex(append_data):",AppendData.hex())
    ## 扩展后的字符串 原始字符长度  原始字符填充长度
    NewHashValue = sm3_hash_fake(func.bytes_to_list(AppendData),len1,len2,hash_value)
    print("="*64)
    print(f"{NewHashValue}")    
if __name__ == '__main__':
    # test()
    sm3_append_attack("6df5e4109b1f8f0194f2cd047423a5bdd33145efe36b4f6fb13d908ff43f486f",64,b"Hello World")