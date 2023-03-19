T=int(input())
for i in range (T):
    X,Y,age = map(int, input().split())
    if age>= X and age<Y:
        
        print("YES")
    else:
        print("NO")
        
    