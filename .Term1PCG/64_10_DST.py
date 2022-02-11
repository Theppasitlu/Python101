Sports = {Name:set(Data.split(",")) for Name, Data in (input().split() for i in range(int(input())))}
Data = input()
while Data != "q":
    First, Second = Data.split()
    print(sorted(Sports[First] & Sports[Second]))
    Data = input()