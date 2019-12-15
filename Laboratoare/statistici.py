import pandas as pd
from pandas import read_csv

produse = pd.DataFrame(read_csv('produse.csv'))
produse['Pret_Nou'] = pd.to_numeric(produse['Pret_Nou'].str.replace(',', '.').astype(float), errors='ignore')
produse['Pret_vechi'] = pd.to_numeric(produse['Pret_vechi'].str.replace(',', '.').astype(float), errors='ignore')

#print(produse.dtypes)

#cea mai scumpa pereche de incaltaminte
pret_maxim=produse['Pret_Nou'].max()
print('\n***Produse cu pret maxim\n', produse.loc[(produse['Pret_Nou']==pret_maxim)])

#cea mai scumpa pereche de incaltaminte pe categoii (femei/barbati/copii)
preturi_maxime = produse.groupby(['Gen']).max()
print('\n***Produse cu pret maxim pe categorii\n',preturi_maxime['Pret_Nou'])

#pretul mediu al unei perechi de incaltaminte pe categorie
preturi_medii = produse.groupby(['Gen']).mean()
print('\n***Pretul mediu categorii\n', preturi_medii)

#pretul mediu al unei perechi de incataminte pe brand
preturi_medii= produse.groupby(['Brand']).mean()
print('\n***Pretul mediu brand\n',preturi_medii)

#bradul cu cele mai mari reduceri
produse['Reducere'] = produse['Pret_vechi'] - produse['Pret_Nou']
reducere_maxima = produse['Reducere'].max()
print('\n***Bradul cu cele mai mari reduceri\n', produse.loc[(produse['Reducere'] == reducere_maxima)])