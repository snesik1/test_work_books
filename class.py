import json


from dataclasses import dataclass

with open("1.json") as data:
    json_db = json.load(data)

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str

class Work(Book):
    def delete(self):
        print()
    def add(self):
        print()
    def search(self):
        print()
    def modify(self):
        print()
    def get_all(self):
        print()

a = Work(**json_db['data'][0])
print()
test_work_books