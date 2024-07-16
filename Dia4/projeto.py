import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

armas = [pedra, papel , tesoura]
escolha = int(input("pedra(0) papel(1) ou tesoura?(2)\n"))
escolhaPc = random.randint(0,1)

print(armas[escolha])

print("O Computar escolhe...")
print(armas[escolhaPc])

if (escolha == 0 and escolhaPc == 2) or (escolha == 2 and escolhaPc == 1) or (escolha == 1 and escolhaPc == 0):
    print("Você venceu!!!")
if (escolhaPc == 0 and escolha == 2) or (escolhaPc == 2 and escolha == 1) or (escolhaPc == 1 and escolhaPc == 0):
    print("O computador venceu!!!")
elif escolha == escolhaPc:
    print("vocês empataram!!!")