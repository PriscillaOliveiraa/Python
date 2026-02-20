lanche = ['Hamburguer', 'Cocacola', 'Batata Frita']
print(lanche)
lanche[1] = 'suco' #Tuplas são imutaveis
print(lanche)
num = [2,5,9,1]
print(num)
num[2] = 3 #substituir valores
num.append(7) #para inserir valores
num.insert(2,0)
num.pop() #não houver parametro então é igual a 1
num.pop(2) #vai remover o zero
num.remove(2) #elimina a primeira ocorrencia do valor escolhido. Se o valor não estiver na lista da erro.
print(num)
print(f'Essa lista tem {len(num)} elementos')