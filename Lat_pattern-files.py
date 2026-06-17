def latrow():
    f=open('patterns.txt','w+')
    f.write('LAT NUM ROW\n-------------\n')
    for i in range (1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
latrow()

def latcoloumn():
    f=open('patterns.txt','a+')
    f.write('LAT NUM COLOUMN\n-------------\n')
    for i in range (1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(str(k))
        f.write('\n')
    f.close()
latcoloumn()

def latupperrow():
    f=open('patterns.txt','a+')
    f.write('LAT UPPER ROW\n-------------\n')
    for i in range (1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()
latupperrow()

def latuppercoloumn():
    f=open('patterns.txt','a+')
    f.write('LAT UPPER COLOUMN\n-------------\n')
    for i in range (1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+64))
        f.write('\n')
    f.close()
latuppercoloumn()

def latlowerrow():
    f=open('patterns.txt','a+')
    f.write('LAT LOWER ROW\n-------------\n')
    for i in range (1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64+32))
        f.write('\n')
    f.close()
latlowerrow()

def latlowercoloumn():
    f=open('patterns.txt','a+')
    f.write('LAT LOWER COLOUMN\n-------------\n')
    for i in range (1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(1,i):
            f.write(chr(k+64+32))
        f.write('\n')
    f.close()
latlowercoloumn()

def latstar():
    f=open('patterns.txt','a+')
    f.write('LAT STAR\n-------------\n')
    for i in range (1,7):
        for j in range(7,i,-1):
            f.write(' ')
        for k in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()
latstar()





