class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
def anilha():
    pilha = Stack()
    total = cont = 0
    while True:
        peso = int(input())
        if peso == 0:
            break
        else:
            pilha.push(peso)
    
    peso_desejado = int(input())

    while True:
        peso_retirado = pilha.pop()
        if peso_retirado != peso_desejado:
            print(f'Peso retirado: {peso_retirado}')
            total += peso_retirado
            cont += 1
        else:
            print(f'Peso retirado: {peso_retirado}')
            total += peso_retirado
            cont += 1
            break

    print(f'Anilhas retiradas: {cont}')
    print(f'Peso total movimentado: {total}') 
   
anilha()