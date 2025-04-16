# -*- coding:utf8 -*-
# @Author : 1cePeak
import re
import base64
import hashlib
from Crypto.Cipher import AES
def Decrypt(key, data): 
    magicNum = int(key[:2], 16) % 16 # 魔数长度
    data = data[:len(data) - magicNum] # 去掉魔数
    c = AES.new(key, AES.MODE_ECB)
    decodebs = base64.b64decode(data)
    # print(c.decrypt(decodebs)) 
    return c.decrypt(decodebs)
def Key_Brute(data): 
    with open('Top100000.txt', 'rb') as f: 
        plain = [i.strip() for i in f.readlines()]
        for i in plain:
            md5_enc = hashlib.md5(i).hexdigest()
            try: 
                key = md5_enc[:16].encode()
                AES_dec = Decrypt(key, data).decode('utf-8') 
                cmd = re.findall(r'[\s\S]\$cmd=\"(.*?)\"', AES_dec)
                if cmd: # print('[*] Crack Success!!!' + '\n' + '[*] The Key is ' + md5_enc[:16] + '\n' + '[*] Decode Text：' + '\n' + AES_dec)
                    print('[*] Crack Success!!!' + '\n' + '[*] Key: ' + i.decode('utf-8') + '\n[*] Webshell Key: ' + md5_enc[:16])
                    payload = base64.b64decode(cmd[0]).decode('utf-8')
                    print('[*] Payload: ' + payload)
                    # print(i)
                break
            except Exception as e:
                pass

