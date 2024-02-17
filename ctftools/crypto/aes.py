import base64

# x = "UEsDBBQAAQAAANgDvlTRoSUSMAAAACQAAAAHAAAAa2V5LnR4dGYJZVtgRzdJtOnW1ycl/O/AJ0rmzwNXxqbCRUq2LQid0gO2yXaPBcc9baLIAwnQ71BLAQI/ABQAAQAAANgDvlTRoSUSMAAAACQAAAAHACQAAAAAAAAAIAAAAAAAAABrZXkudHh0CgAgAAAAAAABABgAOg7Zcnlz2AE6DtlyeXPYAfldXhh5c9gBUEsFBgAAAAABAAEAWQAAAFUAAAAAAA=="
# bt = base64.b64decode(x)

# with open("xxx","wb") as output:
#     output.write(bt)
#     output.close()


c = base64.b64decode("n8kP0oP0W/hTGikWNNcSudW9l7M/wduqvASeUycn2nI=")
from Crypto.Cipher import AES

key = b'l36DoqKUYQP0N7e1' #秘钥，b就是表示为bytes类型
iv  = b'131b0c8a7a6e072e' #需要加密的内容，bytes类型
aes = AES.new(key,AES.MODE_CBC,iv=iv) #创建一个aes对象
den_text = aes.decrypt(c) # 解密密文
print("明文：",den_text)


# print(base64.b64encode(aes.encrypt(b"admIn\n\n\n\n\n\n\n\n\n\n\n")))