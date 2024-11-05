import sys

def initial_phonebook():
    row, cols = int(input("please enter an initial number of contacts:")), 5
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




