zodiac_years = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
Date = input().split()
if 2 <= int(Date[0]) <= 12: print(zodiac_years[(int(Date[1])+8)%12])
else : print(zodiac_years[(int(Date[1])+7)%12])