import random

popust_id = ["'student'", "'ucenik'", "'djeca'", "'umirovljenik'", "'invalid'", "'mladi'", "'nema'"]
ime = ["'Luka'", "'David'", "'Jakov'", "'Ivan'", "'Petar'", "'Matej'", "'Karlo'", "'Mateo'", "'Roko'", "'Noel'", "'Ramon'", "'Kirill'", "'Noemi'", "'Lara'", "'Tena'", "'Petra'", "'Sofia'", "'Natasja'", "'Alina'", "'Daria'"]
prezime = ["'Horvat'", "'Kovačević'", "'Babić'", "'Marić'", "'Jurić'", "'Novak'", "'Kovačić'", "'Vuković'", "'Knežević'", "'Marković'", "'Petrović'", "'Matić'", "'Tomić'", "'Kovač'", "'Pavlović'", "'Božić'", "'Blažević'", "'Grgić'", "'Pavić'", "'Radić'"]
adresa = ["'Park Ivana Pavla II. 22'", "'Šetalište Vatroslava Jagića 19'", "'Ulica Alojzija Stepinca 53'", "'Ulica Ivana Gundulića 73'", "'Ulica Ljudevita Gaja 38'", "'Podravska ulica 126'", "'Ulica Tita Brezovačkog 89'", "'Zagrebačka ulica 6'", "'Splitska ulica 83'", "'Vinkovačka ulica 11'", "'Ulica Marije Jurić-Zagorke 53'", "'Zadarska ulica 64'", "'Hercegovačka ulica 55'", "'Ulica Eugena Kvaternika 124'", "'Zavojna ulica 21'", "'Ulica Ruđera Boškovića 68'", "'Ulica kneza Trpimira 83'", "'Vukovarska ulica 12'", "'Ulica braće Radić 3'", "'Ulica Ljudevita Gaja 5'"]
tel = ["'0992783282'", "'0995821743'", "'0995481275'", "'0979482194'", "'0958232932'", "'0994214219'", "'0957312371'", "'0974721471'", "'0952832194'", "'0973921484'", "'0953838172'", "'0976632808'", "'0972837192'", "'0997384727'", "'0950932855'", "'0978882727'", "'0995834989'", "'0979520005'", "'0951128582'", "'0954247829'"]
god = [
"'26/10/1978'"
,"'24/01/1980'"
,"'21/10/1982'"
,"'07/06/1983'"
,"'16/03/1984'"
,"'16/10/1985'"
,"'18/03/1986'"
,"'05/06/1986'"
,"'30/10/1987'"
,"'04/04/1990'"
,"'17/09/1990'"
,"'14/10/1991'"
,"'25/06/1992'"
,"'28/12/1992'"
,"'03/02/1993'"
,"'17/08/1993'"
,"'21/12/1993'"
,"'04/04/1994'"
,"'14/06/1994'"
,"'07/12/1994'"]
y=1
for x in range(20):
    ran = random.randint(0,6);
    sql = 'INSERT INTO kupac (kupac_id, ime, prezime, adresa, tel, datum, popust_id) VALUES ({},{},{},{},{},{},{});'.format(y, ime[x], prezime[x], adresa[x], tel[x], god[x], popust_id[ran])
    print(sql)
    y = y+1

