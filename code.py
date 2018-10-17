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
    comp = str(input('Сделайте выбор за компьютер: %s ' % options))
    if (player == options[0] or player == options[1] or player == options[2]) and (comp == options[0] or comp == options[1] or comp == options[2]):
        if player == comp:
            print('Ничья')
        elif player == options[0] and comp == options[1]:
            print('Вы выиграли')
            score_player = score_player + 1
        elif player == options[1] and comp == options[2]:
            print('Вы выиграли')
            score_player = score_player + 1
        elif player == options[2] and comp == options[0]:
            print('Вы выиграли')
            score_player = score_player + 1
        elif comp == options[0] and player == options[1]:
            print('Компьютер выиграл')
            score_comp = score_comp + 1
        elif comp == options[1] and player == options[2]:
            print('Компьютер выиграл')
            score_comp = score_comp + 1
        elif comp == options[2] and player == options[0]:
            print('Компьютер выиграл')
            score_comp = score_comp + 1
    else:
        print('Ваша задача выбрать один из трех предметов %s.' % options)
    print('Текущий счет Компьютер %s:%s Вы' % (score_comp, score_player))
