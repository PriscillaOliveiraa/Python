teste = list()
teste.append('Priscila')
teste.append(30)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 35
galera.append(teste[:])
print(galera)