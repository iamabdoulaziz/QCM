
def summ(title, **args):
    print("Titre :",title)
    result = 0
    for n in args.values():
        result += n
    return  result


print(summ("Sommes des notes :",maths =12, physique = 2, anglais =14))
