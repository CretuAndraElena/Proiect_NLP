# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#functie pentru extragerea link-uri pentru toate produsele din categoria barbati
def extragere_linkuri_produse(pagina_principala):
    page = urllib2.urlopen(pagina_principala)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    links = soup.select("div.text-wrapper > div.title > a")

    pages = []
    for link in links:
        url = link.get('href')
        pages.append(url)

    return pages

#functie de parsare html si extragere clase
def parse_html(link):

    page = urllib2.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    brand = soup.find('div' , attrs={'class': 'brand'})
    brand = brand.text.strip()

    nume = soup.find_all('div', attrs={'class':'title'})
    nume = nume[3].text.strip()

    print(nume)
    pret_nou = soup.find('span', attrs={'class': 'product-price-value value'})
    pret_nou = pret_nou.text

    pret_vechi = soup.find('span', attrs={'class': 'product-price-without-discount-value value'})
    pret_vechi = pret_vechi.text

    marime = soup.find('span', attrs={'class': 'original-size'})
    marime = marime.text.strip()

    categorie = 'barbati'

    return (brand, nume, pret_nou, pret_vechi, marime, categorie)

#adaugare informatii in fisier
def scriere_in_fisier(produs):
    with open('produse.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([produs[0],produs[1],produs[2],produs[3],produs[4], produs[5], datetime.now()])

#Laboratorul 3
for i in range(1,11):
    link = 'https://www.sportvision.ro/incaltaminte/barbati/page-'+ str(i)
    quote_pages = extragere_linkuri_produse(link)

    #extragere informatii din  link-uri
    for quote_page in quote_pages:
        try:
            produs = parse_html(quote_page)
            #adaugare produs
            scriere_in_fisier(produs)
        except AttributeError:
            print("Invalid Url: ", quote_page)

