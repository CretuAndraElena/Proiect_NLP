# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_pages = ['https://www.sportvision.ro/pantofi-sport/273039-nike-pantofi-sport-air-max-vision-prm',
                'https://www.sportvision.ro/pantofi-sport/273024-nike-pantofi-sport-air-max-vision-se', 
                'https://www.sportvision.ro/pantofi-sport/164923-nike-pantofi-sport-air-relentless-5']
produse = []

for page in quote_pages:

    page = urllib2.urlopen(page)
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    brand = soup.find('div' , attrs={'class': 'brand'})
    brand = brand.text.strip()

    nume = soup.find_all('div', attrs={'class':'title'})
    nume = nume[6].text.strip()

    print(nume)
    pret_nou = soup.find('span', attrs={'class': 'product-price-value value'})
    pret_nou = pret_nou.text

    pret_vechi = soup.find('span', attrs={'class': 'product-price-without-discount-value value'})
    pret_vechi = pret_vechi.text

    marime = soup.find('span', attrs={'class': 'original-size'})
    marime = marime.text.strip()

    produse.append((brand, nume, pret_nou, pret_vechi, marime))

#adaugare informatii in fisier
with open('produse.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)

    for brand, name, pret_nou, pret_vechi, marime in produse:
        writer.writerow([brand, name, pret_nou, pret_vechi, marime , datetime.now()])
