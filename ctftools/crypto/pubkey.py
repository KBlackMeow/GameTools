from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import gmpy2
path = 'crypto/test/pubkey/pub.key'
with open(path) as f:
    global e,n
    key = RSA.import_key(f.read())
    print('e = %d' % key.e)
    print('n = %d' % key.n)
    e = key.e
    n=  key.n
# yafu 分解n 得到 pq
p= 285960468890451637935629440372639283459
q= 304008741604601924494328155975272418463
phi_n = (p-1)*(q-1)
d = gmpy2.invert(e,phi_n)#即e*d mod phi_n = 1
with open("crypto/test/pubkey/flag.enc",'rb') as file:
    file = file.read()
    c = bytes_to_long(file)
    print(long_to_bytes(gmpy2.powmod(c,d,n)))