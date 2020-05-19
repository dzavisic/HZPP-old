popust_id = ['student', 'ucenik', 'djeca', 'umirovljenik', 'invalid', 'mladi']
postotak = ['50', '30', '50', '50', '75', '30']
index = 0
for x in popust_id:
    sql = 'INSERT INTO popust (popust_id, postotak) VALUES ({},{});'.format(x,postotak[index])
    print(sql)
    index = index + 1