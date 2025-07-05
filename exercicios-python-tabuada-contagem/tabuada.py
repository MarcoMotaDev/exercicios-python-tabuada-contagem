# tabuada.py

# Solicita um número do usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Mostra a tabuada de 1 a 10
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
