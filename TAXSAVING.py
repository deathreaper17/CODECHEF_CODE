T=int (input())
for i in range (T):
    X,Y= map(int,input().split())
    if X>Y :
        print(X-Y)
    elif X<Y:
        print(Y-X)
