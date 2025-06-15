o = [0,0,0]
s = [0,0,0]
print("chose num from 1 to 9 ")
print("if your number in this say (yas) ")
oa = input("5 / 6 / 2 / 1 / 7 / 4 : ")
ob = input("8 / 9 / 3 / 1 / 4 / 7 : ")
oc = input("8 / 6 / 2 / 9 / 3 / 5 : ")  
sa = input("1 / 5 / 2 / 8 / 4 / 3 : ")
sb = input("4 / 7 / 9 / 6 / 5 / 8 : ")
sc = input("1 / 7 / 2 / 9 / 6 / 3 : ")
if oa == "yas":
    o[0] = 1
if ob == "yas" :
    o[1] = 1
if oc == "yas"  :
    o[2] = 1
if sa == "yas":
    s[0] = 1
if sb == "yas":
    s[1] = 1
if sc == "yas":
    s[2] =1        
tt = o,s
if o == [1, 1, 0] and s == [1, 0, 1]:
    print("your number is 1")
if o == [0, 1, 1] and s == [1, 0, 1]:
    print("your number is 3")
if o == [1, 1, 0] and s == [1, 1, 0]:
    print("your number is 4")
if o == [1, 0, 1] and s == [1, 1, 0]:
    print("your number is 5")
if o == [1, 0, 1] and s == [0, 1, 1]:
    print("your number is 6")
if o == [1, 1, 0] and s == [0, 1, 1]:
    print("your numbr is 7")
if o == [0, 1, 1] and s == [1, 1, 0]:
    print("your number is 8")
if o == [0, 1, 1] and s == [0, 1, 1]:
    print("your number is 9")
if o == [1, 0, 1] and s == [1, 0, 1]:
    print("your number is 2")