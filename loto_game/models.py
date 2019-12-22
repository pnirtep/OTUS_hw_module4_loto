import random

'''
Класс Карточка.
У него есть несколько методов: конструктор, вывод на экран и внесение изменений
'''
class Card:
    def __init__(self, name):
        self.name = name
        self.numbers = [x for x in range(1, 91)]
        self.counter = 15
        self.nums = random.sample(self.numbers, 15)

    '''
    def randomize(self):
        self.nums = random.sample(self.numbers, 15)
        return self.nums
    '''

    def display(self):
        res = 'Карточка: ' + self.name + '\n'
        print(res + (', '.join(str(value) for value in self.nums)) + '\n')
        return

    def change_card(self, barrel):
        indx = self.nums.index(barrel)
        self.nums.pop(indx)

    def check(self, barrel):
        if barrel in self.nums:
            return True
        else:
            return False

'''
Класс Мешок.
У него есть несколько методов: конструктор и извлечение случайного боченка
'''
class Bag:
    def __init__(self):
        self.bag = [x for x in range(1, 91)]
        self.counter = 90

    def random_barrel(self):
        self.barrel = random.choice(self.bag)
        indx = self.bag.index(self.barrel)
        self.bag.pop(indx)
        self.counter -= 1
        print('Число № ' + str(self.barrel) + '\nВ мешке осталось: ' + str(self.counter) + ' боченков\n')
        return self.barrel
