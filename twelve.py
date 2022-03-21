with open("/Users/macbook/Desktop/Программирование на Питон/Практическая работа 2/for12.md", 'r+') as f:
    Stringtext = f.readlines()
    closed = False
    flag = True
    for line in Stringtext:
        for i in range(len(line)):
            if line[i] == '"':
                if closed:
                    line = line[:i] + ">" + line[i+1:]
                    closed = False

                else :
                    line = line[:i] + "<" + line[i+1:]
                    closed = True
        if flag:
            f.write('\n'+line)
            flag = False
        else:
            f.write(line)
    print(line)
# [:i] - берем все до i-го элемента
# [i:] - берем все после i-го элемента