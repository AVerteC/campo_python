#!usr/bin/env python3
# made by alan chen

def hashmatcher():
    namehash = {'Aaryan':['Divate','Singh'], 'Alan':['Chen','Do'],'Alexander':['Shtov','Sosnov','Xie'],'Brandon':['Darby','Tedja'],'Daniel':['Camarena','Nelson'],'Ian':['Darby','Mcmamara','Yao']}
    for k in namehash:
<<<<<<< HEAD
        print (k ,end = "")
        print (namehash.get(k))

=======
        if namehash.count(k) > 1:
            print("condition1complete")
>>>>>>> e1fd86a... continuing hash excercise


def htest():
    nhash = {'Jason': 'Sen','Jason': 'Do','Jason': 'Dan'}
    print(nhash)
    print(nhash.get('Jason'))
""""




Isaac        Chang
Isaac        Li

Jacob        Culaton
Jacob        Zhang

Jay        Nathan

Jay        Vishwarupe

Julia        Garrido
Julia        Kononova

Justin        Chow
Justin        Qiu

Kent        Williams
Kent        Wong

Kevin        Arackaparambil
Kevin        Wang
Kevin        Zhang

Peter        Le
Peter        Nguyen

Pranav        Damal
Pranav        Singh

Rohan        Taitriya
Rohan        Tibrewal

Samuel        Collet
Samuel        Vu

Sriram        Nagasuri
Sriram        Selvakumar

"""

#list of first names that should match

#Aaryan
#Alan
#Alexander
#Brandon
#Daniel






def main():
    # hashmatcher()
    htest()
main()