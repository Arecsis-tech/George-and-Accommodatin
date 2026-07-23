n=int(input())
f=0
for i in range(n):
    p,c=map(int,input().split())
    if p<=(c-2):
        f=f+1
print(f)
