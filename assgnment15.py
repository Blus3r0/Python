import sqlite3
#Este programa analiza el archivo mbox.txt en busca de direcciones de correos electrónico
#Divide dichas direcciones y nos separa el dominio, lo cual luego almacena en una pequeña BD 
#con el mismo nombre de este programa
#Hecho por Carlos Correa para el curso de Python de la plataforma Coursera

con = sqlite3.connect('assignment_15.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts ( org TEXT, count INTEGER)')

fname = input("Enter file: ")
if len(fname) < 1: fname = 'mbox.txt'
fh = open(fname)

for l in fh:
    if not l.startswith('From: '): continue
    pcs = l.split()
    #print(pcs)
    org = pcs[1]
    at = org.split('@')
    org = at[1]

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    con.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr): 
    print(str(row[0]), row[1] )

cur.close()