import json

from dataclasses import dataclass

with open("db.json") as data:
    json_db = json.load(data)["data"]


@dataclass(repr=False)
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str

    def __repr__(self):
        return f"{self.id}"

    @staticmethod
    def get_all(self):
        print()

class Actions(Book):
    def delete(self):
        print()

    def add(self):
        title,author,year = input('Введите описание книги\n'), input('Введите автора\n'), input('Ведите год издания\n')
        self.title, self.author, self.year = title, author, int(year)
        print()

    def search(self):
        print()

    def modify(self):
        print()




a = Actions(**json_db[0])
a.add()
print()
