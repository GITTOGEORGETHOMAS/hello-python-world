def average(num1,num2):
    print("Required Arguments  Average is :", (num1+num2)/2)

average(10,20)


def average1(num1 = 5, num2 = 10):
    print("Default Arguments Average is :", (num1+num2)/2)

average1()

average1(6,14)
average1(6)
average1(num2 = 20)
average1(num2 = 50, num1 = 60)
average1(num2 = 50, num1 = 100)

def name(mname='George',fname="Gitto", lname = "Thomas"):
    print("Full Name is :", fname,mname,lname)

name("Varghese","Jikku","Thomas")



def name1(fname,mname,lname):
    print("Hello", fname,mname,lname)

name1(mname = "Mathew", lname="Thomas", fname="Ajish")


def name2(fname,mname,lname):
    print("Hello", fname,mname,lname)

name2("Betty","George","Thomas")

def averageNumbers(*numbers):
    sum =0
    for num in numbers:
        sum += num
    print("Average is :", sum/len(numbers))

averageNumbers(5,6,4)    



def namesofstudents(*names):
     print(type(names))
     print("Hello", names[0], names[1])

namesofstudents("Ajish","Betty","George","Thomas")


def namesidicti(**names):
    print("Hello",names['fname'],names['lname'] )

namesidicti(fname ="Ajish", lname ="Mathew")