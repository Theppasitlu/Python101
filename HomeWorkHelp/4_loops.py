# HW5_LOOPS (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

# - เขียนในเซลล์นี้เท่านั้น 
# - ถ้าต้องการเขียนฟังก์ชันเพิ่ม ก็เขียนในเซลล์นี้
import time
def position_numbers(n):
    """
    รับ n เก็บจำนวนเต็มบวก
    คืน ลิสต์ posnums ขนาดอย่างน้อย 2 ช่องที่เก็บ position numbers 
        ตั้งแต่ตัวแรกไปเรื่อย ๆ โดย posnums[-2] ≤ n < posnums[-1]
    เช่น position_numbers(1) คืน [1, 2]
        position_numbers(2) คืน [1, 2, 5]
        position_numbers(3) คืน [1, 2, 5]
    """
    NLists = [1]
    Number = 1
    Count = 0
    First = 1
    Second = 3

    while Number <= n:
        if Count%2 == 0:
            # Number += 1 + Count//2
            Number += First
            First += 1
            NLists += [Number]
        else:
            # Number += 3 + 2*Count//2
            Number += Second
            Second += 2
            NLists += [Number]
        Count += 1
    return NLists
            
# print(position_numbers(200))
# ---------------------------------------------------
def next_partition_number(p, posnums):
    """
    กำหนดให้ m คือขนาดของลิสต์ p
    รับ p เป็นลิสต์มี p[0], p[1], ..., p[m-1] 
       เก็บ partition numbers ตัวที่ 0 ถึง m-1 ตามลำดับ
    รับ posnums เป็นลิสต์เก็บ position numbers ตั้งแต่ตัวแรกไปเรื่อย ๆ 
       โดย posnums[-1] > m
    คืน partition number ตัวที่ m (ขอเน้นว่า ไม่ต้องเพิ่มใน p)
    เช่น next_partition_number([1], [1,2,5,7,12]) คืน 1
        next_partition_number([1,1,2,3,5,7], [1,2,5,7]) คืน 11
    หมายเหตุ: ห้ามแก้ไขข้อมูลในลิสต์ p และ posnums โดยเด็ดขาด
    """
    #       p[6] = p[6-1] + p[6-2] - p[6-5] #!- p[6-7] + p[] + p[] - p[] - p[]
                #=   7    +    5   -   1  --> 11
    m = len(p)
    part = 0
    i = 0
    while m - posnums[i] >= 0:
        if i%4 in [0, 1]:
            part += p[m - posnums[i]]
        else:
            part -= p[m - posnums[i]]
        if m - posnums[i] == 0:
            break
        i += 1
    return part

# print(next_partition_number([1,1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,297,385,490], [1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70, 77, 92, 100, 117, 126, 145, 155, 176, 187, 210]))
# ---------------------------------------------------
def rhs_of_pn(n, posnums):
    """
    รับ n เก็บจำนวนเต็มบวก
    รับ posnums เป็นลิสต์เก็บ position numbers ตั้งแต่ตัวแรกไปเรื่อย ๆ 
       โดย posnums[-1] > n
    คืน สตริง ที่เก็บวิธีคำนวณค่า p(n) ซึ่งคือส่วนทางขวามือของสมการ p(n)
    เช่น rhs_of_pn(1, [1,2,5])      คืน 'p(0)'
        rhs_of_pn(5, [1,2,5,7,12]) คืน 'p(4) + p(3) - p(0)'
    หมายเหตุ: ห้ามแก้ไขข้อมูลในลิสต์ posnums โดยเด็ดขาด
             สังเกตให้ดีว่า ต้องมีช่องว่างคั่นเครื่องหมาย + หรือ - ด้วย
    """
    Answer = ""
    i = 0
    while n - posnums[i] >= 0:
        if i == 0:
            Answer += "p(" + str(n - posnums[i]) + ")"
        elif i%4 in [0, 1]:
            Answer +=  " + p(" + str(n - posnums[i]) + ")"
        else:
            Answer += " - p(" + str(n - posnums[i]) + ")"
        i += 1
    return Answer
# print(rhs_of_pn(5, [1,2,5,7,12]))

# ---------------------------------------------------
# ไม่ต้องแก้ไขอะไรใด ๆ ในชุดคำสั่งข้างล่างนี้
def main(n, show_rhs):
    n = int(n)
    posnums = position_numbers(n)
    p = [1]  # p[0] = 1
    for m in range(1, n+1):
        p += [ next_partition_number(p, posnums) ]
    out = 'p(' + str(n) + ') = '
    if show_rhs == 'Y':
        out += rhs_of_pn(n, posnums) + ' = '
    out += str(p[n])
    print(out)

def least_pn_having(x):

    Want = False
    Data = [1]
    k = 0
    poslist = []
    odd = 1
    even = 1
    po = 0
    while not Want:
        if k%2 == 1:
            po += odd 
            poslist += [po]
            odd += 1
        else: 
            po += even
            poslist += [po] 
            even += 2
        Data += [next_partition_number(Data, poslist)]
        j = 0
        Temp = str(Data[k])
        for ch in str(x):
            for i in range(j, len(Temp)):
                if ch == Temp[i]:
                    j = i+1
                    break
            else:
                break
        else:
            Want = True
            return Temp
        k += 1

def CheckRunTime():
    start = time.time()
    print(least_pn_having(6430221921))  
    stop = time.time()
    print("ใช้เวลา {}".format(stop-start))
CheckRunTime()