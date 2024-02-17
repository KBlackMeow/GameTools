from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import gmpy2
path = 'crypto/test/Rabin/pubkey.pem'
with open(path) as f:
    global e,n
    key = RSA.import_key(f.read())
    print('e = %d' % key.e)
    print('n = %d' % key.n)
    e = key.e
    n=  key.n
# yafu 分解n 得到 pq
p= 275127860351348928173285174381581152299
q= 319576316814478949870590164193048041239
phi_n = (p-1)*(q-1)
print(e,phi_n)
# d = gmpy2.invert(e,phi_n)#即e*d mod phi_n = 1
with open("crypto/test/Rabin/flag.enc",'rb') as file:
    global c
    file = file.read()
    c = bytes_to_long(file)

inv_p = gmpy2.invert(p, q)
inv_q = gmpy2.invert(q, p)

# 计算mp和mq
mp = gmpy2.powmod(c, (p + 1) // 4, p)
mq = gmpy2.powmod(c, (q + 1) // 4, q)

# 计算a,b,c,d
a = (inv_p * p * mq + inv_q * q * mp) % n
b = n - int(a)
c = (inv_p * p * mq - inv_q * q * mp) % n
d = n - int(c)
print(long_to_bytes(a))
print(long_to_bytes(b))
print(long_to_bytes(c))
print(long_to_bytes(d))