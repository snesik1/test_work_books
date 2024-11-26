import utills as bd

if __name__ == "__main__":
    while True:
        mod_program = (
            input(
                "Введите действие\n"
                "[1] - Добавить книгу\n"
                "[2] - Удалить книгу\n"
                "[3] - Изменить книгу\n"
                "[4] - Поиск книги\n"
                "[5] - Вывести все книги\n"
                "[6] - Выход\n"
            )
        )
        match mod_program:
            case "1":
                bd.add()
            case "2":
                bd.delete()
            case "3":
                bd.modify()
            case "4":
                bd.search()
            case "5":
                bd.get_all()
            case "6":
                break
            case _:
                print("Действие не найдено. Проверьте действие")
