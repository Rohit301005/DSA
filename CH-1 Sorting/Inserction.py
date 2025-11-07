n = int(input())
myList = [int(ele) for ele in input().split()]

for i in range(1,n):
    key = myList[i]
    j = i  -1

    while j >= 0 and myList[j] > key:
        myList[j +1] = myList[j]
        j -= 1

    myList[j + 1] = key

    print(myList)
    print("-------")

print(myList)