def tabulate(table, headers=[]):
    #кол-во столбцов в строках должно совпадать, в headers кол-во столбцов может быть равно 0
    columns_count = len(table[0])
    columns_size = [0 for i in range(0, columns_count, 1)] #размер столбцов
    if len(headers):
        columns_count = len(headers)
        for i in range(0, len(headers), 1):
            columns_size[i] = len(headers[i])
    for row in table:
        if(len(row) != columns_count):
            print('Error')
            return
        for i in range(0, columns_count, 1):
            if columns_size[i] < len(row[i]):
                columns_size[i] = len(row[i])
    if len(headers) != 0:
        print(end='| ')
        for i in range(0, columns_count, 1):
            print(headers[i] + ' ' * (columns_size[i]-len(headers[i])), end=' | ')
        print()
    print(end='+')
    for i in range(0, columns_count, 1):
        print('-' * (columns_size[i]), end='--+')
    print()
    for row in table:
        print(end='| ')
        for i in range(0, columns_count, 1):
            print(row[i] + ' '*(columns_size[i]-len(row[i])), end=' | ')
        print()
    print(end='+')
    for i in range(0, columns_count, 1):
        print('-' * (columns_size[i]), end='--+')
    print()


table = [['ММ', '3', '6'], ['Построение бд', '1', '3'], ['АКМС', '2', '3'], ['ТПР', '2', '4']]
headers = ["Название предмета", "Кол-во сданных работ (шт)", "Кол-во оставшихся работ (шт)"]
tabulate(table, headers=headers)
