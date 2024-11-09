import sys

def initial_phonebook():
    rows, cols = int(input("please enter an initial number of contacts:")), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter the contact%d details in the following order"%(i+1))
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*:")))
            if temp[j] == "":
                sys.exit(
                    "Name is mandatory"
                )
            if j == 1:
                temp.append(int(input("Enter number*:")))
            if j == 2:
                temp.append(str(input("Enter email*:")))
            if j == 3:
                temp.append(input(input("Enter birth dd/mm/yy*:")))
            if j == 4:
                temp.append(str(input("Enter category*:")))
        phone_book.append(temp)
    print(phone_book)
    return phone_book

def menu():

    print("\t\t\tSMARTPHONE DIRECTORY",flush=False)
    print("\tu can now use these operations:\n")
    print("1. add ")
    print("2. delete")
    print("3. display")
    print("4. exit")

    choice = int(input("please enter ur choice"))

    return choice

def add_contact():

    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("enter name:")))
        if i == 1:
            dip.append(int(input("enter no.:")))
        if i == 2:
            dip.append(str(input("enter email:")))
        if i == 3:
            dip.append(str(input("enter dob:")))
        if 1 == 4:
            dip.append(str(input("enter category:")))


def delete_all(pb):
    return pb.clear()


def display_all(pb):
    if not pb:
        print("list is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])
        
def thanks():
    sys.exit("goodbye pls visit again")

print("welcome")

ch = 1
pb = initial_phonebook()
while ch in (1,2,3):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb) 
    elif ch == 2:
        pb = delete_all(pb)
    elif ch == 3:
        display_all(pb)
    else:
        thanks()