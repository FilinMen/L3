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
Y = L/100# перевод в метры
T = S/10000# перевод в метры
print(" Длинна окружности ", Y ,"m; Площадь круга ", T , "m")# записать результата в метрах
#q = float(1/2) # для корня
p = (k * b)/ math.sqrt(b)# сторона квадрата см
r = float(3) # перевыод от int в  float
c = math.sqrt(r)
w = k * math.sqrt(r)  # сторона равно сторонненго треугольника
x = k * b # сторона описаного квадрата
e = k * math.sqrt(r) * b # сторона  описанного равностороннего треугольника !!!!!!!

m = 2 * k * (2**0.5 - 1) # сторона восьмиугольника !!!!!!!
print("сторона восьмиугольника", m, "сторона  описанного равностороннего треугольника", e, "сторона равно сторонненго треугольника", w,"сторона описаного квадрата", x, "сторона квадрата ", p)
 




