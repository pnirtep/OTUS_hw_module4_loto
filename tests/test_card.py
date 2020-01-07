from loto_game.models import Card,  Bag

'''
Проверяем то, что карточка создается с уникальным набором чисел
'''

def test_card():
    card = Card('Карточка')
    s = set(card.nums)
    assert len(s) == len(card.nums)


'''
Проверяем удаление элементов из карточки функцией change_card
'''
def test_change_card():
    card = Card('Карточка')
    l = len(card.nums)
    x = card.nums[0]
    card.change_card(x)
    assert len(card.nums) == l - 1

'''
Првоеряем, что возвращаемый объект функции random_barrel находится в нужном нам диапазоне чисел
'''
def test_random_barrel():
    bag = Bag()
    assert bag.random_barrel() in [x for x in range(1, 91)]


def test_random_barrel_1():
    card = Card('Карточка')
    bag = Bag()
    assert bag.random_barrel() in card.numbers


'''
Првоеряем, что вызов random_barrel уменьшает counter мешка с боченками
'''
def test_random_barrel_3():
    bag = Bag()
    len_bag = len(bag.bag)
    bag.random_barrel()
    assert len(bag.bag) == len_bag - 1

'''
Првоеряем, что вызов random_barrel (если диапазон превышает 1-90, например, 91) вызывает ошибку IndexError,
что означает, что из мешка можно достать РОВНО 90 боченков
'''
def test_random_barrel_4():
    bag = Bag()
    count = 0
    while True:
        try:
            bag.random_barrel()
            count += 1
        except IndexError:
            print('Всё, боченки закончились')
            break
    assert count == 90


