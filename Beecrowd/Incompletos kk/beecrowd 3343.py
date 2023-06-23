N_Titans, Walls_Size = map(int, input().split(" "))
Titans_Size = input()
P, M, G = map(int, input().split())

N_Walls = [Walls_Size]

for Actual_Titan in Titans_Size:

    if(Actual_Titan == "P"):

        for x in range(len(N_Walls)):

            if(N_Walls[x] - P >= 0):
                N_Walls[x] -= P
            elif(x == len(N_Walls)-1):
                N_Walls.append(Walls_Size)
                N_Walls[-1] -= P

    elif(Actual_Titan == "M"):

        for x in range(len(N_Walls)):

            if(N_Walls[x] - M >= 0):
                N_Walls[x] -= M
            elif(x == len(N_Walls)-1):
                N_Walls.append(Walls_Size)
                N_Walls[-1] -= M

    else:

        for x in range(len(N_Walls)):

            if(N_Walls[x] - G >= 0):
                N_Walls[x] -= G
            elif(x == len(N_Walls)-1):
                N_Walls.append(Walls_Size)
                N_Walls[-1] -= G

print(len(N_Walls))