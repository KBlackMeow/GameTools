'''
smt问题可以理解为很多逻辑谓词的组合，我们可以做一些问题的推理工作
比如有这么一个问题
Alice and Bob can complete a job in 2 hours.
Alice and Charlie can complete the same job in 3 hours
Bob and Charlie can complete the same job in 4 hours
How long will the job take if Alice, Bob, and Charlie work together?Assume each person works at a constant rate, whetherworking alone or working with others.
'''
 
from z3 import *
s = Solver()
 
a, b, c, n = Reals('a b c n')
 
s.add(a * 2 + b * 2 == 1)
s.add(a * 3 + c * 3 == 1)
s.add(b * 4 + c * 4 == 1)
s.add(a * n + b * n + c *n == 1)
 
pr(s.check())
if s.check() == sat:
    m = s.model()
    pr(m)
 
'''
输出：
sat
[n = 24/13, c = 1/24, a = 7/24, b = 5/24]
'''