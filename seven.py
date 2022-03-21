def func(**keywords):
    for kw in keywords:
        print(kw, "=", keywords[kw])

kword = {'meow' : "мяу", 'gav' : "гав", 'sh' :"шшш"}
func(**kword)
