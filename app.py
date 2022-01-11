#Function to sort the inputs using x1 as primary and height as secondary key
#x1 is asc order where as height in desc order

def init_sort(ls):
    ls.sort(key = lambda x: (x[0],x[2]))
    temp=-1
    for i in range(1,len(ls)):
        if ls[i][0]==ls[i-1][0]:
            if temp==-1:
                temp=i-1
            if i==len(ls)-1:
                ls[temp:i+1]=ls[temp:i+1][::-1]
        else:
            if temp!=-1:
                ls[temp:i]=ls[temp:i][::-1]
                temp=-1
    return ls


#Calculate drops and rise below
def calc(ls):
    res=[]
    res.append((ls[0][0],ls[0][2]))
    for i in range(1,len(ls)):
        if ls[i-1][1] < ls[i][0] and res!=[]:
            res.append((ls[i-1][1],0))
            res.append((ls[i][0],ls[i][2]))
            if i==len(ls)-1:
                res.append((ls[i][1],0))
            continue
        if ls[i][2]<ls[i-1][2] and ls[i][1]>ls[i-1][1]:
            res.append((ls[i-1][1],ls[i][2]))
        elif ls[i][2]>ls[i-1][2]:
            res.append((ls[i][0],ls[i][2]))
            if ls[i][1]<ls[i-1][1]:
                res.append((ls[i][1],ls[i-1][2]))
        if i==len(ls)-1:
            if ls[i-1][1] > ls[i][1]:
                res.append((ls[i-1][1],0))
            else:
                res.append((ls[i][1],0))
        
    return res

#insert input as inp
inp=[(1,5,10),(4,6,8),(10,15,10),(11,12,8)]
inp=init_sort(inp)
print('Output is : ',calc(inp))


        
     