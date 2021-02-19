def BinarySearch(l,h,key):
    if l==h:
        if A[l]==key:
            return 1
        else:
            return 0
    else:
        mid=(l+h)//2
        if A[mid]==key:
            return mid
        if key < A[mid]:
            return BinarySearch(l,mid-1,key)
        else:
            return BinarySearch(mid+1,h,key)

# A=[3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
A=[10,20,30,40,50,60,70,80]
print("Enter the Element to check which value are available in the list or Not ")
key=int(input())
result=BinarySearch(1,len(A),key)
print(result)
