hello = input().split(":")
Name,Date = hello[0].split(","),hello[1].split("/")
print(Name[1],Name[0]+":",Date[1],Date[0]+',',Date[2])