stack_size=5
list=[None]*stack_size
top=-1

def isEmpty():
   if top== -1: return True
   else : return False
       
        
def isFull():
    return stack_size-1 == top
    
def push(e):
    global top
    if not isFull():
        top=top+1
        list[top]=e
        print(list)
    else:
        print("stack overflow")
        exit()
        
def pop():
    global top
    if not isEmpty():
        top=top-1
        return list[top+1]
    else:
        print("stack overflow")
        exit()

def peek():
    if not isEmpty():
        return list[top]
    else:pass
    
push(1)
push(1)
push(1)
push(1)
push(1)
   