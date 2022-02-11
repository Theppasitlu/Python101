import math
a, b, c = int(input()), int(input()), int(input())
Want = math.acos((1/2*((a-b)+(a-c)))/(math.sqrt((a-b)**2+(a-c)*(b-c))))
print(360 - int(math.degrees(Want)))