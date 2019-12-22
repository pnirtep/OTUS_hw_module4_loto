from loto_game.models import Card, Bag


player_name = input('Введите ваше имя: ')

player = Card(player_name)
#player.randomize()
computer = Card('Компьютер')
#computer.randomize()
bag = Bag()

while True:


    player.display()
    computer.display()
    '''
    if player.display() == computer.display():
        print('Повторные карточки, перезапустите игру....')
        exit()
    else:
        continue
    '''
    if player.counter == 0 and computer.counter == 0:
        print('ничья')
        exit()
    elif player.counter < 1:
        print('Победа пользователя')
        exit()
    elif computer.counter < 1:
        print('Победа компьютера')
        exit()
    else:
        barrel = bag.random_barrel()
        print("Удалить число? Y/N/Q")
        reply = input()
        if computer.check(barrel):
            computer.change_card(barrel)
            computer.counter -= 1
        else:
            pass
        while len(reply) == 0 or reply not in ('Y', 'N', 'Q'):
            print('Ответ не распознан!\n')
            reply = input("Удалить число? Y/N/Q ")
            reply = reply.lower()
        if reply.lower() == 'y':
            if player.check(barrel):
                player.change_card(barrel)
                player.counter -= 1
            else:
                print('Боченка не было в вашей карточке, вы проиграли!')
                exit()
        elif reply.lower() == 'n':

            if player.check(barrel):
                print('Вы не заметили боченок в карточке, вы проиграли!')
                exit()
            else:
                continue
        elif reply.lower() == 'q':
            print('Вы завершили игру. До встречи!')
            exit()

        else:
            print('Неверое значение')