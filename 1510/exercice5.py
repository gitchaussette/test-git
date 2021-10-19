print()
# 1
list = [17, 38, 10, 25, 72]
list.sort()
print(list)

print()
# 2
list.append(12)
print(list)

print()
# 3
list.reverse()
print(list)

print()
# 4
print(list.index(17))

print()
# 5
list.remove(38)
print(list)

print()
# 6
print(list[1:3])

print()
# 7
print(list[:2])

print()
# 8
print(list[2:])

print()
# 9
print(list[-1])

print()
# 10
# stringsOfList = str(list).strip("[]")
# print(stringsOfList)
# print(':'.join(stringsOfList))
stringList = ":".join(str(i) for i in list)
print(stringList)

print()
# 11
stringList += ":175"
print(stringList)

print()
#12

re_list = stringList.split(":")
print(re_list)

