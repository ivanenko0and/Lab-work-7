"""
Вивести дані про книги, в яких кількість сторінок більше 150. Поля
структури: Автор, Кількість сторінок, Тираж, Рік видання.
"""

answer = '1'
while answer == '1':

    books = {}
    print("Введіть дані для довільної послідовності книг(натисніть пробіл, щоб завершити введення):")
    while True:

        n = {len(books)+1: [input(f"Введіть автора книги №{len(books)+1}:"), 0, 0, 0]}

        if n[len(books)+1][0] == "" or n[len(books)+1][0] == " ":
            break

        while True:
            try:
                n[len(books)+1][1] = int(input(f"Введіть кількість сторінок книги №{len(books)+1}:"))
                if n[len(books)+1][1] <= 0:
                    print("Вводьте правильні дані!")
                else:
                    break
            except ValueError:
                if n[len(books)+1][1] == int():
                    break
                else:
                    print("Вводьте правильні дані!")
        if n[len(books)+1][1] == int():
            break

        while True:
            try:
                n[len(books)+1][2] = int(input(f"Введіть тираж книги №{len(books)+1}:"))
                if n[len(books)+1][2] <= 0:
                    print("Вводьте правильні дані!")
                else:
                    break
            except ValueError:
                if n[len(books)+1][2] == int():
                    break
                else:
                    print("Вводьте правильні дані!")
        if n[len(books)+1][2] == int():
            break

        while True:
            try:
                n[len(books)+1][3] = int(input(f"Введіть рік видання книги №{len(books)+1}:"))
                if n[len(books)+1][3] < 1460 or n[len(books)+1][3] > 2020:
                    print("Введіть правильний рік!")
                else:
                    break
            except ValueError:
                if n[len(books)+1][3] == int():
                    break
                else:
                    print("Вводьте правильні дані!")

        if n[len(books)+1][3] == int():
            break

        books.update(n)
        print("───────────────────────────────────────────────────────────")

    max = [7, 5, 18, 5]
    if max[0] < len(books):
        max[0] = len(books)
    for i in books.values():
        if max[1] < len(str(i[0])):
            max[1] = len(str(i[0]))
        if max[2] < len(str(i[1])):
            max[2] = len(str(i[1]))
        if max[3] < len(str(i[2])):
            max[3] = len(str(i[2]))

    print("───────────────────────────────────────────────────────────")
    print("Список книг, в яких кількість сторінок більше 150:")
    print(f" {'Книга №':^{max[0]}} | {'Автор':^{max[1]}} | {'Кількість сторінок':^{max[2]}} | {'Тираж':^{max[3]}}\
 | Рік видання")
    for i in books.items():
        if i[1][1] > 150:
            print(f" {i[0]:^{max[0]}} | {i[1][0]:^{max[1]}} | {i[1][1]:^{max[2]}} | {i[1][2]:^{max[3]}}\
 | {i[1][3]:^11}")

    print("───────────────────────────────────────────────────────────")
    answer = input("Введіть '1' для повторення:")

# Виконав Іваненко Андрій Вадимович
