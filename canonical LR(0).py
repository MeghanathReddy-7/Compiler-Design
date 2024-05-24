class prod:
    def __init__(self,l='',r=''):
        self.l=l
        self.r=r
n=int(input("Enter the number of productions:"))
op=[]
for i in range(n):
    l = input("left: ")
    r = input("right: ")
    op.append(prod(l,r))
first=prod()
first.l=op[0].l+"'"
first.r=op[0].l
max=0
print("I0:")
print(first.l+"->"+"."+first.r)
for i in range(n):
    print(op[i].l+"->."+op[i].r)
    if len(op[i].r)>max:
        max=len(op[i].r)
print("I1:")
print(first.l+"->"+first.r+".")
k=2
for m in range(1,max+1):
    for j in range(n):
        if(len(op[j].r)>m-1):
            print("I"+str(k)+":")
            k+=1
            print(op[j].l+"->"+op[j].r[:m]+"."+op[j].r[m:])