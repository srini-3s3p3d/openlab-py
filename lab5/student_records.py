import csv


def insert_rec(data):
    with open('records.csv', 'a') as csvfile:
        fw = csv.writer(csvfile)
        fw.writerow(data)
    print('Record inserted')


def display_rec():
    try:
        with open('records.csv', 'r') as csvfile:
            fr = csv.reader(csvfile)
            for row in fr:
                print(row)
    except IOError:
        print('File not found:')


def update_rec(rollno):
    try:
        data = []
        total = []
        with open('records.csv', 'r') as csvfile:
            fr = csv.reader(csvfile)
            total = list(fr)
            for row in total:
                if (row[1] == rollno):
                    name = input('Name')
                    branch = input('Branch')
                    year = input('Year')
                    cgpa = input('CGPA')
                    data.append(name)
                    data.append(rollno)
                    data.append(branch)
                    data.append(year)
                    data.append(cgpa)

        with open('records.csv', 'a+') as csvfile:
            fw = csv.writer(csvfile)
            fw.writerows(total)

    except IOError:
        print('File not found:')


while (1):
    char = input('Enter i to insert record, d to display records and u to update record(enter q to quit)')
    if (char == 'q'):
        break
    if (char == 'i'):
        print('Enter following details : ')
        name = input('Name')
        roll_no = input('Roll no')
        branch = input('Branch')
        year = input('Year')
        cgpa = input('CGPA')
        data = []
        data.append(name)
        data.append(roll_no)
        data.append(branch)
        data.append(year)
        data.append(cgpa)
        insert_rec(data)
    if (char == 'd'):
        display_rec()
    if (char == 'u'):
        rollno = input('Enter roll number of student:  ')
        update_rec(rollno)
        display_rec()
