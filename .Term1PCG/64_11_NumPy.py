import numpy as np

def f1(M, c):
    return M*c

def f2(U, V):
    return sum(U*V)

def f3(M):
    return M.T

def f4(x, y, dx, dy, k, R):
    neighbors = (x-x[k])**2 + (y-y[k])**2 <= R**2
    sx = sum(neighbors*dx)
    sy = sum(neighbors*dy)
    t = np.arctan2(sy,sx)
    return np.cos(t), np.sin(t)

# def f4(x, y, dx, dy, k, R):
#     # x, y, dx, dy: 1-D numpy arrays of all equal size
#     # k, R: float
#     neighbors = [(x[i]-x[k])**2 + (y[i]-y[k])**2 <= R**2
#                  for i in range(len(x))]
#     sx = sy = 0
#     for i in range(len(neighbors)):
#         # True is equal to 1 and False is equal to 0
#         sx += neighbors[i] * dx[i]  
#         sy += neighbors[i] * dy[i]
#     t = np.arctan2(sy, sx)
#     return np.cos(t), np.sin(t)

#----- DON'T modify any of the following lines -----
for k in range(int(input())):
    exec(input().strip())