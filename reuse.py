import time
from tracemalloc import start
Start = time.time()
if Start != "0":pass
else: pass
End = time.time()
print(f"{End-Start}")
Want = "สวัสดีครับผม"
print(f"{Want}")
A = [[0,0],[0,0]]*3
C = A
C[0][0] = 2
B = [0]*6
B[1] = 2
d = [0 for i in range(6) ]
print(A)