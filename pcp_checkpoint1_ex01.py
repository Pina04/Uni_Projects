#First give the value in REAIS to the user choose

valor_real  = float(input("De o valor em real"))

dolar = valor_real / 5.75

euro = valor_real / 6.23

peso_argentino = valor_real / 0.005

libra = valor_real / 7.46

iene = valor_real / 0.39


print(f"Valor em Real: {valor_real:.2f}")
print(f"Valor em Dólar:{dolar:.2f}")
print(f"Valor em Euro:{euro:.2f}")
print(f"Valor em Peso Argentino:{peso_argentino:.2f}")
print(f"Valor em Líbra:{libra:.2f}")
print(f"Valor em Iene:{iene:.2f}")






