class Stack:
    def __init__(self):
        self.items=[]
    def  push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
e=input("Enter the input:")
s=Stack()
flag=0
OB="[({"
CB=")}]"
for i in e:
    if i in OB:
        s.push(i)
    if i in CB:
        x=s.pop() 
        if x=="(" and i== ")":
            pass
        elif x=="{" and i=="}":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag=1
            break
if flag==0 and s.size()==0 :
   print("valid")
else:
   print("invalid")        
    
        