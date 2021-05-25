# Доработайте предыдущую программу так, чтобы каждый сгенерированный сотрудник
# был уникальным(не должны повторяться комбинации Имя + Фамилия).
from random import choice, randint

names_list = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил',
              'Никита', 'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Тимофей', 'Владислав',
              'Игорь', 'Владимир', 'Павел', 'Руслан', 'Марк', 'Константин', 'Тимур', 'Олег', 'Ярослав', 'Антон',
              'Николай', 'Данил']
prof_list = ['Аудитор', 'Актуарий', 'Аналитик', 'Банкир', 'Брокер', 'Бухгалтер', 'Дилер', 'Продавец', 'Инкассатор',
             'Коммерческий директор', 'Кредитный консультант', 'Маркетолог', 'Маклер биржевой',
             'Менеджер по работе с клиентами', 'Налоговый инспектор', 'Операционист', 'Предприниматель', 'Сметчик',
             'Снабженец', 'Страховой агент', 'Релайтер', 'Товаровед', 'Торговый представитель', 'Тренд-вотчер',
             'Трейдер', 'Экономист', 'Экспедитор', 'Финансист', 'Кассир']
vowels = ["а", "е", "и", "о", "у", "ы", "э", "ю", "я"]
sur_names_list = []
for name in names_list:
    if name[-1] in vowels:
        sur_names_list.append(name[:-1] + "ин")
    elif name[-1] in ("й", "ь"):
        sur_names_list.append(name[:-1] + "ев")
    else:
        sur_names_list.append(name + "ов")
staff_list = []
names_set=set()
count=0
for i in range(1000):
    while True:
        surname = choice(sur_names_list)
        name = choice(names_list)
        if " ".join([surname, name]) not in names_set:
            staff_list.append({"numb": i+1 ,"surname": surname, "name": name , "age":randint(22, 65),
                               "profession": choice(prof_list), "salary": randint(30, 300) * 1000})
            names_set.add(" ".join([surname, name]))
            break
        else:
            count+=1
staff_list.sort(key=lambda x: (x["numb"], x["surname"], x["name"]))
print("Список сотрудников:")
for el in staff_list: print(el)
print(f"Количество выпавших повторений равно: {count}")
