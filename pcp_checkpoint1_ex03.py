anos = int(input("Digite quantos anos você tem: "))
meses = int(input("Digite quantos meses você tem: "))
dias = int(input("Digite quantos dias você tem: "))
# Calcular a idade total em dias
idade_total_dias = (anos * 365) + (meses * 30) + dias
# Calcular o total de dias que a pessoa viveu
print(f"Você viveu aproximadamente {idade_total_dias} dias.")