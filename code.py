rules = '''В данной игре вы соревнуетесь с компьютером.
Ваша задача выбрать один из трех предметов «Камень», «Ножницы» или «Бумага».
Компьютер так же сделает свой выбор.
«Камень» побеждает «Ножницы»
«Ножницы» побеждают «Бумагy»
«Бумага» побеждает «Камень»
Если выбор одинаков, засчитывается ничья.
Желаем удачи
'''

options = ['Камень', 'Ножницы', 'Бумага']

name = input('Как вас зовут? ')

print('Привет, %s ' % name)
print(rules)

player = str(input('Сделайте свой выбор: %s ' % options))
comp = str(input('Сделайте выбор за компьютер: %s ' % options))