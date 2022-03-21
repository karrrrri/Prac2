import sys

def print_my(arg):
    stdout = sys.stdout#объект выходного файла
    if (type(arg)) == int:
        stdout.write(str(arg) + '\n')
    if (type(arg)) == str:
        stdout.write(arg + '\n')
    if (type(arg)) == list:
        stdout.write('[')
        for i in range(0, len(arg)):
            if i != len(arg)-1:
                stdout.write("'" + arg[i] + "', ")
            else:
                stdout.write("'" + arg[i] + "']")

num = 123
str_1 = 'мяу'
lst = ['к', 'р', 'я']
print_my(num)
print_my(str_1)
print_my(lst)
