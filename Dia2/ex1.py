#String
print("Hello" [0])
print("123" +"456")

#Integer
print(123456)
123456  
123_456

#float
3.4564

#boolean
True
False


num_char = len(input("Qual o seu nome?"))

int_num_char = str(num_char)
#float(element)
#str(element)
print("Seu nome contém " + int_num_char + " Letras")


3+5
7-3
3*5
4/6 #divisions are floats
** #isso é o simbolo do expoente ou elevação
2**2 #lê-se 2 elevado a 2

PEMDASLefttoRight
()
**
* /
+ -

#será priorizado o calculo mais pra esquerda

print(3*3 + 3 / 3 - 3)


#arrredondando numeros

print(round(8/3))
print(round(8/3,2)) #assim vai arredondar com duas casas decimais
print(round (2.66666666,2))
print(8//3) #isso vai cortar todos os numeros depois da casa decimal, o numero vai ser um integer

#f-string
#permite parar de converter tudo
score=0

f"sua pontuação é {score},"