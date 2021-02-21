# Queue Implement using List
# FIFO---->First in First Out
queue=[]
def enqueue():
    ele=int(input("Enter the element "))
    queue.append(ele)
    print(ele," is added to queue ")

def dequeue():
    if not queue:
        print("Queue is empty ")
    else:
        e=queue.pop(0)
        print("removed element : ",e)

def display():
    print(queue)

while True:
    print("--------Queue operation--------")
    print("Press 1 for enqueue ")
    print("Press 2 for dequeue ")
    print("Press 3 for display ")
    print("Press 4 for exit ")
    ch=int(input())
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
