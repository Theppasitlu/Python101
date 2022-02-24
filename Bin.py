# HW6_LIST (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

# - เขียนในเซลล์นี้เท่านั้น 
# - ถ้าต้องการเขียนฟังก์ชันเพิ่ม ก็เขียนในเซลล์นี้

def compute_similarity(food_name1, food_name2):
  """
  รับ food_name1 และ food_name2 เป็นสตริงเก็บชื่ออาหารที่ตัดคำมาให้แล้ว โดยมีวรรคคั่นระหว่างคำ
  คืน ค่าความคล้ายของชื่ออาหาร ซึ่งเป็นเลขจำนวนจริงที่มีค่าระหว่าง [0,1]
  """
  f1 = food_name1.split()
  f2 = food_name2.split()
  a = 0
  for i in range(len(f1)):
      if f1[i] in f2:
        a +=1
  similarity = a*2/(len(f1)+len(f2)) 
  return similarity

# ---------------------------------------------------
def match_foods(nutrient, food_name):
  """
  รับ nutrient เก็บตารางข้อมูลโภชนาการรูปแบบของลิสต์ที่อธิบายข้างบน
  รับ food_name เป็นสตริงชื่ออาหารที่ผู้บริโภครับประทานที่ตัดคำมาให้แล้ว โดยมีวรรคคั่นระหว่างคำ
  คืน ลิสต์ผลลัพธ์ที่เก็บรหัสอาหาร food_id ที่มีชื่ออาหารตรงกับ food_name มากที่สุด รายละเอียดดังอธิบายไว้ข้างบน
  """
  fid,fn,n,m,end = [],[],[],[],[]
  for i in range(len(nutrient)):
    fid += [nutrient[i][0]]
    fn += [nutrient[i][1]]
  for i in range(len(fn)):
    n += [compute_similarity(food_name, fn[i])]
  Max = max(n)
  for i in range(len(n)):
    if Max == n[i]:
        m += [i]
  if Max <= 0.5:
    end = []
  else:
    for i in range(len(m)):
        end += [fid[m[i]]]
  return end
    
# ---------------------------------------------------
def get_nutrient(nutrient,food_name):
  """
  รับ nutrient เก็บตารางข้อมูลโภชนาการ ในรูปแบบของลิสต์
  รับ food_name เป็นสตริงชื่ออาหาร
  คืน ลิสต์ผลลัพธ์ที่เก็บข้อมูลพลังงานและสารอาหาร รายละเอียดดังอธิบายไว้ข้างบน
  """
  fid, kcal, carb, protein, fat, sugar, sodium = [], [], [], [], [], [], []
  kcal2, carb2, protein2, fat2, sugar2, sodium2 = 0, 0, 0, 0, 0, 0
  a1, a2, a3, a4, a5, a6 = 0, 0, 0, 0, 0, 0
  ends = []
  for i in range(len(nutrient)):
      fid += [nutrient[i][0]]
  fid_match = match_foods(nutrient, food_name)
  if not fid_match: ends = []   
  else:
    for i in range(len(fid_match)):
      n = fid.index(fid_match[i])
      kcal += [nutrient[n][2]]
      carb += [nutrient[n][3]]
      protein += [nutrient[n][4]]
      fat += [nutrient[n][5]]
      sugar += [nutrient[n][6]]
      sodium += [nutrient[n][7]]
    if len(fid_match) == 1 :
      end = [kcal, carb, protein, fat, sugar, sodium]
      for i in range(len(end)):
          if end[i][0] != 'NA' :
            ends += [float(end[i][0])]
          else: ends += [(end[i][0])]
    else : 
      for i in range(len(fid_match)):
          if kcal[i] == 'NA' : kcal2 += 0
          else : 
              kcal2 += kcal[i]
              a1 += 1
          if carb[i] == 'NA' : carb2 += 0
          else : 
              carb2 += carb[i]
              a2 += 1
          if protein[i] == 'NA' : protein2 += 0
          else : 
              protein2 += protein[i]
              a3 += 1
          if fat[i] == 'NA' : fat2 += 0
          else : 
              fat2 += fat[i]
              a4 += 1
          if sugar[i] == 'NA' : sugar2 += 0
          else : 
              sugar2 += sugar[i]
              a5 += 1
          if sodium[i] == 'NA' : sodium2 += 0
          else : 
              sodium2 += sodium[i]
              a6 += 1
      if a1 == 0 : a1 = 1
      if a2 == 0 : a2 = 1
      if a3 == 0 : a3 = 1
      if a4 == 0 : a4 = 1
      if a5 == 0 : a5 = 1
      if a6 == 0 : a6 = 1
      kcal2 = kcal2/a1
      protein2 = protein2/a2
      carb2 = carb2/a3
      fat2 = fat2/a4
      sugar2 = sugar2/a5
      sodium2 = sodium2/a6
      if kcal2 == 0 : kcal2 = 'NA'
      if protein2 == 0 : protein2 = 'NA'
      if carb2 == 0 : carb2 = 'NA'
      if fat2 == 0 : fat2 = 'NA'
      if sugar2 == 0 : sugar2 = 'NA'
      if sodium2 == 0 : sodium2 = 'NA'
      ends = [kcal2, carb2, protein2, fat2, sugar2, sodium2]
  return ends

 # ---------------------------------------------------
