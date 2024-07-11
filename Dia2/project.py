print ("Bem vindo a calculadora de gorjetas!!")


conta = input("Qual o valor da conta?")
gorjeta = input("Quanto de gorjeta você quer dar?? 10% , 12% ou 15%?")
pessoas = input("Quantas pessoas vão dividir a conta?")

gorjeta = int(gorjeta)/100 
gorjeta_total = float(conta) * float(gorjeta)

total = round((float(conta) + gorjeta_total)/ int(pessoas),2)

print(f"Cada pessoa deve pagar: R${total}")