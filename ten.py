def f(text):
    t1 = 'kKкКвВнv'
    t2 = 'kKкК'
    t3 = 'vвВ'
    t4 = 'н'
    st = []
    bad = []
    for i in range(len(text)):
        for j in range(len(t1)):
            if t1[j] in text[i]:
                bad.append(text[i])
    for i in range(len(bad)):
        for j in range(len(t2)):
            if t2[j] in bad[i]:
                t1 = ''.join(filter(lambda x: x.isdigit(), bad[i]))
                p = 'ИКБО-' + t1[:2] + ' Вариант №' + t1[2:4]
                st.append(p)
        for j in range(len(t3)):
            if t3[j] in bad[i]:
                t1 = ''.join(filter(lambda x: x.isdigit(), bad[i]))
                p = 'ИВБО-' + t1[:2] + ' Вариант №' + t1[2:4]
                st.append(p)
        for j in range(len(t4)):
            if t4[j] in bad[i]:
                t1 = ''.join(filter(lambda x: x.isdigit(), bad[i]))
                p = 'ИНБО-' + t1[:2] + ' Вариант №' + t1[2:4]
                st.append(p)
    return st


text = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21',
            '1.3.py', 'В 11 4', '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23', '1.2.py, 1.3.py, 1.4.py', '1.1.py',
            'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10', 'ПитонН4 н11',
            'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']
print('Результат работы программы: ', f(text))