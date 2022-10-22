# генерация случайного int списка
from msvcrt import kbhit
import random
def Create_random_list (size):
   my_list = list()
   for i in range (size):
      num = random.randint(1,10)
      my_list.insert(i, num)
   print ()
   print ("список представлен ниже:")
   print (my_list)
   print ()
   return my_list

# ввод int списка с клавиатуры
def Create_handle_list (size):
   my_list = list()
   print ()
   for i in range (size):
      print("Введите элемент №", i+1,":  ", end='')
      num = int(input())
      my_list.insert(i, num)
   print ()
   print ("список представлен ниже:")
   print (my_list)
   return my_list

# генерация случайного float списка
import random
def Create_random_float (size):
   my_list = list()
   for i in range (size):
      num = round((10 * (random.random())), 2)
      my_list.insert(i, num)
   print ()
   print ("список представлен ниже:")
   print (my_list)
   print ()
   return my_list
   
# ввод float списка с клавиатуры
def Create_handle_float (size):
   my_list = list()
   print ()
   for i in range (size):
      print("Введите элемент №", i+1,":  ", end='')
      num = float(input())
      my_list.insert(i, num)
   print ()
   print ("список представлен ниже:")
   print (my_list)
   return my_list


'''
# 1.  Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# складываем нечетные элементы списка
def elem_sum (my_list):
   size = len(my_list)
   sum = 0
   i = 1
   while (i < (size)):
      sum = sum + int(my_list[i])
      i = i + 2
   print("Сумма элементов на нечетных позициях = ", sum,)


digit = int(input("Введите количество элементов списка: "))
var = int(input("задать список автоматом (1) или вручную (2): "))
if (var == 1):
   new_list = Create_random_list(digit)
   elem_sum(new_list)
elif (var == 2):
   new_list = Create_handle_list(digit)
   elem_sum(new_list)
else: 
    print ("неверный номер")
'''


'''
# 1.  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# умножаем пары чисел из списка
def elem_mult (my_list):
   size = len(my_list)
   # проверка на четность (числа элементов)
   if (size%2 == 0):
      list_end = int(size/2)
   else:
      list_end = int(size/2) + 1
   # результат запишем в список
   result = list()
   buffer = 0
   for i in range(list_end):
      buffer = (int(my_list[i])) * (int(my_list[size - 1 - i]))
      result.append(buffer)
   print("произведения пар чисел представлены ниже")
   print(result)

digit = int(input("Введите количество элементов списка: "))
var = int(input("задать список автоматом (1) или вручную (2): "))
if (var == 1):
   new_list = Create_random_list(digit)
   elem_mult(new_list)
elif (var == 2):
   new_list = Create_handle_list(digit)
   elem_mult(new_list)
else: 
    print ("неверный номер")
'''

'''
# 1. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# поиск дробных частей
def diff_find (my_list):
   size = len(my_list)
   buffer = 0
   new_float_list = list()
   for i in range (size):
      #разделили на 1, взяли только целую часть, вычли из исх числа, округлили 
      buffer = round (((my_list[i])) - (int (my_list[i] / 1)), 2)  
      new_float_list.append(buffer)
   print ("список дробных частей представлен ниже:")
   print (new_float_list)
   print ()
   
   max_element = max(new_float_list)
   min_element = min(new_float_list)
   dif = max_element - min_element
   print("Max значение дробной части = ", max_element)
   print("Min значение дробной части = ", min_element)
   print("Разница между Max и Min значениями дробной части = ", dif)

digit = int(input("Введите количество элементов списка: "))
var = int(input("задать список автоматом (1) или вручную (2): "))
if (var == 1):
   new_list = Create_random_float(digit)
   diff_find(new_list)
elif (var == 2):
   new_list = Create_handle_float(digit)
   diff_find(new_list)
else: 
    print ("неверный номер")
'''


'''
# 1.  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# пользователь вводит число, считываем его 
digit = int(input("Введите число: "))
digit_2 = digit
print()

#результат сохраним в список
buffer = []                    

#перевод в двоичную систему
while (1):
  if (digit_2 == 0):
    break
  elif (digit_2 != 0):
      buffer.insert(0,(int(digit_2 % 2))) # запишем в результат остаток от деления на 2
      digit_2 = int((digit_2 / 2)) # целая часть от деления на 2, в цикл вернется эта часть 
    
print("В двоичном виде число", digit , "выглядит так: ")  
for i in range(len(buffer)):
    print (buffer[i], end='')
print()
'''


'''
# 1. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def Fib_numbers (number):
   # вывод в список с "+" значениями, и список с "-" значениями
   p_list = list()
   n_list = list()    
   
   # получаем список с "+" значениями
   p_list.insert (0, 0)
   p_list.insert (1, 1)
   for i in range(2, number+1):
      p_list.insert (i, (p_list[i-1] + p_list[i-2]))

   # получаем список с "-" значениями
   n_list.insert (0, 0)
   n_list.insert (1, 1)
   for i in range(2, number+1):
      n_list.insert (i, (n_list[i-2] - n_list[i-1]))
   n_list.reverse()  #инвертируем полученный список 

   # соединяем "+" и "-" списки, удаляем дублирующийся ноль
   result = n_list + p_list
   del result[number+1]
   
   print("Числа Фибоначчи представлены ниже: ")  
   print (result)

digit = int(input("Введите число: "))
print ()
Fib_numbers (digit)
'''