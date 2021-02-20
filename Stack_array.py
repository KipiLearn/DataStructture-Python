# Stack Implementation using python
stack=[]
def push():
    if len(stack)==5:
        print("Stack is Overflow")
    else:
        ele=int(input("Enter the element : "))
        stack.append(ele)
        print(stack," Push element is : ",stack[-1])

def pop():
    if not stack:
        print("stack is empty")
    else:
        print("pop element is : ",stack.pop())
def top():
    print("Top element is : ",stack[-1])
def display():
    print("Stack=",stack[0:])

while True:
    print("--------Stack operation--------")
    print("Press 1 for Push")
    print("Press 2 for Pop")
    print("Press 3 for Top")
    print("Press 4 for Display")
    print("Press 5 for Quit")
    ch=int(input())
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        top()
    elif ch==4:
        display()
    elif ch==5:
        break
    else:
        print("Choose the correct Option ")


