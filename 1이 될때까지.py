'''
N에서 1을 뺀다
N을 K로 나눈다
'''

n,k=map(int,input().split())
count=0
while True:
    if n%k==0:
        n=n/k
    else :
        n-=1
    count+=1
    if n==1:
        break
print(count)



