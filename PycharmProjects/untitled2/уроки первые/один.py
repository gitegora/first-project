# -*- coding: utf-8 -*-

print 'Введите коэфициенты уравнения'

print '**'

b = int (input("Напишите коэфициент A :"))
a = int (input("Напишите коэфициент B :"))
c = int (input("Напишите коэфициент C :"))

D = b**2 - 4 * a * c;
print ("D = %.2f" % D)

if D > 0:
        import math
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif D == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)

else:
        print("нет корней")
