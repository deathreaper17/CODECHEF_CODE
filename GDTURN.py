dice= int (input())


for i in range (dice):
    a,b =map(int ,input().split())

    sum=a+b

    if sum >6:
        print("YES")
    else:
        print("NO")
