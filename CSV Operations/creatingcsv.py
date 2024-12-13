import csv

def create(filename):
    with open(filename, 'w', newline='') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(('ID','Name','Percentage_Attendence'))
        while True:
            id = int(input("Enter student id : "))
            name = input("Enter student name : ")
            attendence = float(input("Enter '%' attendence : "))
            file_writer.writerow([id,name,attendence])
            choice = int(input("1 -> Add more\n 2 -> Exit\n Enter your choice : "))
            if choice == 2 :
                break
def reading(filename):
    with open(filename,'r') as file:
        file_reader = csv.reader(file)
        for i in file_reader:
            print(i)
def searching(filename):
    with open(filename, 'r') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        next(file_reader)
        for i in file_reader:
            if i[2] > '97':
                print(i[0])
searching('details.csv')