n=list(map(int,input().split()))
if len(n)==0:
    print("empty")
else:
    max_index=0
    for i in range(1,len(n)):
        if(n[i]<n[max_index]):
                max_index=i
    print(max_index)        
    
    