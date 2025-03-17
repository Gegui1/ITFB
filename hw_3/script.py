import csv
import json

with open("books.csv", newline="") as book_file:
    reader = csv.DictReader(book_file)
    books = list(reader)

with open("user.json") as user_file:
    users = json.load(user_file)


min_books = len(books) // len(users)
remainder = len(books) % len(users)
book_index = 0

for i, user in enumerate(users):
    num_books_to_give = min_books + (1 if i < remainder else 0)
    user["books"] = books[book_index: book_index + num_books_to_give]
    book_index += num_books_to_give


with open('result.json', 'w') as result:
    json.dump(users, result, indent=4)