if __name__ == '__main__': 
    data ="""S/qD+voQyDdj4MOPowXBsNK/aaBI4C1UQhKWPEQfWubzXydnwjKtX4R9f6PL0AZZ5Gt2IHo5CGhhHCjtRvg13Qn9/3Bgn6XGpajVaRzd
dCYIdVZFJHbQ7JBnYMcR2Sb1cShPfARGUW2Q7xq8KhY0KoEb49/WjOk3Ho5ZmZcRtqsS26rUH1JGraEIQkKYcg2qzFvoqI/wodh7gGwk
KzIfPqVie5YHWSkOTdkkVqQXNSUKlLsoOa0dPlknI3ijpUy8nblIeNSs1v6HBYJNPzYKy4vDAFBAm2W2y5ZDmkOfS/vXfXhTLzyTmDjtpn
utbuI+i4suI31BrGBHPzxSsdFucskn4QYRBQQ6X353/1ZJn4wvHYvHTeWaY9BvtucEoZXUDVTESycyp14F7v7PtAIjZ+9NOhvj71XHtNRK
qlGfs/GZym3c8fW7euFxy6FLYQbLtPUa+CN2XWmW9ZvYPqw1YR0Dk5cW1CZrxcTggE8gxiccN/wutwUGwizkY7Sznb6dcY+jdMfYIVCvp
ZbLz9aTzJmtcX5L2df1Qp44EGKCe6ca5srVu46HpXabk17cwTO8j6IhqwY+vx4BaruU2ZFZruerO6ejhiwjsdrEf/Wj4o1+cj+tpUUlJ/vKZWBb +a8iZW6KclBNmjNcpXeHqxmxLI5AFS3HswOh3p05wo8HkaQ295d6Wz87XN4iALoGTpXjicdVWJivrKxKqUDVQwJn7Ffarod2KqQVxZn8 +ctMeozYjf0ZVHr2iSJIUnWmIh+nXmuAuVfEQvauc/Em0Hr9cel3wmMzl/uV+spqrSZNvMdaka58yFkGpP5tGOKDgjZZiAqhf4egl9pyHk90v k3v0EAVK9cKqigLVs5Ugp6zBl2pb6IMQFrfjr43Rl1VhxW6jYcjbr2zpKy3abRhIZbZUUuWahNY3rbQZQ+awl0Mi7pfuXKN5ORjYAk3oWT
sj2DEvqHNvpVVwjb7kxsbQUGNgFLgty0Gci1GtrMQ+RM/92PhLfnsFFZYr++hKg2uVaydBnVTKSzso5FugkcLqilzl4WmfdmA4G5WuDwv1
2iyS7CTJTqLzlr4/lZrvEwRjqJ3c3Z2tg9IbN7yCq293HQ0OJjGAM360nlPfXX3pohG9xc6gY5CGCuTHapykUA1sqmyvyQwVowByAdhWtVBe 64ewnCsdPEfOASBUb+MQArn/1GDnpUAH6vYZHyCzIExRv9wx3wZEmCGhLX/OmIY09nNH5QAqrpHah00deS/rsdrP7bySKFMyRrUdvZ
EreZwMcVlRG7Fs8+LJwK0xJS9xk8zSUz1gcj3e4mm5+j4GCrCjVc0Wz5RAyMxx3yTuyU8/MUgVWhzrxuV+v9FDjY7n9F4JnL/THz7ROVm
Hwn9qqqAiy3JC2HzxH1WBm5AkJ83S7wqchU09vkBXncePeSCzicFdemqnoLPCCwepKRd8mTAF7I0m9hpBnIrfYFbzz21GQ+r3W1PxYMf
h2FCV8FR3c4hpMB5F4a62c5tv8QhHXlhuOPAxvY6h0RN4c8ZRERMOZwbB9eu/NaYduJw4Np41nu0WyMtIc75BZMEOYWGlgtXwx3WC
ONs+upzNfQmPaBBGgY+xdtnUHzW9kzr62RgTbQMKWCAhvN8WrJEeqm2aZldqOJvlfyYJoTK50o52dPeRdWv5B6UOf7ODOYzLbYjhGiR
DooWXzb9c8MbFHJp7jQPaccXFcyAVtrBWozrCI7nZWlY0Aj1IyBnQUNwt0kB0/yrtR5cQRvZr2bX2nGh5hcjMv1FjgoEp2kYQVjDqVoj0Vj
6I3G4p3W48pi7dTkQOG6ojwpEGgdrjZZ1qGkufP2UG5n+zChhy2fH3xwb6bc7+zpwe66f+YcM9EwpGa8AddtSpVpsZcddHdkmqpSksWjcG
NjpWpYc4/R6SWXHQH0YqzPUFGOJqOVkBWzsDxuo4r1clDxfe/iEWkP34sL7IIl26I0TjUUcVx70faldBgONysiyg6VeA7NnTQhsSrh1Wobg
2VjyhNlyU/DS55FwxrmDJGcsstd++ZHGvKskmiGcyAb3lPmSEd1bJMcCW1jqGRIOdR3rdSBuF0Uc4TqoBZQP+z5rJwj85UOB80myXDvrfsz EsYQxlxyDLNea7RDspwLghtWhNe7EnL2RezoUQdnEQNd7UfpMuyswg4MTOB0c0TVGat2tV+j5GDPAts1wrxe2LZAdR26mx97a13BEQ3m
cdDtOUhWgJlySDjDrknR1R3r64MduQRT4SFT0P3y9TPHGo52uLJeyaYBMHUJIhfMfnqhyJSPA4G81cmjuPSpxmYUMK5oQBjfBrzJmO7ph
2ojgc8FloI/9o3k+Y7jfp/MZG0K1U9ryC5KZQSXHHGzBW6fSiLMwD2pGvHfVPouqcMkAshWOL5AAg4nONGVogDl1s8fFDwjdZOVtACm7
QoKwzX7AlPmSEd1bJMcCW1jqGRIOdSgRgITUnzqqX2S74o+g2Pes3f1w4nWWxnU7t9X9sFnOU2mEWsYPqry5tAELIHtI0zX2FhThtDBd
1WL2jXQzp6SyAfVpMigZUM4EGDCgzzahFL2o3bwiaJ9+tAj/TFdzGQvm4EECYdYD/+/mujBygge83sfpFkKT7ffQqUFZfXb6838yrIusIfClnJ
ZLMzdRYlNo6ZOTc0pdjIPaNPxLgRzrdzgruSFSWdru4jWuupHYqF7kwKkpS0jGm+Ed36AQ+Vvwv4NiTYQ57YMWHB/OapqDnpUAH6vY
ZHyCzIExRv9wQCYmKxI23A3TOBB/I+GD/onGa0d4TM1Xdy1otXTYcCktRS2jLluAWnMD/GhJ7tUEyjwavXSQZXQPn2AvObLE+Qp0BCC
lZI4I3xglOXB4bdC5718bOkUZtskKz0J6+KLEPr27I48fetJmR6S1UbrphGi/mGaHb8xSbOI/LC6mNvF6K8Rqa+gqZQYI1Bbamw+FC/5m4qI
FRlNA4uP15FYkleU3loOR/vmbO0cTZkVXHBXCxhXJtzaDmBufGeORu68rUPEIKznipBSOAOYZGq8d3uqWpHVWZn2pXBE0eF8ymX27
LjOir7vjwClq7rs6D/eesoaZlyVGIYo8/iRMlnPEINu+i7cG0YALWc3XFb2TJybjiDLWkvATve/OCAqOx5xxmTWZFroHjCeOesv/Poki6Xj+0j9 +cZcdltfaq3LkVtg7oKoorreNT+EvfjJ7yfSqMIW9d29JdzyF9/xaE4mlvM3OxQi8MHNdjJiXwtwHS0Yh7Q4LDT06I5WDdnkDqfmOG6+bfM5e MOVsyV6WQvzhkofl23jR/zpqyPeVgKUDkWnAQBXLSGF3JrJqHXt7QeRdyFxE4/1fJ+9D7g9BiTkVnLrNlO3zHmJmocZUm/IYSIfDoUWvcb
XevzOGvdQA23o9V6gHzh/3ZxK6ADN/UGXrDGKx0UDQTyBrDWISvqxTrQ1EbQTdZi7geOU4qcGIp1QDPsYyJnbs5wAlghdMqw15MjYc6 +USN9eGxQ7NdFG3Wn9cvxS/8GjyPD+q5mZsQ95BPsYyJnbs5wAlghdMqw15MrZEdjo+e3RdpUaJU7DahD6PAosRwzo8Vmov5vNdu5QAZ
72YEvKJTIMUhZeoPP0p8birLirmXZjsmXOCkIxao/tPV5ezr8qrdy7DU1NpDx8yJn6WC+qgIGn1006T/bBTcpRE9wdL481TkRcDqQH1E3iS
Xw13/9iffZloVpaVCGSxYh0xbO8VwgM5hbjzxiIDHRTEydQD1u+d2qncr5XdFBZ/kzOWdVPimnngKjThTf5sERPGaHY1GpT3JdMT8UjRF
VTf2Vw+0gAo+k6hsJmTA08wACL0e8cD06F/6aMnNg4X49WIToeb2cdwXHEto+T4rbTCFJjGY+84/7njDHM7UZI3PLO2Ib04wIjc25M6KH
vVWdAflAafoAIGWuWSJgJo1fExVvisu/46Rl8hf35JFIMx4QQXlAcfhZChvYvCsFDTRpApEb1BgLtt6JevNFTT5EyWMJxGusht1vVc4oGAM
HUcYnBtlRrggPUk97mb3jUazZE7XOiF2bRbiZgXNSW8tMh7ZUU1pEqyIshoPSSXoGV5mPToVfofO2RHVC3UOF9CAp8IGxsUxelDyFYnE
v1w7TWe26aC5F2rxJjzuKHgvwgOKEkIkgUx7Td3a5fgiy16pwCNTi5vqh1VHH1N5OU7NpnhHZy1soTFSPEAL2BfjliX6TNQdAJ4YaT4U7Q
W27Px7IJHOJKzQFMteih+0s1vQtnoRC6Cwlmy2ggx7lu4gzsQNVGdpDYSXKSL175CR4J0FkItFTThCYEivYuoYNiVJuzIqJSoriFPrvkww4Si
91huhb80wiQtBgtp9BkZ2dcy8fSU+fc1VUz1iEoKyTB6H+YTv07LmphdQyzc9p2RJGRpiP96Uz7mFOnrHDMjfVBTIKH6lFDQytrxmdB0OZ7
v/75GCaX1Pdl/FyojkUR9gw/lZWt26EWKgI+iq0xvzFWrhmdj2iewdhtMCYhEp2lFTCQB5BAVHJ67EXct6VI0MBpY+36NVZj6u1b7wykFbF
fshEnIL0zskHkVuUGIYCi0Y1VhG+S6udIi1PVfCA0Ke0qeXWVuUwFEHKx3HrDw34v2eMDipfgOubo6GvjWADYYlfcHgwoUZIyx8w1DsL
cHbAvTKLuIy17cZDtJxw7mcmJzzGQhZJm5iisEF/y4dlCDMA==.%.""".split('\n')

    data = "".join(data)   
    # print(data) 
    Key_Brute(data)
