#Exercício 1

base1, lado1 = map(float, input().split())
base2, lado2 = map(float, input().split())

Area1 = base1 * lado1
Area2 = base2 * lado2

print(f"Area A: {Area1:.2f}")
print(f"Area B: {Area2:.2f}")

if Area1 > Area2: 
	print("O retângulo A é maior que o retângulo B.")
elif Area1 < Area2: 
	print("O retângulo B é maior que o retângulo A.")
elif Area1 == Area2: 
	print("As áreas dos retângulos são iguais.")