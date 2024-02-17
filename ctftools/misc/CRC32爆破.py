import string
import binascii
crc1=0x6C844E92

def ascii_letters(length,index):
    chars = string.ascii_letters+"-"+'0123456789'
    ret = ""
    for i in range(length):
        ret = chars[index%len(chars)] + ret
        index //= len(chars)
    return ret

def CRC32(crc):
    for i in range(40**4):
        st = ascii_letters(4,i)
        if crc == (binascii.crc32(str(st).encode()) & 0xffffffff):
            print (st)
            return

if __name__ =="__main__":
    CRC32(crc1)