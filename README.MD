Реализуйте имитацию игры в лото.

Есть два участника - компьютер и игрок.

В начале игры вы и компьютер получаете карточку, которая хранит 15 случайных двузначных числа.
Далее ведущий вытягивает случайное число из мешка с 90 боченками.

Если выпавшее число у вас есть. Вы удаляете его из своей карточки.
Игра продолжается, пока один из игроков не опустошит свою карточку.

Программа умеет проверять карточки на честность - если вы жульничаете, игра заканчивается, победжает компьютер.
Программа умеет проверять вас на внимательность - если вы не заметили число, игра заканчивается, победжает компьютер.

В случае, если под конец игры вы заканчиваете с одинаковым количеством оставшихся номерков в карточках - ничья!

----------------

Внутри два файла loto.py и models.py
В loto.py осуществялется логика самой игры, проверки на наличие чисел в карточках и ход игры
В models.py осуществляется создание классов - карточка, мешок.