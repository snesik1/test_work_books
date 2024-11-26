import json

from dataclasses import dataclass
from os import path


def file_management(mod: str, write_data: None | list = None) -> None | list:
    """
    Управление операциями с файлом.

    Аргументы:
        mod (str): Режим работы. Выберите «w» (записать), «r» (читать) файл.
        write_data (список, необязательно): данные для записи в файл. По умолчанию — Нет.

    Возврат:
        list: Список словарей с данными из файла.
    """
    # Создание файла БД если его нет
    if not path.exists("db.json"): open('db.json', 'w', encoding="utf-8").close()

    with open("db.json", f"{mod}+", encoding="utf-8") as file:
        match mod:
            case "w":
                # Помещаем данные в файл
                write = json.dumps({"data": [data.__dict__ for data in write_data]})
                file.write(write)
            case "r":
                check_file = file.read()
                # Проверяем пустой на файл
                if len(check_file):
                    return json.loads(check_file)["data"]
                return []


@dataclass(repr=False)
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str

    def __repr__(self):
        return f"{self.id} {self.title} {self.author} {self.year} {self.status}"


class Cache(Book):
    """
    Общий кэш, хранящий данные о всех книгах.
    """

    all_books = [Book(**book) for book in file_management("r")]


def delete() -> None:
    """
    Удалить книгу
    Запрашивает у пользователя идентификатор книги.
    Если книга с данным идентификатором не найдена, выводит сообщение об ошибке.
    В противном случае удаляет книгу из списка всех книг, сохраняет изменения в db.json
    и выводит информацию об удаленной книге.
    """
    _id = int(input("Введите id книги\n"))
    delete_book = [book for book in Cache.all_books if book.id == _id][0]

    if delete_book is None:
        print("Книга не найдена. Проверьте id")
        return

    Cache.all_books.remove(delete_book)
    file_management("w", write_data=Cache.all_books)
    print("Книга удалена:\n", delete_book)


def modify() -> None:
    """
    Изменить статус книги.
    Запросите у пользователя идентификатор книги и статус, который нужно установить.
    Если книга с данным идентификатором не найдена, выведите сообщение об ошибке.
    Если статус не «1» или «2», выведите сообщение об ошибке.
    В противном случае измените статус книги и сохраните изменения в db.json.
    Распечатать модифицированную книгу.
    """
    _id = int(input("Введите id книги\n"))
    modify_book = [book for book in Cache.all_books if book.id == _id][0]
    if modify_book is None:
        print("Книга не найдена. Проверьте id")
        return

    status = (
        input(
            'Введите статус\n'
            '[1] - в наличии\n'
            '[2] - выдана\n'
        )
    )
    match status:
        case "1":
            modify_book.status = "в наличии"
        case "2":
            modify_book.status = "выдана"
        case _:
            print("Статус не найден. Проверьте статус")
    file_management("w", write_data=Cache.all_books)
    print("Книга изменена:\n", modify_book)


def add() -> None:
    """
    Добавить книгу
    Запросит у пользователя название, автора и год издания книги.
    Если год издания меньше 0 или больше 2024, выведите сообщение об ошибке.
    Создайте новую книгу, добавьте ее в список всех книг и сохраните изменения в db.json.
    Распечатайте добавленную книгу.
    """
    title, author, year = (
        input('Введите название книги\n'),
        input('Введите автора\n'),
        int(input('Ведите год издания\n'))
    )
    if 0 < year > 2024:
        return print("Введите корректный год")
    new_book = Book(id=len(Cache.all_books) + 1, title=title, author=author, year=year, status="в наличии")
    Cache.all_books = Cache.all_books + [new_book]
    file_management("w", write_data=Cache.all_books)
    print("Книга добавлена:\n", new_book)


def search() -> None:
    """
    Поиск книги
    Запросит у пользователя колонку и значение поиска.
    Если значение поиска пустое, выведите сообщение об ошибке.
    Если колонка не 1, 2 или 3, выведите сообщение об ошибке.
    В противном случае выведите книги, у которых значение
    в указанной колонке соответствует значению поиска.
    """
    mod, search_data = (
        input(
            "Колонка поиска\n"
            "[1] - название книги\n"
            "[2] - автор\n"
            "[3] - год издания\n"
        ),
        input(
            "Значение поиска\n"
        )
    )
    if search_data == "":
        print("Введите значение поиска")
        return

    match mod:
        case "1":
            return [print(book) for book in Cache.all_books if book.title == search_data]
        case "2":
            return [print(book) for book in Cache.all_books if book.author == search_data]
        case "3":
            return [print(book) for book in Cache.all_books if book.year == search_data]
        case _:
            print("Колонка не найдена. Проверьте колонку поиска")


def get_all() -> list[None] | None:
    """
    Вывести все книги
    Если книги нет, вывести сообщение об ошибке.
    В противном случае вывести все книги.
    """

    if not Cache.all_books:
        return print('База пуста')
    return [print(book) for book in Cache.all_books]
