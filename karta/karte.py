import random
karta_id = 0
kupac_id = 0
datum = [
"'7/16/2020'"
,"'7/28/2020'"
,"'8/5/2020'"
,"'8/10/2020'"
,"'8/28/2020'"
,"'11/2/2020'"
,"'11/6/2020'"
,"'1/1/2021'"
,"'1/5/2021'"
,"'1/14/2021'"
,"'1/26/2021'"
,"'2/10/2021'"
,"'4/5/2021'"
,"'4/13/2021'"
,"'4/21/2021'"
,"'6/23/2021'"
,"'7/13/2021'"
,"'8/3/2021'"
,"'8/9/2021'"
,"'9/28/2021'" 
]
for x in range(20):
    trajanje = random.randint(1,23)
    if trajanje<10:
        trajanje = '0' + str(trajanje)
    trajanje2 = random.randint(1,59)
    karta_id = karta_id + 1
    info_id = random.randint(1,400)
    kupac_id = kupac_id+1
    sql = 'INSERT INTO karta (karta_id, info_id, datum, kupac_id, vrijeme_polaska) VALUES ({},{},{},{},{});'.format(karta_id, info_id, datum[x], kupac_id, "'" + str(trajanje) + ":" + str(trajanje2) + ":00'")
    print(sql)