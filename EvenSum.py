def SumOfList():
    nums = []
    oddsum = 0
    evensum = 0
    lenght = int(input())
    for i in range(lenght):
        nums.append(int(input()))
    for i in nums:
        if i%2 == 0:
            evensum+=i 
        else:
            oddsum+=1

    print("evensum-"+ str(evensum))
    print("oddsum-"+str(oddsum))

def findMax():
    nums = []
    lenght = int(input())
    for i in range(lenght):
        nums.append(int(input()))
    maxnum = nums[i]
    for i in nums:
        if i > maxnum:
            maxnum = i
    print("max:-",end=" ")
    print(maxnum)

def reverse():
    liststr = ["abhi","jeeth","sad","done"]
    res = ""
    for i in liststr[::-1]:
        res+=i
    print(res)

def hello():
    filename = input()
    f = open(filename, "r")
    a = f.read().split(" ")
    a.sort()
    print(a)


def hello2():
    filename = input()
    f = open(filename, "r")
    lines = f.read().splitlines( )
    f.close()
    f = open(filename, "r")
    words = f.read().split(" ") 
    f.close()
    f = open(filename, "r")
    charecters = [*f.read()]
    f.close()
    print('words ',len(words))
    print('charecters ' , len(charecters))
    print('lines ', len(lines))
hello2()