def summarize_daily_intake(nutrient, intakes):
  """
  รับ nutrient เก็บตารางข้อมูลโภชนาการ ในรูปแบบของลิสต์ที่อธิบายข้างต้น
  รับ intakes เก็บรายการการรับประทานอาหารของผู้ใช้ ในรูปแบบของลิสต์ที่อธิบายข้างต้น
  คืน ลิสต์ผลลัพธ์ที่เก็บข้อมูลสรุปโภชนาการสารอาหารที่ได้รับในแต่ละวัน รายละเอียดตามที่อธิบายข้างบน
  """
  nut = [] #สารอาหาร
  day = ["NA", "NA", "NA", "NA", "NA", "NA"] #อาหารวันนั้น
  Sum = []
  k = 0
  in2 = [e for e in intakes]
  y = True
  # for i in range(len(intakes)):
  #   b += [intakes[i][1]]
  #   c = intakes[i][0].split('/')
  #   d = c[0] + c[1] + c[2]
  #   in2[i][0] = int(d)
  in2.sort(reverse=True)
  length = len(in2)  #11 range(11) --> 0 - 10 | (10+1) --> 11 | ((10+1)%11) --> 0
  nut = [get_nutrient(nutrient,in2[i][1]) for i in range(length)]
  # for i in range(len(in2)):
  #   nut += [get_nutrient(nutrient,in2[i][1])] 
    # intakes[i][1] = a[i]
  # for i in range(len(intakes)):
  #   if intakes[i][1] == '[]' :
  #     y = False 
  #     intakes[i][1] = [0,0,0,0,0,0,y]
  #   else : intakes[i][1] += [y]

  for i in range(length):    
    if in2[i][0] != in2[(i+1)%length][0]:
      for j in range(k, i+1):
        if nut[j]:
          for Eat in range(6):
            if day[Eat] != "NA" and nut[j][Eat] != "NA"   : day[Eat] += nut[j][Eat]
            elif day[Eat] == "NA" and nut[j][Eat] != "NA" : day[Eat] = nut[j][Eat]
        else:
          y = False        
      Sum.append([in2[i][0], day[0], day[1], day[2], day[3], day[4], day[5], y])
      k = i+1
      day = ["NA", "NA", "NA", "NA", "NA", "NA"]
      y = True
  return Sum


  # t = 0
  # r = []
  # last = []
  # r1,r2,r3 = intakes[0][1][0], intakes[0][1][1], intakes[0][1][2]
  # r4,r5,r6 = intakes[0][1][3], intakes[0][1][4], intakes[0][1][5]
  # r7 = []
  # for i in range(len(intakes)-1):
  #   for i in range(len(intakes[i][1])):
  #       if intakes[i][1][t] == 'NA' : intakes[i][1][t] = 0
            
  #   if intakes[i][0] == intakes[i+1][0] :
  #     r1 += intakes[i+1][1][0]
  #     # r2 += intakes[i+1][1][1]
  #     # r3 += intakes[i+1][1][2]
  #     # r4 += intakes[i+1][1][3]
  #     # r5 += intakes[i+1][1][4]
  #     # r6 += intakes[i+1][1][5]
  #     r7.append(r1)
        
  #   else : 
  #     r1,r2,r3 = intakes[i+1][1][0], intakes[i+1][1][1], intakes[i+1][1][2]
  #     r4,r5,r6 = intakes[i+1][1][3], intakes[i+1][1][4], intakes[i+1][1][5]
  #   # last += r7
  #   # print(r7)  
      
  # # last += [r1]
  
  # for i in range(len(intakes)):
  #   print(intakes[i])
  # z = 0




