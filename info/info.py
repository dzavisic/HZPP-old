import random
polazište = []
for x in range(556):
    polazište.append(x)
odredište = []
for x in range(556):
    odredište.append(x)

nova = []
info_id=0
for i in range(400):
    info_id = info_id + 1;  
    pola = random.randint(1,556)
    odr = random.randint(1,556)
    if pola in nova:
        pola = random.randint(1,556)
    if odr in nova:
        odr = random.randint(1,556)
    while pola == odr:
        odr = random.randint(1,556);
    nova.append(pola)
    nova.append(odr)
    
        
    cijena = round(abs(odr-pola) * random.uniform(20,60),2)
    
    trajanje = random.randint(1,23)
    if trajanje<10:
        trajanje = '0' + str(trajanje)
    trajanje2 = random.randint(1,59)
    vlak = random.randint(1,6)
    sql = 'INSERT INTO info (info_id, polaziste, odrediste, cijena, trajanje, vlak_id) VALUES ({},{},{},{},{},{});'.format(info_id,pola,odr,cijena,"'" + str(trajanje) + ":" + str(trajanje2) + ":00'",vlak)
    print(sql)


