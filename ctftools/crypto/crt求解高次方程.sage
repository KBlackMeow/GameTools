import gmpy2
from Crypto.Util.number import *

e = 23
n = 76198847820766755799575419083507924439717371587288270051268263988998008696707
c = 22544322401515359081098558097211421427974939372246104662667107456064368566176

p = 278397922222800446346367107995770769671
q = 273704800712503895893612643539504241317



p_roots = mod(c, p).nth_root(e, all=True)
q_roots = mod(c, q).nth_root(e, all=True)
for p_root in p_roots:
   for q_root in q_roots:
       flag = long_to_bytes(int(crt([Integer(p_root), Integer(q_root)], [p, q])))
       if flag.startswith(b"flag{"):
           print(flag.decode())