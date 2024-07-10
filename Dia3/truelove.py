print("The Love Calculator is calculating your score...")
name1 = input() # seu nome
name2 = input() # nome dele(a)
#juntando os nomes e convertendo em minuscula 
text = name1+name2
lowerT = text.lower()

#contando as letras de true
true = lowerT.count("t")
true += lowerT.count("r")
true += lowerT.count("u")
true += lowerT.count("e")

#contando as letras de love
love = lowerT.count("l")
love += lowerT.count("o")
love += lowerT.count("v")
love += lowerT.count("e")
#transformando true e love em string ,concatenando elas e transformando em int
trueLove = int(str(true) + str(love))

if trueLove < 10 or trueLove > 90:
  print(f"Your score is {trueLove}, you go together like coke and mentos.")
elif trueLove > 40 and trueLove <50:
  print(f"Your score is {trueLove}, you are alright together.")
else:
  print(f"Your score is {trueLove}.")
