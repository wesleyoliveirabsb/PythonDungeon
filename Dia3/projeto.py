print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro")
print("Sua missão é achar o tesouro.")

way = input("Qual direção você quer ir?(direita ou esquerda?\n")
way = way.lower()
if way == "esquerda":
    rio = input("A sua frente você vê um grande riacho com fortes correntes, o que você quer fazer? (esperar ou nadar?)\n")
    rio = rio.lower()
    if rio == "esperar": 
        porta = input("Depois de passar o rio você encontra um castelo com 3 portas distintas, qual a cor da porta que você quer entrar?(verde, azul ou vermelha?)\n")
        porta = porta.lower()
        if porta == "verde":
            print("parabéns!!! você achou o tesouro!!!")
        else:
            print("a porta tem uma armadilha de espinhos!!! x.x")
    else:
        print("a corrente te leva para sua morte!!! x.x")
else:
    print("você se perde na floresta!!! x.x")