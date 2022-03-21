s = ['1', '2', '3', '4', '5', '6']
new_s = list(map(int, s)) #преобразование из строковой в числовую форму
s.count()#подсчет кол-ва элементов
s.reverse()#разворот последователньости
def get_index(s, x): #поиск индексов вех вхождений x
    return [i for i in range(len(x)) if s[i] == x]
def count(s): #сложение четных индексов
    return [sum([s[i] for i in range(len(s)) if i % 2 == 0])]
def get_max_str(s): #вывод максимальной строки
    return max(s, key=len)
