print("Привет друг!")
first_number = int(input("Введите первое число: "))
while True:
    znak = input("Введите знак: ")
    list_znak = ["+", "-", "*", "/"]
    if znak not in list_znak:
        print("Знак не корректен, повторите ввод")
    else:
        second_number = int(input("Введите второе число: "))
        try:
            if znak == "+":
                result = first_number + second_number
            elif znak == "-":
                result = first_number - second_number
            elif znak == "/":
                result = first_number / second_number
            else:
                result = first_number * second_number
            print(result)
            break
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            break
        