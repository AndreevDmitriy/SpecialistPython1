# Иван кладет в банк x рублей под a процентов годовых на n лет. Напишите функцию, которая возвращает число -
# сколько денег получит Иван в результате.

def deposit(x, a, n):
    for i in range(n):
        x+=x*a

    return x
def deposit12(x, a, n):
    for i in range(12*n):
        x+=x*a/12

    return x
# функция принимает три числа и возвращает одно - итоговая сумма на счету Ивана.
# Проценты на вклад начисляются один раз в год.

x=10
a=0.05
n=10
# m=12
# print(x*(1+a)**n)
# print(x*(1+a/m)**(m*n))
print(deposit(x,a,n))
print(deposit12(x,a,n))
# функция принимает три числа и возвращает одно - итоговая сумма на счету Ивана.
# Проценты на вклад начисляются один раз в год.
