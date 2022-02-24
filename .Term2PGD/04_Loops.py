Key = input().split(",")
StdData = input()
Plus, Min, Zero = 0, 0, 0
for i in range(len(Key[0])):
    if i < len(StdData):
        if StdData[i] == "-": Zero += 1
        elif StdData[i] == Key[0][i]: Plus += 1
        else: Min += 1  
    else:Zero += 1
Score = Plus*int(Key[1]) - Min*int(Key[2])
if Score < 0: Score = 0
print(Plus, Min, Zero, Score)