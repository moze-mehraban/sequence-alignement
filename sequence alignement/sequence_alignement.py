
def s(c1,c2):
    if c1==c2:
        return 1
    else :
        return -1

n ,m = map(int,input().split())
a=input()
b=input()
c = [[0 for i in range(m+1)] for j in range(n+1)]
d = [[ " " for i in range(m+1)] for j in range(n+1)]
for i in range (n+1):
    c[i][0]=-i
for i in range (m+1):
    c[0][i]=-i
for i in range (1,n+1):
    for j in range(1,m+1):
        arr=[c[i-1][j-1]+s(a[i-1],b[j-1]),c[i-1][j]-1,c[i][j-1]-1]
        ma=max(arr)
        c[i][j]=ma
        if arr.index(ma) == 0:
            d[i][j]="d"
        if arr.index(ma) == 1:
            d[i][j]="u"
        if arr.index(ma) == 2:
            d[i][j]="l"

# for row in c:
#     print(*row, sep="\t")
# print(10*"___")
# for row in d:
#     print(*row, sep="\t")
i=m
j=n
gapa=0
gapb=0
mc=0
while i!=0 and j!=0 :
    #print(i,j)
    if d[j][i]=="d":
        if a[j-1]!=b[i-1]:
            mc+=1
        i-=1
        j-=1
    elif d[j][i]=="u":
        j-=1
        gapb+=1
    elif d[j][i]=="l":
        i-=1
        gapa+=1
print(mc,gapa,gapb,sep="\n")