import random
ran = random.randint(0,6);
ime = ["'Marko'", "'Toni'", "'Luka'", "'Stjepan'", "'Borna'", "'Mislav'", "'Tomislav'", "'Karlo'", "'Antonio'", "'Bernard'", "'Mario'", "'Slavko'", "'Marija'", "'Barbara'", "'Luna'","'Magdalena'", "'Ferida'", "'Naomi'", "'Danka'", "'Irina'"]
prezime = ["'Bajić'", "'Ištvanović'", "'Karlić'", "'Bosančić'","'Ivanišević'", "'Bekavac'", "'Marijanović'", "'Cvitković'", "'Miklošević'", "'Galista'", "'Dajak'", "'Grizelj'", "'Lukić'", "'Brajković'", "'Luburić'", "'Filipović'","'Čančarević'", "'Žurić'", "'Kardum'", "'Radišić'"]
adresa = ["'Marusinac 2'","'Matoševa 6'","'Meštrovići 64'","'Mezanovci 152'","'Ulica sv. Anastazija 53'","'Ulica mladih 252'","'Ulica ZNG 25'","'Kapljuč 11'","'Kaštelanska 25'","'Kliški put 86'","'Kliških uskoka 65'","'Kneza Domagoja 628'","'Kneza Mislava 142'","'Kneza Trpimira 235'","'Kolići 53'","'Kozjačka 75'","'Kraljice Jelene 124'","'Krešimirova 421'","'Kroz Smiljanovac 35'","'Kunčeva greda 53'"]
tel = ["'0958231082'","'0953020508'","'0959312776'","'0953761771'","'0953173030'","'0938031169'","'0998550589'","'0996493843'","'0978231082'","'0973020508'","'0979312776'","'0973761771'","'0993173030'","'4888031169'","'0998550589'","'0996493843'","'0993173030'","'095031169'","'0958550589'","'0956493843'"]
god = [
"'19/03/1981'"
,"'16/03/1982'"
,"'22/09/1982'"
,"'18/11/1982'"
,"'03/12/1984'"
,"'17/02/1987'"
,"'08/05/1987'"
,"'19/08/1987'"
,"'01/06/1989'"
,"'31/08/1989'"
,"'13/11/1989'"
,"'20/06/1990'"
,"'18/02/1991'"
,"'16/08/1991'"
,"'21/10/1991'"
,"'20/12/1991'"
,"'01/01/1992'"
,"'18/03/1992'"
,"'31/05/1994'"
,"'09/12/1994'"
]
placa = []

for y in range(20):
    placa.append(random.randint(5000, 12000))
y=1
for x in range(20):
    uloga = random.randint(1,3)
    sql = 'INSERT INTO zaposlenik (zap_id, ime, prezime, adresa, tel, datum, placa, uloga) VALUES ({},{},{},{},{},{},{},{});'.format(y, ime[x], prezime[x], adresa[x], tel[x], god[x], placa[x], uloga)
    print(sql)
    y = y+1

