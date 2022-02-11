mima = input().strip()
out = ""
for i in range(len(mima)):
    if "A" <= mima[i] <= "Z" or "a" <= mima[i] <= "z":
        out += "*"
    elif "0" <= mima[i] <= "9":
        out += "#"
    else:
        out += mima[i]
print(out,end="")