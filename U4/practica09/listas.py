listaJuegos = ['Kingdom Hearts II', 'The Legend of Zelda: Breath of the Wild', 'Red Dead Redemption 2', 'The Last of Us', 'God of War']

listaJuegos.append('Mario Odyssey')
listaJuegos.append('Final Fantasy VII Rebirth')

listaJuegos.insert(2, 'The Legend of Zelda: Tears of the Kingdom')

listaJuegos.remove('God of War')

for e in listaJuegos:
    print(e)

listaJuegos_ordenada = sorted(listaJuegos)
print(listaJuegos_ordenada)