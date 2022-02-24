ABC = input()
XYZ = []
total = 0

while ABC != "q":
    XYZ.append(ABC.split())
    ABC = input()
for want in input().split():
    for e in XYZ:
        if want == e[0]:
            total += float(e[1])
            break
print("total payment", total)