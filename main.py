numb_input = int(input("Введите кол-во элементов списка: "))
str_input = str(input("Введите строковое значение: "))
list_str = []
x = 0
while x <= numb_input:
    if x % 2 == 0:
        list_str.append(str_input)
    else:
        list_str.append(x)
    x+=1
print(list_str)