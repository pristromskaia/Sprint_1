world_champions = {
    2002: 'Бразилия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

country = 'Италия'


# Добавляем в словарь  чемпиона 2022 года -  Аргентину.
world_champions[2022] = 'Аргентина'


# Выводим на экран всех чемпионов в формате год - страна.
for year, champion in world_champions.items():
    print(f'{year} - {champion}')


# Проверяем, выигрывала ли Италия в 21 веке. 
if country in world_champions.values():
    print(f'{country} cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')  
