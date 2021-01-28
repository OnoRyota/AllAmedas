import pandas
import requests
from bs4 import BeautifulSoup

#国見
url_kunimi = 'http://www.jma.go.jp/jp/amedas_h/today-83021.html'
kunimi = pandas.io.html.read_html(url_kunimi)
kunimi[4].to_json('KunimiNoAme.json',force_ascii=False)

html_kunimi = requests.get(url_kunimi).content
soup = BeautifulSoup(html_kunimi,'html.parser')
date_kunimi = soup.find(class_ = "td_title height2").get_text()
date_kunimi = date_kunimi + "の気象情報"

file = open('date_kunimi.txt','w')
file.write(date_kunimi)
file.close()

##############################################################################

#中津
url_nakatu = 'http://www.jma.go.jp/jp/amedas_h/today-83051.html'
nakatu = pandas.io.html.read_html(url_nakatu)
nakatu[4].to_json('NakatuNoAme.json',force_ascii=False)

html_nakatu = requests.get(url_nakatu).content
soup = BeautifulSoup(html_nakatu,'html.parser')
date_nakatu = soup.find(class_ = "td_title height2").get_text()
date_nakatu = date_nakatu + "の気象情報"

file = open('date_nakatu.txt','w')
file.write(date_nakatu)
file.close()

##############################################################################

#豊後高田
url_bungotakada = 'http://www.jma.go.jp/jp/amedas_h/today-83061.html'
bungotakada = pandas.io.html.read_html(url_nakatu)
nakatu[4].to_json('BungotakadaNoAme.json',force_ascii=False)

html_bungotakada = requests.get(url_bungotakada).content
soup = BeautifulSoup(html_bungotakada,'html.parser')
date_bungotakada = soup.find(class_ = "td_title height2").get_text()
date_bungotakada = date_bungotakada + "の気象情報"

file = open('date_bungotakada.txt','w')
file.write(date_bungotakada)
file.close()

##############################################################################

#杵築
url_kituki = 'http://www.jma.go.jp/jp/amedas_h/today-83121.html'
kituki = pandas.io.html.read_html(url_kituki)
kituki[4].to_json('KitukiNoAme.json',force_ascii=False)

html_kituki = requests.get(url_kituki).content
soup = BeautifulSoup(html_kituki,'html.parser')
date_kituki = soup.find(class_ = "td_title height2").get_text()
date_kituki = date_kituki + "の気象情報"

file = open('date_kituki.txt','w')
file.write(date_kituki)
file.close()

##############################################################################

#院内
url_innai = 'http://www.jma.go.jp/jp/amedas_h/today-83106.html'
innai = pandas.io.html.read_html(url_innai)
innai[4].to_json('InnaiNoAme.json',force_ascii=False)

html_innai = requests.get(url_innai).content
soup = BeautifulSoup(html_innai,'html.parser')
date_innai = soup.find(class_ = "td_title height2").get_text()
date_innai = date_innai + "の気象情報"

file = open('date_innai.txt','w')
file.write(date_innai)
file.close()

##############################################################################

#玖珠
url_kusu = 'http://www.jma.go.jp/jp/amedas_h/today-83191.html'
kusu = pandas.io.html.read_html(url_kusu)
kusu[4].to_json('KusuNoAme.json',force_ascii=False)

html_kusu = requests.get(url_kusu).content
soup = BeautifulSoup(html_kusu,'html.parser')
date_kusu = soup.find(class_ = "td_title height2").get_text()
date_kusu = date_kusu + "の気象情報"

file = open('date_kusu.txt','w')
file.write(date_kusu)
file.close()

##############################################################################

#湯布院
url_yuhuin = 'http://www.jma.go.jp/jp/amedas_h/today-83201.html'
yuhuin = pandas.io.html.read_html(url_yuhuin)
yuhuin[4].to_json('YuhuinNoAme.json',force_ascii=False)

html_yuhuin = requests.get(url_yuhuin).content
soup = BeautifulSoup(html_yuhuin,'html.parser')
date_yuhuin = soup.find(class_ = "td_title height2").get_text()
date_yuhuin = date_yuhuin + "の気象情報"

file = open('date_yuhuin.txt','w')
file.write(date_yuhuin)
file.close()

##############################################################################

#竹田
url_taketa = 'https://www.jma.go.jp/jp/amedas_h/today-83371.html?areaCode=000&groupCode=59'
taketa = pandas.io.html.read_html(url_taketa)
taketa[4].to_json('TaketaNoAme.json',force_ascii=False)

html_taketa = requests.get(url_taketa).content
soup = BeautifulSoup(html_taketa,'html.parser')
date_taketa = soup.find(class_ = "td_title height2").get_text()
date_taketa = date_taketa + "の気象情報"

file = open('date_taketa.txt','w')
file.write(date_taketa)
file.close()

##############################################################################

#犬飼
url_inukai = 'http://www.jma.go.jp/jp/amedas_h/today-83341.html'
inukai = pandas.io.html.read_html(url_inukai)
inukai[4].to_json('InukaiNoAme.json',force_ascii=False)

html_inukai = requests.get(url_inukai).content
soup = BeautifulSoup(html_inukai,'html.parser')
date_inukai = soup.find(class_ = "td_title height2").get_text()
date_inukai = date_inukai + "の気象情報"

file = open('date_inukai.txt','w')
file.write(date_inukai)
file.close()

##############################################################################

#宇目
url_ume = 'http://www.jma.go.jp/jp/amedas_h/today-83431.html'
ume = pandas.io.html.read_html(url_ume)
ume[4].to_json('UmeNoAme.json',force_ascii=False)

html_ume = requests.get(url_ume).content
soup = BeautifulSoup(html_ume,'html.parser')
date_ume = soup.find(class_ = "td_title height2").get_text()
date_ume = date_ume + "の気象情報"

file = open('date_ume.txt','w')
file.write(date_ume)
file.close()

##############################################################################

#佐伯
url_saiki = 'http://www.jma.go.jp/jp/amedas_h/today-83401.html'
saiki = pandas.io.html.read_html(url_saiki)
saiki[4].to_json('SaikiNoAme.json',force_ascii=False)

html_saiki = requests.get(url_saiki).content
soup = BeautifulSoup(html_saiki,'html.parser')
date_saiki = soup.find(class_ = "td_title height2").get_text()
date_saiki = date_saiki + "の気象情報"

file = open('date_saiki.txt','w')
file.write(date_saiki)
file.close()

##############################################################################

#蒲江
url_kamae = 'http://www.jma.go.jp/jp/amedas_h/today-83476.html'
kamae = pandas.io.html.read_html(url_kamae)
kamae[4].to_json('KamaeNoAme.json',force_ascii=False)

html_kamae = requests.get(url_kamae).content
soup = BeautifulSoup(html_kamae,'html.parser')
date_kamae = soup.find(class_ = "td_title height2").get_text()
date_kamae = date_kamae + "の気象情報"

file = open('date_kamae.txt','w')
file.write(date_kamae)
file.close()
