import random

print("Bem vindo ao gerador de senhas!!")
letras = int(input("Quantas letras você quer na sua senha?\n"))
simbols = int(input("Quantos simbolos você quer na sua senha?\n"))
numeros = int(input("quantos numeros você quer na sua senha?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letra=['']*letras
for i in range(letras):
    letra[i] = random.choice(letters)

number=['']*numeros
for i in range(numeros):
    number[i] = random.choice(numbers)

simbolo=['']*simbols
for i in range(simbols):
    simbolo[i] = random.choice(symbols)

senha = letra + number + simbolo
megasenha = []
for i in range(len(senha)): 
    megasenha.append(random.choice(senha))

strSenha = ''.join(megasenha)

print(f'Aqui está sua nova senha: {strSenha}') 