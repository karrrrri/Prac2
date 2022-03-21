import random

def check (str):
    str_list = list(str)
    for i in range (0, len(str_list)):
        if str_list[i-1] in {'ш', 'ж'}:
            if str_list[i] == 'ы':
                str_list[i] = 'и'
        if str_list[i - 1] in {'щ', 'ч'}:
            if str_list[i] == 'я':
                str_list[i] = 'а'
            if str_list[i] == 'ю':
                str_list[i] = 'у'
    str = ''.join(str_list)
    return str


def surname(vowels, consonants):
    surname_list = []
    for i in range (0, 11):
        str = ''
        for j in range (0, random.randint(5, 7)):
            if j == 0:
                str += consonants[random.randint(0, 20)]
            else:
                if j % 2!=0:
                    str += vowels[random.randint(0, 7)]
                else:
                    str += consonants[random.randint(0, 20)]
        str = check(str)
        surname_list.append(str.capitalize())
    return surname_list

def create (names, surname_list, patronymics):
    fio_list = []
    for i in range (0, 11):
        str = ''
        str += ''.join(names[random.randint(0, 23)]) + ' ' + ''.join(patronymics[random.randint(0, 11)].capitalize()) +\
               '. ' + ''.join(surname_list[i])
        fio_list.append(str)
    return fio_list


names = ['Александр', 'Сергей', 'Дмитрий', 'Алексей', 'Андрей', 'Максим',
             'Евгений', 'Владимир', 'Иван', 'Михаил', 'Николай', 'Денис', 'Роман',
             'Игорь', 'Артем', 'Павел', 'Олег', 'Юрий', 'Антон', 'Владислав', 'Виктор', 'Никита', 'Виталий', 'Илья']
vowels = ['а', 'у', 'о', 'ы', 'и', 'я', 'ю', 'е']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
              'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
patronymics = ['б', 'в', 'г', 'д', 'л', 'м', 'н', 'п', 'с', 'а', 'и', 'о']
surnames = surname(vowels, consonants)
fio_list = create(names, surnames, patronymics)
print('Список сгенерированных ФИО: ')
print(*fio_list, sep="\n", end="\n\n")

