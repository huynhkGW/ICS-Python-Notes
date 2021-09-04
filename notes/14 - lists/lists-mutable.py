
import copy
a = 3
b = a  #Integers are immutable, so a new variable b is created that stores the VALUE that is currently stored in A
b = 2
print(f' The value stored in a is: {a}')
print(f' The value stored in b is: {b}')


listA = [1,2,3]
listB = listA  #Lists are mutable, so a new variable is created that stores the REFERENCE to listA
listC = copy.deepcopy(listA)
listB[0] = 9999
listC[1] = 'CCCC'
print(f' The value stored in listA is: {listA}')
print(f' The value stored in listB is: {listB}')


print('\r\n'*5)



#How does this change when working with functions?
def changeNumber(numberIn):
    numberIn = numberIn + 1
    print(f' Inside changeNumber function numberIn is: {numberIn}')


def changeList(listIn):
    listIn.append('CAT')
    print(f' Inside changeList function listIn is: {listIn}')



number = 0
changeNumber(number)
print(f' At end of program number is: {number}')


numberList = [0,1,2,3]
changeList(numberList)
print(f' At end of program number is: {numberList}')