# ---------------------------------------------------
def main():

  nutrient = [['R010007', 'ลาบ หมู', 267, 17, 23, 12, 2, 1470],
              ['R010014', 'ส้มตำ ไทย', 143, 143, 31, 5, 27, 1064],
              ['R010005', 'ก๋วยเตี๋ยว ผัดไทย ใส่ ไข่', 447, 49, 21, 18, 'NA', 1139],
              ['P010019', 'ขนมจีน ซาวน้ำ', 437, 62, 9, 17, 'NA', 810],
              ['P010021', 'ขนมจีน น้ำยา', 348, 41, 14, 14, 11, 1210],
              ['P010023', 'ขนมจีน น้ำพริก', 497, 75, 11, 17, 'NA', 'NA'], 
              ['P010041', 'ข้าว หมก ไก่', 481, 74, 19, 12, 'NA', 900],
              ['P020008', 'ข้าว ราด กะเพรา ไก่', 458, 60, 20, 15, 'NA', 1200],
              ['P010049', 'ข้าว ไข่ พะโล้', 464, 55, 20, 18, 'NA', 946],
              ['P010025', 'ข้าว ไก่ ผัด กะเพรา', 432, 54, 20, 15, 'NA', 'NA'],
              ['F010003', 'กล้วย ไข่', 62, 14, 0, 0, 7, 4],
              ['D010032', 'บัวลอย เผือก', 336, 62, 2, 9, 'NA', 'NA'],
              ['D010033', 'ลำใย เผือก', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']]
              
  intakes = [['2022/01/15', 'ลาบ หมู'],
             ['2022/01/15', 'ส้มตำ ไทย'],
             ['2022/01/18', 'กาแฟ เย็น'], 
             ['2022/01/14', 'แซนวิซ'],
             ['2022/01/19', 'ซาวน้ำ'],
             ['2022/01/15', 'ขนมจีน น้ำยา'],
             ['2022/01/16', 'ขนมจีน น้ำพริก'],
             ['2022/01/16', 'ส้มตำ ไทย'],
             ['2022/01/06', '茄子鸡丁'],
             ['2022/01/16', 'สลัด ทูน่า'],
             ['2022/01/18', 'ข้าว ไก่ ผัด กะเพรา'],
             ['2022/01/18', 'ส้มตำ ไทย'],
             ['2022/01/18', 'แตงโม'],
             ['2022/01/14', 'ส้มตำ ไทย'],
             ['2022/01/14', 'ลาบ หมู'],
             ['2022/01/19', 'บัวลอย']]

  # print(compute_similarity('ข้าว กะเพรา ไก่', 'ข้าว ไก่ ผัด กะเพรา'))
  # print(match_foods(nutrient, 'ข้าว กะเพรา ไก่'))
  # print(get_nutrient(nutrient,'ข้าว กะเพรา ไก่'))    
  # print(get_nutrient(nutrient,'ห่อ หมก')) 
  # print(summarize_daily_intake(nutrient, intakes))
  for e in summarize_daily_intake(nutrient, intakes): print(e)
  

#   print(get_nutrient(nutrient,'ห่อ หมก'))
#   print(get_nutrient(nutrient,'บัวลอย เผือก'))
#   print(get_nutrient(nutrient,'ข้าว กะเพรา ไก่'))
#   print(get_nutrient(nutrient,'ลำใย เผือก'))

main()

