Date = input().split("/")
Month = ["", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
print("*"*19 + "*"*len(Date[0]))
print("* DATE: {}.{}.{} *".format(Date[0],Month[int(Date[1])],Date[2]))
print("*"*19 + "*"*len(Date[0]))