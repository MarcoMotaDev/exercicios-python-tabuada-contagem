# contagem_regressiva.py

# Solicita um número do usuário
numero = int(input("Digite um número para iniciar a contagem regressiva: "))

# Mostra a contagem de forma decrescente até 0
print("\nContagem regressiva:\n")
for i in range(numero, -1, -1):
    print(i)
