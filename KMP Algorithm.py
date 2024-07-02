def KMPalgo(P,S):
    M=len(P)
    N=len(S)
    LPS(P,M,lps)
    print(lps)
    i=0
    j=0
    while (N-i)>=(M-j):
        if P[j]==S[i]:
            i+=1
            j+=1
        if j==M:
            print("pattern found",i-j)
            j=lps[j-1]
        elif i<N and P[j]!=S[i]:  
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
                
def LPS(P,M,lps):
    lps.append(0)
    j=0
    for i in range(1,len(P)):
        if P[i]==P[j]:
            lps.append(j+1)
            j+=1
        else:
            j=0
            lps.append(j)
        
if _name=='main_':
    S="ABABACDEABABABCABCABCABEAA"
    P="ABCAB"
    KMPalgo(P,S)