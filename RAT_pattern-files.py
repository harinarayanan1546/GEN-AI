#RAT_NUMBER_ROWS
#--------------#

def rat_num_row():
    f=open('patterns.txt','w+')
    f.write("=======RAT NUM ROW=======\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()

    
#RAT_NUMBER_coloumn
#--------------#

def rat_num_coloumn():
    f=open('patterns.txt','a+')
    f.write("=======RAT NUM COLOUMN=======\n")
    for i in range(1,6):
        for j in range(1,i):
            f.write(str(j))
        f.write('\n')
    f.close()


#RAT_upper_row
#--------------#

def rat_upper_row():
    f=open('patterns.txt','a+')
    f.write("=======RAT UPPER ROW=======\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()

#RAT_upper_coloumn
#--------------#

def rat_upper_coloumn():
    f=open('patterns.txt','a+')
    f.write("=======RAT UPPER COLOUMN=======\n")
    for i in range(1,6):
        for j in range(1,i):
            f.write(chr(j+64))
        f.write('\n')
    f.close()


#RAT_lower_row
#--------------#

def rat_lower_row():
    f=open('patterns.txt','a+')
    f.write("=======RAT LOWER ROW=======\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(i+64+32))
        f.write('\n')
    f.close()

#RAT_lower_coloumn
#--------------#

def rat_lower_coloumn():
    f=open('patterns.txt','a+')
    f.write("=======RAT LOWER ROW=======\n")
    for i in range(1,6):
        for j in range(1,i):
            f.write(chr(j+64+32))
        f.write('\n')
    f.close()

#RAT_STAR
#--------------#

def rat_star():
    f=open('patterns.txt','a+')
    f.write("=======RAT STAR=======\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write('*')
        f.write('\n')
    f.close()

rat_num_row()
rat_num_coloumn()
rat_upper_row()
rat_upper_coloumn()
rat_lower_row()
rat_lower_coloumn()
rat_star()












            
