import random

class Сharacter:
    def __init__(self):
        self.age = random.randint(15,80)
        self.profession = random.choice(['Пожарный',
        'Полицейский',
        'Военный',
        'Хирург',
        'Доктор',
        'Химик',
        'Физик',
        'Астро-физик',
        'Порноактер',
        'Сексолог',
        'Режисер',
        'Астролог',
        'Екстрасенс',
        'Диджей',
        'Сдесарь',
        'Сантехник',
        'Прораб',
        'Писатель',
        'Певец',
        'Менеджер',
        'Програмист',
        'Бухгалтер',
        'Продавец-консультант',
        'Зоолог',
        'Ветеринар',
        'Биолог',
        'Математик',
        'Переводчик',
        'Агроном'])
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
        phobia = random.randint(1,2)
        phobias = ['Айлурофобия',
            'Акустикофобия ',
            'Баллистофобия ',
            'Винофобия',
            'Арахнофобия',
            'Гидрофобия',
            'Декстрофобия',
            'Демофобия',
            'Зоофобия',
            'Клаустрофобия',
            'Клептофобия',
            'Никтофобия',
            'Нозофобия',
            'Орнитофобия',
            'Паразитофобия',
            'Рипофобия',
            'Акрофобия',
            'Танатофобия',
            'Фармакофобия',
            'Хемофобия',
            'Хоплофобия',
            'Эфебифобия',
            'Ятрофобия',
            'Спермофобия',
            'Дентофобия',
            'Гинекофобия',
            'Геронтофобия',
            'Мусофобия'
            ]

        if phobia == 1:
            self.phobia = 'Нет фобий'
        else:
            self.phobia = random.choice(phobias)

            
                
        self.inventory = random.choice(['Семена пшеницы',
        'Переносная електростанция',
        'Переносная гидроелектростанция',
        'Собака',
        'Кошка',
        'Аптечка',
        'Инструменты слесаря',
        'Продукты питания',
        'Алкоголь',
        'Распираторные маски',
        'Запас туалетной бумаги',
        'Сигнальный огонь',
        'Канистра с бензином',
        'Топор',
        'Медикаменты',
        'Дрова',
        'Набор швеи',
        'Охотничье ружье и патроны',
        'Консервы',
        'Огнетушитель'])

        disease = random.randint(1,2)
        health=['Алкоголизм',
            'СПИД',
            'Геморрой',
            'Деменция',
            'Наркомания',
            'Ожирение',
            'ОРВИ',
            'Панкреатит',
            'Плоскостопие',
            'Рак',
            'Сколиоз'
            'Сахарный диабет',
            'Туберкулёз',
            'Шизофрения',
            'Гиповитаминоз',
            'Игровое расстройство',
            'Гастрит',
            'Игровое расстройство',
            'Грип',
            'Слепота',
            'ПМА']

        if disease == 1:
            self.disease = 'Абсолютно здоров'
        else:
            self.disease = random.choice(health)

        self.hobby = random.choice(['Вязание',
            'Фитнес',
            'Пианино',
            'Гитара',
            'Геймер',
            'Спасать людей',
            'Калиграфия',
            'Охота на приведений',
            'Трейнсерфинг',
            'Рыбаловство',
            'Охота',
            'Гэокешинг',
            'Читать книги',
            'Волонтёрство',
            'Ходить в туалет',
            'Стритлюж',
            'Смотреть фильмы сериалы',
            'Смотреть аниме',
            'Колекционирование кукол Барби',
            'Дресировка голубей'])


                self.additional = random.choice(['Резидент комеди клаб',
                	'Ограбил банк',
                	'Тайный поклонник Марлин Монро',
                	'Альфасамец',
                	'Тайный агент',
                	''])

    def showrole(self):
        return f'''Возраст: {self.age},
Пол: {self.gender},
Профессия: {self.profession},
Характеристика: {self.characteristic},
Фобия: {self.phobia},
Инвентарь: {self.inventory},
Здоровье: {self.disease},
Хобби: {self.hobby},
Доп.Информация{self.additional}'''


def create_Character(quontity):
    for i in range(quontity):
        persone = Сharacter().showrole()

        return persone