import random

class Сharacter:
    def __init__(self):
        self.age = random.randint(15,80)
        self.profession = random.choice(['Пожарный',
        'Полицейский',
        'Военный',
        'Хирург',
        'Медсестра',
        'Химик',
        'Физик',
        'Астро-физик'])
        self.characteristic = random.choice(['Агрессия',
        'Алчный',
        'Бездарный',
        'Вежливый',
        'Гордый',
        'Добрый',
        'Коварный',
        'Ленивый',
        'Лицемерный',
        'Мудрый',
        'Наглый',
        'Настойчивый',
        'Недотрога',
        'Отважный',
        'Патриот',
        'Подлый',
        'Пунктуальный',
        'Раздражительный',
        'Самопожертвованый',
        'Самоуверенный',
        'Скромный',
        'Смелый',
        'Спокойный',
        'Трусливый',
        'Упрямистый',
        'Хитрый',
        'Храбрый',
        'Эгоистический'])
        self.gender = random.choice(['Мужчина', 'Женщина'])

    def showrole(self):
        return f'''Возраст: {self.age},
Пол: {self.gender},
Профессия: {self.profession},
Характеристика: {self.characteristic},
Фобия: {None}'''


def create_Character(quontity):
    for i in range(quontity):
        persone = Сharacter().showrole()

        return persone