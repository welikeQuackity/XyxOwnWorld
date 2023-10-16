1.
guy1 = int(input())
guy2 = int(input())
if guy1 > guy2 :
    print("нет")
if guy1 < guy2 :
    print("да")
else:
    print("не знаю")

2.
colour = int(input())
if colour > 36 or colour < 0:
    print("нет такого ответа, хаха")
if colour == 0:
    print ("зеленый")
if 1  <= colour <= 10:
    if colour % 2 == 0:
        print ("красные")
    else :
        print ("черные")
if 11 <= colour <= 28:
    if colour % 2 == 0:
        print ("красные")
    else :
        print("черные")
if 29 <= colour <= 36:
    if colour % 2 == 0:
        print("красные")
    else:
        print("черные")

  3.
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if b1 == a2  :
    print(b1)
if b2 == a1  :
    print (b2)
if b1 < a2 or a1 > b2 :
    print("пустое множество")
