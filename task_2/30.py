# 30. Вычислить число Пи c заданной точностью d
#	Пример: при d = 0.001,  = 3.141. 10-1d≤10-10

import math 
P = 0.001 

P = str(P).split('.') 
L = len(P[1]) 
M = str(math.pi) 
print(float(M[:L+2]))