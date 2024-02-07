f=open('students.csv')

for line in f.readlines():
    data = line.split(',')
    if data[4]=='None\n':
        data[4]==0

    if 'Хадаров Владимир' in data[1]:
        ocenka = int(data[4])
        id_work = data[2]
        print(f'Ты получил: {ocenka}, за проект - {id_work}')
        break