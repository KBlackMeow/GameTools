from z3 import *
 
# 首先创建一个求解器
s = Solver() 
 
'''
比如我们想求解这么一个问题
x + y = 5
x >= 2
y >= 2
我们想看看符合要求的x，y的整数解有哪些？
'''
 
# 定义两个变量
v7 = Int('v7')
v6 = Int('v6')
v5 = Int('v5')
v4 = Int('v4')
# #
# #  (((( ((( v7 ^  (v7 >> 11)) & 0x2A4E) << 7) ^  (v7 ^ (v7 >> 11))) & 0x7B2A) << 15) ^ (((v7 ^ (v7 >> 11)) & 0xF12A4E) << 7) ^ v7 ^ (v7 >> 11) ^ ((((( ((( v7 ^  (v7 >> 11)) & 0x2A4E) << 7) ^  (v7 ^ (v7 >> 11))) & 0x7B2A) << 15) ^ (((v7 ^ (v7 >> 11)) & 0xF12A4E) << 7) ^ v7 ^ (v7 >> 11)) >> 18)) == 404303411
    # && (((( ((( v6 ^  (v6 >> 11)) & 0x2A4E) << 7) ^  (v6 ^ (v6 >> 11))) & 0x7B2A) << 15) ^ (((v6 ^ (v6 >> 11)) & 0xF12A4E) << 7) ^ v6 ^ (v6 >> 11) ^ ((((( ((( v6 ^  (v6 >> 11)) & 0x2A4E) << 7) ^  (v6 ^ (v6 >> 11))) & 0x7B2A) << 15) ^ (((v6 ^ (v6 >> 11)) & 0xF12A4E) << 7) ^ v6 ^ (v6 >> 11)) >> 18)) == 1499145799
    # && (((( ((( v5 ^  (v5 >> 11)) & 0x2A4E) << 7) ^  (v5 ^ (v5 >> 11))) & 0x7B2A) << 15) ^ (((v5 ^ (v5 >> 11)) & 0xF12A4E) << 7) ^ v5 ^ (v5 >> 11) ^ ((((( ((( v5 ^  (v5 >> 11)) & 0x2A4E) << 7) ^  (v5 ^ (v5 >> 11))) & 0x7B2A) << 15) ^ (((v5 ^ (v5 >> 11)) & 0xF12A4E) << 7) ^ v5 ^ (v5 >> 11)) >> 18)) == -1407364476
    # && (((( ((( v4 ^  (v4 >> 11)) & 0x2A4E) << 7) ^  (v4 ^ (v4 >> 11))) & 0x7B2A) << 15) ^ (((v4 ^ (v4 >> 11)) & 0xF12A4E) << 7) ^ v4 ^ (v4 >> 11) ^ ((((( ((( v4 ^  (v4 >> 11)) & 0x2A4E) << 7) ^  (v4 ^ (v4 >> 11))) & 0x7B2A) << 15) ^ (((v4 ^ (v4 >> 11)) & 0xF12A4E) << 7) ^ v4 ^ (v4 >> 11)) >> 18)) == 425173660 )
# 在求解器中定义约束条件
s.add(((((((( v7 ^  (v7 >> 11)) & 0x2A4E) << 7) ^  (v7 ^ (v7 >> 11))) & 0x7B2A) << 15) ^ (((v7 ^ (v7 >> 11)) & 0xF12A4E) << 7) ^ v7 ^ (v7 >> 11) ^ ((((( ((( v7 ^  (v7 >> 11)) & 0x2A4E) << 7) ^  (v7 ^ (v7 >> 11))) & 0x7B2A) << 15) ^ (((v7 ^ (v7 >> 11)) & 0xF12A4E) << 7) ^ v7 ^ (v7 >> 11)) >> 18)) == 404303411)
# 我们调用求解器的check()方法来判别约束集合是否能得到可行解，如果可行，给出结果
print(s.check())
if s.check():
    m = s.model()
    print(m)
 
'''
输出：
sat
[y = 2, x = 3]
'''

'''
smt问题可以理解为很多逻辑谓词的组合，我们可以做一些问题的推理工作
比如有这么一个问题
Alice and Bob can complete a job in 2 hours.
Alice and Charlie can complete the same job in 3 hours
Bob and Charlie can complete the same job in 4 hours
How long will the job take if Alice, Bob, and Charlie work together?Assume each person works at a constant rate, whetherworking alone or working with others.
'''
 
# from z3 import *
# s = Solver()
 
# a, b, c, n = Reals('a b c n')
 
# s.add(a * 2 + b * 2 == 1)
# s.add(a * 3 + c * 3 == 1)
# s.add(b * 4 + c * 4 == 1)
# s.add(a * n + b * n + c *n == 1)
 
# pr(s.check())
# if s.check() == sat:
#     m = s.model()
#     pr(m)
 
'''
输出：
sat
[n = 24/13, c = 1/24, a = 7/24, b = 5/24]
'''