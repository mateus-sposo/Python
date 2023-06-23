V1 = input().split()
V2 = input().split()
FR = []
FR.append(int(V1[0]) + int(V2[0]))
FR.append(int(V1[1]) + int(V2[1]))
FR.append(int(V1[2]) + int(V2[2]))
print(f"Força resultante: ({FR[0]}, {FR[1]}, {FR[2]})")