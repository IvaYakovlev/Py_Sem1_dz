# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой 
# билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
#     001001 -> yes

x = int (input())
sum1 = x//100000+(x//10000)%10+(x//1000)%10
sum2 = (x//100)%10+(x//10)%10+x%10
if sum1==sum2:
    print ("yes")
else:
    print ("no")
