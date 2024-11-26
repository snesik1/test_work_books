import json
import os

from dataclasses import dataclass


def file_management(mod: str, write_data: None | list = None) -> None | list:
    if not os.path.exists("db.json"): open('db.json', 'w', encoding="utf-8").close()
    with open("db.json", f"{mod}+", encoding="utf-8") as file:
        match mod:
            case "w":
                write = json.dumps({"data": [data.__dict__ for data in write_data]})
                file.write(write)
            case "r":
                check_file = file.read()
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
    all_books = [Book(**book) for book in file_management("r")]


def delete():
    _id = int(input("Введите id книги\n"))
    delete_book = [book for book in Cache.all_books if book.id == _id][0]

    if delete_book is None:
        print("Книга не найдена. Проверьте id")
        return

    Cache.all_books.remove(delete_book)
    file_management("w", write_data=Cache.all_books)
    print("Книга удалена:\n", delete_book)

def modify():
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


def add():
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


def search():
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


def get_all():
    if not Cache.all_books:
        return print('База пуста')
    return [print(book) for book in Cache.all_books]
