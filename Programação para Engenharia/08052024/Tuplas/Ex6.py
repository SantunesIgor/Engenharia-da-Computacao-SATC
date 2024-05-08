# Crie uma tupla com os nomes dos super-heróis que devem participar do Filme Vingadores seguindo a ordem:
#  • Homem de Ferro • Capitão América • Thor • Hulk • Viúva Negra • Gavião Arqueiro

# Agora, inclua o Homem-Aranha no final da lista e mostre em qual posição está o Thor. 

# Infelizmente a Viúva Negra e o Homem de Ferro não fazem mais parte do filme Vingadores, então retire-os 
# da lista.
herois = ('Homem de Ferro', 'Capitão América', 'Thor', 'Hulk', 'Viúva Negra', 'Gavião Arqueiro')
print(herois)
herois = herois + ('Homem-Aranha',)
print(herois, herois.index('Thor'))
herois = tuple(set(herois) - set(('Viúva Negra', 'Capitão América')))
print(herois)
