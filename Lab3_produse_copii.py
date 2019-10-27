# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_pages = ['https://www.sportvision.ro/pantofi-sport/311366-adidas-pantofi-sport-advantage-i',
                'https://www.sportvision.ro/pantofi-sport/317082-nike-pantofi-sport-air-max-90-ultra-2-0-br-gs', 
                'https://www.sportvision.ro/pantofi-sport/309579-adidas-pantofi-sport-altarun-cf-i']
produse = []

for page in quote_pages:

    page = urllib2.urlopen(page)
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    brand = soup.find('div' , attrs={'class': 'brand'})
    brand = brand.text.strip()
    print (brand)
    
    nume = soup.find_all('div', attrs={'class':'title'})
    nume = nume[3].text.strip()                           
    print(nume)
    
    pret_nou = soup.find('span', attrs={'class': 'product-price-value value'})
    pret_nou = pret_nou.text
    print (pret_nou)

    pret_vechi = soup.find('span', attrs={'class': 'product-oldprice-value value'})
    pret_vechi = pret_vechi.text
    print (pret_vechi)
    
    marime = soup.find('span', attrs={'class': 'original-size'})
    marime = marime.text.strip()
    print (marime)

    produse.append((brand, nume, pret_nou, pret_vechi, marime))

#adaugare informatii in fisier
with open('produse_copii.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)

    for brand, name, pret_nou, pret_vechi, marime in produse:
        writer.writerow([brand, name, pret_nou, pret_vechi, marime , datetime.now()])
