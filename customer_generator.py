import random
import pymysql
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def client_generator(x):
    prenom = random.choice(prenoms)
    nom = random.choice(noms)
    ville = random.choice(villes)
    email = prenom +'.'+nom + '@shop.com'
    return {'id':x, 'Prenom et nom': prenom +' '+nom,'email':email,'adresse':ville}

def store_client(client):
    cur.execute('insert into customers (customer_id, customer_name, email, address) values '
                '(%s,%s,%s,%s)',(client['id'],client['Prenom et nom'],client['email'],client['adresse']))
    cur.connection.commit()



html = urlopen('https://everybodywiki.com/Liste_des_pr%C3%A9noms_au_Qu%C3%A9bec')
bs = BeautifulSoup(html.read(),'html.parser')

table = bs.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

prenoms = []

for row in rows:
    try:
        prenoms.append(row.find_all(['td'])[0].get_text()[0:-1])
    except IndexError:
        pass
    #for cell in row.find_all(['td','th']):
     #   print(cell.get_text())
print(prenoms)

html = urlopen('https://fr.wikipedia.org/wiki/Liste_des_noms_de_famille_les_plus_courants_au_Qu%C3%A9bec')
bs = BeautifulSoup(html.read(),'html.parser')

table = bs.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

noms = []

try:
    for row in rows[1:]:
        noms.append(row.find(['span']).get_text())
except AttributeError:
    pass

print(noms)

html = urlopen('https://fr.wikipedia.org/wiki/Liste_des_villes_du_Qu%C3%A9bec')
bs = BeautifulSoup(html.read(),'html.parser')

table = bs.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

villes = []

for row in rows[1:]:
        villes.append(row.find(['b']).get_text())
print(villes)

conn = pymysql.connect(host='*****',user='root',passwd='******',db='mysql')

cur = conn.cursor()
cur.execute('use shop2')

for i in range(1,51):
    store_client(client_generator(i))
