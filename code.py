import random
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
number_games = int(input('Сколько раз играем? '))
score_player = 0
score_comp = 0
for i in range(number_games):
    player = str(input('Сделайте свой выбор: %s ' % options))
    comp = random.choice(options)
    print('Компьютер выбрал: %s' % comp)
    if (player == options[0] or player == options[1] or player == options[2]) and (comp == options[0] or comp == options[1] or comp == options[2]):
        if player == comp:
            print('_Ничья_')
        elif player == options[0] and comp == options[1]:
            print('_Вы выиграли_')
            score_player = score_player + 1
        elif player == options[1] and comp == options[2]:
            print('_Вы выиграли_')
            score_player = score_player + 1
        elif player == options[2] and comp == options[0]:
            print('_Вы выиграли_')
            score_player = score_player + 1
        elif comp == options[0] and player == options[1]:
            print('_Компьютер выиграл_')
            score_comp = score_comp + 1
        elif comp == options[1] and player == options[2]:
            print('_Компьютер выиграл_')
            score_comp = score_comp + 1
        elif comp == options[2] and player == options[0]:
            print('_Компьютер выиграл_')
            score_comp = score_comp + 1
    else:
        print('Ваша задача выбрать один из трех предметов %s.' % options)
    print('''
__Текущий счет__
_Компьютер %s:%s Вы_''' % (score_comp, score_player))
