import base64
tar = "GzssGDC8HbEwgDMygJ00mjIZfjsTgLCwHLIzMrkqHLK8mbE7"
string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/+"
string2 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0987654321+/" 
# encrypted_str = input("请输入要解密的字符串：")
# 替换字符
# print(str.maketrans(string2, string1))
decoded_str = tar.translate(str.maketrans(string2, string1))
print(decoded_str)

# # base64 解码
# decoded_str = base64.b64decode(decoded_str).decode()
# print(decoded_str) # 输出解密后的字符串