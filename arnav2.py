

stack1=[]
stack2=[]
stack3=[]


def add():
    print()
    print()
    global x,y,z
    n=int(input("ENTER NUMBER OF ENTERIES TO BE ENTERED : "))
    i=0
    while i<n:
        print()
        print()
        x=int(input("Enter HOSTEL NUMBER : "))
        stack1.append(x)
        y=int(input("Enter NUMBER OF ROOMS : "))
        stack2.append(y)
        z=int(input("Enter NUMBER OF STUDENTS :"))
        stack3.append(z)
        i=i+1


def show():
    global x,y,z
    print()
    print()
    if stack1==[]:
        print("NO RECORDS FOUND")
    else :
        print()
        print()
        print("TOTAL HOSTELS : ",stack1)
        print("TOTAL ROOMS : ",stack2)
        print("TOTAL STUDENTS : ",stack3)


def delete():
    print()
    print()
    if stack1==[]:
        print("NO RECORD FOUND")
    else :
        stack1.pop()
        stack2.pop()
        stack3.pop()
        print("LAST RECORD DELETED")



        
while True:
    print()
    print()
    print("ENTER 1 TO ADD RECORDS")
    print("ENTER 2 TO SHOW RECORDS")
    print("ENTER 3 TO DELETE RECORDS")
    comm=int(input("ENTER YOUR CHOICE : "))
    if comm==1:
        add()
    elif comm==2:
        show()
    elif comm==3:
        delete()
    else :
        exit()











        
