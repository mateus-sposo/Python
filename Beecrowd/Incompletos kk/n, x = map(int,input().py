n, x = map(int,input().split())
LT = input()
p, m, g = map(int, input().split())
c = 0
M = x
NM = 1
Ma = [0, 0, 0, 0, 0, 0, 0]
c1 = 0
while c < n:
    if ord(LT[c]) == ord("P"):
        if Ma[c1] >= p:
            Ma[c1] = Ma[c1] - p
            if Ma[c1] < p:
                c1 = c1 + 1
        else: 
            if M >= p: 
                M = M - p                
            else:    
                M = x
                M = M - p
                NM = NM + 1
    elif ord(LT[c]) == ord("M"):
        if Ma[c1] >= m:
            Ma[c1] = Ma[c1] - m
            if Ma[c1] < p:
                c1 = c1 + 1
        else:
            if M >= p:
                if Ma[c1] < p:
                    Ma[c1] = M
                    M = x
                    M = M - m
                    NM = NM + 1
                else:    
                    Ma[c1 + 1] = M
                    M = x
                    M = M - m
                    NM = NM + 1
            else:
                M = x
                M = M - m
                NM = NM + 1
    else:
        if M >= g:
            M = M - g
        else:
            if M > m:
                if Ma[c1] < p:
                    Ma[c1] = M
                    M = x
                    M = M - g
                    NM = NM + 1
                else:    
                    Ma[c1 + 1] = M
                    M = x
                    M = M - g
                    NM = NM + 1
            else:    
                if M > p:
                    if Ma[c1] < p:
                        Ma[c1] = M
                        M = x
                        M = M - g
                        NM = NM + 1
                    else:
                        if Ma[c1 + 1] >= p:
                            Ma[c1 + 2] = M
                            M = x
                            M = M - g
                            NM = NM + 1 
                        else:   
                            Ma[c1 + 1] = M
                            M = x
                            M = M - g
                            NM = NM + 1    
                else:    
                    M = x 
                    M = M - g
                    NM = NM + 1   
    c = c + 1
print(NM)