with open('naselja2.txt') as f:
    lines = [line.rstrip() for line in f]
    postaja_id = 311
for x in lines:
    postaja_id = postaja_id + 1
    sql = 'INSERT INTO postaja (postaja_id, naselje) VALUES ({},{});'.format(postaja_id,x)
    print(sql)
    
    