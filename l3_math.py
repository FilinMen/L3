import math 
print(" Радиус круга? ")
a = input()
print(" Радиус круга ", a, "см")
k = float(a)
PI = 3.14
b = float(2)
L = b * PI * k # длина окружности
S = PI * k * k # площадь круга
print(" Длинна окружности ", L ,"cm; Площадь круга ", S , "cm")#записать результата в см
Y = L/1000# перевод в метры
T = S/1000# перевод в метры
print(" Длинна окружности ", Y ,"m; Площадь круга ", T , "m")# записать результата в метрах
q = float(1/2) # для корня
p = (k * b)/ b ** q # сторона квадрата см
r = float(3) # перевыод от int в  float
w = k * r ** q # сторона равно сторонненго треугольника
x = k * b # сторона описаного квадрата
e = k/r # сторона  описанного равностороннего треугольника
v = 180
n = 22.5 * PI/ v
i = n * k # половина сторолны сторона восьмиугольника
m = i * b # сторона восьмиугольника
print("сторона восьмиугольника", m, "сторона  описанного равностороннего треугольника", e, "сторона описаного квадрата", x, "сторона квадрата ", p)
 




