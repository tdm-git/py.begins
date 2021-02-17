# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    name_list = {}
    for name in args:
        if name[0] in name_list.keys():                  # через оператор , gets() будет очень похож на in
            name_list[name[0]].append(name)
        else:
            name_list[name[0]] = [name]
        # element = name_list.setdefault(name[0], [name]) # через setdefault()
        # if element != [name]:
        #     element.append(name)
    print(name_list)

thesaurus("Иван", "Мария", "Сергей", "Петр", "Илья", "Игорь")  # условия задачи

list_name = ['Иван', 'Игоррь', 'Илья', 'Дима', 'Михаил']
list_name.sort()       # если нужна сортировка то можно как вариант отсортировать передаваемый список
thesaurus(*list_name)  # либо при выводе - отсртировать список ключей

# str_name = input('Введите список имён, через пробел - ')     # ввод списка пользователем
# thesaurus(*str_name.split(' '))                              # закомментировал т.к. нужно вводить =)
