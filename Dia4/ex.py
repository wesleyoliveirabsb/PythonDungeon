import random
import modulo

random_integer = random.randint(1,10)

print(modulo.pi)

#criar um floating point random

random_float = random.random() #um numero float entre 0 e 1 mas não inclui 1
random_float = random.random()*5 #um numero entre 0 e 5 mas não inclui 5

print(random_float) 

trueLove = random.randint(1,100)
print(f"Sua compatibilidade com seu companheiro recebeu {trueLove} pontos.")