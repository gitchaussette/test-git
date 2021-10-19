# Variables

a = 6
b = 7
c = 7
f = "Hello world!"
g = f + " coucou"
h = g + str(a)
i = 54
j = 25 % 2
k = 12 ** 2
l = 25 // 6
m = 12.5
n = 4, 20, 6, 9
boolean = True

# print()
# print("a = " + str(a))
# print("b = " + str(b))
# print("c = " + str(c))
# print(g)
# print(h)
# print("Vous avez " + str(i) + " € sur votre compte, espèce de gros pauvre")
# print()
# print()

# Conditions

# print()
# if a >= 5 :
#     b = 10
# elif a < 3 :
#     b = 12
# else :
#     b = 25

print(b)
print(j)
print(k)
print(l)
print(type(m))
print(n)
print()

if a < b :
    print("a is inferior to b")
elif a == b :
    print("a is b")
elif a != b :
    print("a is not b")
elif a > b :
    print("a is superior to b")
else :
    print("egg")

aa = True
bb = 12

if aa == True :
    bb = 15
    aa = False
else :
    bb = 12
    aa = True

print(aa)

# zgeg = "8======D"
# boolbool = False

# if var1 and var2 == 9 :
#     print("noice")

# if var1 or zgeg == "8======D":
#     print(zgeg)

# if var1 or not boolbool:
#     print("???")

var1 = 9
var2 = 68
var3 = 70

print(var1)
print(var2)
print(var3)

if var1 == 9 :
    if var2 == 69 :
        print("ouyé")
    elif var3 > 69 :
        print("oh no")
    else :
        print("???")

else :
    print("la truite s'est échappée")

print("j'ai dit : \"que j\'étais désolé\"")

answer = input("répondre oui ou non : ")
print(answer)