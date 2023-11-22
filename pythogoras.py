def gettriad1():
    list1=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    list2=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    triad1=[]
    for j in range(0,15,1):
        p1=list1[j]**2
        for i in range(0,15,1):
            p2=list2[i]**2
            p3=(p1+p2)**0.5
            p33=int(p3)
            diff=p3-p33
            if diff==0:
                temp1=(list1[j],list2[i],p33)
                temp2=set(temp1)
                triad1.append(temp2)
    print(triad1)

gettriad1()
