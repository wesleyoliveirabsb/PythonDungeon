print("bem vindo a roda gigante")
height = int(input("Qual a sua altura em centímetros?"))

if height >= 120 #maior ou igual a 120
    print("Você pode entrar na roda gigante!!") 
else:
    print("Você é pequeno!!!Cresça mais um pouco antes de entrar na roda gigante")


number = int(input())

if number%2 == 0: #o sinal % faz com que seja considerado apenas o resto a divisão
  print("This is an even number.")
else: 
  print("This is an odd number.")

###########################################################################################################
print("bem vindo a roda gigante")
height = int(input("Qual a sua altura em centímetros?"))

if height >= 120 #maior ou igual a 120
    print("Você pode entrar na roda gigante!!") 
    age = int(input("Quantos anos você tem?"))
    if age < 12:
       print("Por favor pague 5 reais")
    elif age > 18:
       print("Por favor pague 7 Reais.")
    else:
       print("Por favor pague 12 Reais.")
else:
    print("Você é pequeno!!!Cresça mais um pouco antes de entrar na roda gigante")

##################################################################################################################
print("bem vindo a roda gigante")
height = int(input("Qual a sua altura em centímetros?"))
conta= 0

if height >= 120 #maior ou igual a 120
    print("Você pode entrar na roda gigante!!") 
    age = int(input("Quantos anos você tem?"))
    if age < 12:
       conta = 5
       print("ingressos para crianças são 5 Reais.")
    elif age > 18:
       conta = 12
       print("ingressos para adultos são 12 Reais.")
    else:
       conta = 7
       print("ingressos para jovens são 7 Reais.")

    foto = input("você quer que tirem uma foto sua? Y or N.")
    if foto == "Y":
        conta += 3
    print(f"Você vai ter que pagar {conta} Reais.")
else:
    print("Você é pequeno!!!Cresça mais um pouco antes de entrar na roda gigante")