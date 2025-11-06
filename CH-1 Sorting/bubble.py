n = int(input())
myList = [int(ele) for ele in input().split()]

for i in range(n-1):
    isSwaped = False
    for j in range(n-i-1):
        if myList[j] > myList[j+1]:
            isSwaped = True
            temp = myList[j]
            myList[j] = myList[j+1]
            myList[j+1] = temp
    
    if isSwaped == False:
        break
    


print(myList)