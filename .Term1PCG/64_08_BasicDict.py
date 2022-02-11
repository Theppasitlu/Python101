def update(points, uses, reward):
    for e in uses:points[e] -= uses[e]
    for e in points:points[e] += (points[e]*reward)//100
# exec(input().strip()) 
# p={'A1':100,'A2':50,'A3':20};u={'A1':10,'A3':5};update(p,u,10);print(p)
