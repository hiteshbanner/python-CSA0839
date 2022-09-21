def sumsq(l):
    even=0
    odd=0
    for i in range(len(l)):
        if(l[i]%2==0):
            even=even+l[i]**2
        else:
            odd=odd+l[i]**2
        

        
    l=[odd,even]
    return(l)
    



n=int(input("enter the no element:"))
l=[]
for i in range(n):
    l.append(int(input("enter the elemnet:")))
print(sumsq(l))
                 
