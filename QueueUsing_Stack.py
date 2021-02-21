#Implement Queue using stack-(two)
stack1=[]
stack2=[]
def enqueue():
    if len(stack1)==5:
        print("Queue is Overflow")
    else:
        ele=int(input("Enter the element : "))
        stack1.append(ele)
        print("Push element is : ",ele)

def dequeue():
    if not stack1 and not stack2:
        print("Queue is Empty")
    else:
        for i in range(len(stack1)):
            ele=stack1.pop()
            stack2.append(ele)
        e=stack2.pop()
        print("Pop element is : ",e)
        for i in range(len(stack2)):
            a=stack2.pop()
            stack1.append(a)
def display():
    print("Queue elements are : ",stack1)

while True:
    print("----------Queue Operation----------")
    print("Press 1 for enqueue")
    print("Press 2 for dequeue")
    print("Press 3 for display")
    print("Press 4 for exit")
    ch=int(input())
    print("-----------------------------------")
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Please enter a valid input")



