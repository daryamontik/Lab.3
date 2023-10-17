content2 =[]
content = []

while True:
    print("Меню:")
    print("1. Ввести строки в файл F1")
    print("2. Скопировать строки из файла F1 в файл F2")
    print("3. Вывести строки из F2 на экран")
    print("0. Выход")

    choice = input("Введите номер выбранного варианта: ")

    if choice == '1':
        F1 = open("F1.txt", "w")

        while True:
            stroka = input('Введите строку для записи: ')
            if stroka == '':
                break
            F1.write(stroka + '\n')

        F1 = open("F1.txt", "r")
        content = F1.readlines()
        F1.close()

    elif choice == '2':

        if len(content) == 0:
            print("Ошибка: в файле F1 нет записей")

        else:



            F2 = open("F2.txt", "w")
            F2.writelines(content)
            F2.close()

            F2 = open("F2.txt", "r")
            content2 = F2.readlines()
            F2.close()

            print('Запись прошла успешно')

    elif choice == '3':

        if len(content2) == 0:
             print('Ошибка content2 устой')
        else:
             print(content2)