def insert_rec(data):
    print('Record inserted')

def display_rec():
    print('Displaying records:')

def update_rec():
    print('REcord updated')

while(1):
    char=input('Enter i to insert record, d to display records and u to update record(enter q to quit)')
    if(char=='q'):
        break
    if(char=='i'):
        print('Enter following details : ')
        name=input('Name')
        roll_no=input('Roll no')
        branch=input('Branch')
        year=input('Year')
        cgpa=input('CGPA')
        data=
        insert_rec(data)