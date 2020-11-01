#min,max사용 안함 이중포문

n,m=map(int,input().split())
result=0
for i in range(n):
    data=list(map(int,input().split()))
    min_num=10001
    for j in data:
        if min_num > j:
            min_num=j;
    if result < min_num:
        result=min_num
print(result)