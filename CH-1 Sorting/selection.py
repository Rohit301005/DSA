n = int(input())
myList = [int(ele) for ele in input().split()]

for i in range (n):
    minIndex = i
    for j in range(i,n):
        if myList[minIndex] > myList[j]:
            minIndex = j

    temp = myList[minIndex]
    myList[minIndex] = myList[i]
    myList[i] = temp

    print(myList)
    print("------")

print(myList)