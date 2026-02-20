#lanche = ('Hamburguer', 'suco', 'pudim', 'pizza')
lanche = ('0', '1', '2', '3', '4')

#Tuplas são imutavéis
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche)
print('=' * 30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('=' * 30)

for cont in range(0, len(lanche)):
    #print(lanche[cont]) ou
    print(f'Agora vou comer {lanche[cont]} na posição {cont}')

print('=' * 30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('=' * 30)

print(sorted(lanche))#para ordenar a lista
