# Insertion sort program using Python
def InsertionSort(lst):
    for i in range(1,len(lst)):
        ele=lst[i]
        position=i
        while ele < lst[position-1] and position > 0 :
            lst[position]=lst[position-1]
            position=position-1
        lst[position]=ele
list1=[20,40,30,50,10,60]
InsertionSort(list1)
print(list1)
