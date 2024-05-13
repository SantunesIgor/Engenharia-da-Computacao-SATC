# 1) Crie um Dicionário com os nomes de séries de TV seguindo o exemplo:

# series = ("Black Mirror", "Breaking Bad", "Friends", "Game of Thrones", 
#                 "The Big Bang Theory”, “House”,  “The Last of Us”, “One Piece”,
#                 “Grey's Anatomy”, “Stranger Things” )

# Agora, inclua uma nova série no final da lista 
# Mostre em qual posição está a série  “One Piece”. 
# Infelizmente a série “House” não fazem mais parte da lista e deve ser removida.
# Ao final, mostre a lista completa de séries.

series = ("Black Mirror", "Breaking Bad", "Friends", "Game of Thrones", 'The Big Bang Theory', 'House',  'The Last of Us', 'One Piece',"Grey's Anatomy", "Stranger Things")
print(f"Tupla 'series' inicial: \n{series}")
series = series + (input('Digite uma série para ser adicionada: '),)
print(f"Tupla com a série 'The Office' adicionada: \n{series}")
print(f"A posição da série 'One Piece' é: \n{series.index('One Piece')}")
series = tuple(i for i in series if i != 'House')
print(f"A série 'House' foi retirada: \n{series}")
print(f"Tupla final:\n{series}")
