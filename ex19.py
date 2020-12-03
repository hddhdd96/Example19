n = int(input())
s=1
if(n==1):
    print(1)
else:
    for x in range(n):
        s = s + 6*x
        if(s>n):
            print(x+1)
            break


    # 1 + 6 / 2
    # 1 + 6 + 12 / 3


