
#Make the user put a random number with a limit of 3 digits
numero = int(input("Digite um Número"))

#Now we make the separations of the number in terms of hundres, ten and unit
centena = (numero // 100) * 100
dezena = ((numero % 100) // 10) * 10
unidade = numero % 10
#Afer all that now we print the results
print(f"Centena = {centena}")
print(f"Dezena = {dezena}")
print(f"Unidade = {unidade}")