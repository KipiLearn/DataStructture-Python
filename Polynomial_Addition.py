ACof=[5,6,5,4,6,2]
AExp=[5,4,3,2,1,0]
BCof=[2,-7,3,1]
BExp=[3,2,1,0]
CCof=[]
CExp=[]
#To find the maximum lenth of two polynomial Eqaution
if len(ACof)>len(BCof):
    l=len(ACof)
else:
    l = len(BCof)
# Assign Both array are Equality
for k in range(l):
    if AExp[k] > BExp[k] :
        BExp.insert(k,0)
        BCof.insert(k,0)
    if AExp[k] < BExp[k]:
        AExp.insert(k,0)
        ACof.insert(k, 0)
# After Assign both array are-------------------------
print('-----------------------------------------------------------')

# print the Value of 1st equation
for k in range(l):
    print("(%+d" % ACof[k], '^', AExp[k], ')', end=' ')
print()

# print the Value of 2nd equation
for k in range(l):
    print("(%+d" % BCof[k], '^', BExp[k], ')', end=' ')

# addition two polynomial function
for i in range(l):
    if AExp[i]==BExp[i]:
        CCof.append(ACof[i]+BCof[i])
        CExp.append(AExp[i])
    else:
        if AExp[i]>BExp[i]:
            CCof.append(ACof[i])
            CExp.append(AExp[i])
        else:
            CCof.append(BCof[i])
            CExp.append(BExp[i])

print()
print('-----------------------------------------------------------')
#print the two polynomial addition value
for j in range(len(CCof)):
    print("(%+d" %CCof[j],'^',CExp[j],')' ,end=' ')



