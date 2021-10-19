numList = [1,2,3,4,5]
alphaList = ["a","b","c","d","e"]
print(numList is alphaList)
print(numList == alphaList)
numList = alphaList
print(numList is alphaList)
print(numList == alphaList)

# print(numList is alphaList) -> False
# print(numList == alphaList) -> False
# print(numList is alphaList) -> True
# print(numList == alphaList) -> True
