Info, Data  = input(), {"Total":0}
while Info != "q":
    New = Info.split()
    Data[New[0]], Info = float(Data[New[1]]), input()
for want in input().split():Data["Total"] += Data[want]
print("total payment", Data["Total"])