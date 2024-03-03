# coding:utf-8
import os
from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf import PasswordType 
def get_reader(filename, password):
    try:
        old_file = open(filename, 'rb')
    except Exception as err:
        print('文件打开失败！' + str(err))
        return None
 
    # 创建读实例
    pdf_reader = PdfReader(old_file, strict=False)
    # 解密操作
    if pdf_reader.is_encrypted:
        if password is None:
            print('%s文件被加密，需要密码！' % filename)
            return None
        else:
            code = pdf_reader.decrypt(password)
            # print(code , PasswordType.NOT_DECRYPTED,code == PasswordType.NOT_DECRYPTED)
            if  code == PasswordType.NOT_DECRYPTED:
                print('%s 密码不正确！' % filename, code)
                return None
    if old_file in locals():
        old_file.close()
    return pdf_reader
 
 
def decrypt_pdf(filename, password, decrypted_filename=None):
    """
    将加密的文件及逆行解密，并生成一个无需密码pdf文件
    :param filename: 原先加密的pdf文件
    :param password: 对应的密码
    :param decrypted_filename: 解密之后的文件名
    :return:
    """
    # 生成一个Reader和Writer
    pdf_reader = get_reader(filename, password)
    if pdf_reader is None:
        return
    if not pdf_reader.is_encrypted:
        print('文件没有被加密，无需操作！')
        return
    pdf_writer = PdfWriter()
 
    pdf_writer.append_pages_from_reader(pdf_reader)
 
    if decrypted_filename is None:
        decrypted_filename = "".join(filename[:-4]) + '_' + 'decrypted' + '.pdf'
 

    # 文件加密
    # pdf_writer.encrypt(user_password = "123", 
    # owner_pwd = "123456", 
    # use_128bit = True)
    # 写入新文件
    pdf_writer.write(open(decrypted_filename, 'wb'))
    print("解密成功")
 
 
if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    password = ""
    if len(sys.argv)>2:
        password = sys.argv[2]
    print(filename,password)
    decrypt_pdf(filename,password)