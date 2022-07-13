import requests
import pprint
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

questionlist = []

def getQuestions(page):
    url = f'https://sbmh.com.br/medicos/page/{page}/'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class': 'item-medico col-lg-12 col-md-12 col-sm-12 col-xs-12'})
    for item in questions:
         linha = item.find('a',{'class': 'link-medico'})['title']+","+item.find('a', {'class': 'link-medico'})['href']+","+item.find('div', {'class': 'det-medico col-lg-9 col-md-9 col-sm-12 col-xs-12'}).text.replace('\n', ',')
         questionlist.append(linha)
    return

pprint.pprint(questionlist)
print(len(questionlist))

for x in range(1,19):
  getQuestions(x)

df = pd.DataFrame(questionlist)
df.to_csv('MEDICOS.csv', index=False)
print('Finalizado com sucesso!')
