#1. Вычислить и вывести на экран длину окружности и площадь круга одного и того же заданного радиуса R, который необходимо ввести с клавиатуры в сантиметрах. Результаты должны округляться до сотых.
import math
R=int(input())
l=2*math.pi*R
S=math.pi**2*R
print(round(l,2), round(S,2))
#2. Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. Выведите значения переменных на экран до и после замены.
x=10
y=55
print(x,y)
a=x
s=y
y=a
x=s
print(x,y)
#3. Вычислить и вывести на экран период колебания маятника длиной L с точностью до сотых. Для рассчетов использовать формулу T = 2π√(L/g), где g – ускорение свободного падения (9.81 м/c2). Значение длины маятника в метрах необходимо ввести с клавиатуры.
import math
L=int(input())
g=9.81
T=2*math.pi*math.sqrt(L/g)
print(round(T,2))