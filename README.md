# E-Library Database

This project is a simple E-Library database implemented in Python using SQLite3. It allows users to perform create, read, update, and delete (CRUD) operations on the database.

## Database Structure

The Library database consists of a single table named `books` with the following columns:

- `id`: An integer that serves as the primary key for our table.
- `title`: A text field that stores the title of the book.
- `author`: A text field that stores the name of the author.
- `publisher`: A text field that stores the name of the publisher.

```py
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT NOT NULL,
publisher TEXT NOT NULL,
UNIQUE(title, author, publisher)
```

## Functions

The project includes the following main functions:

- `connection_to_database()`: Establishes a connection to the SQLite3 database.
```py
import sqlite3

def connection_to_database():
	try:
		conn = sqlite3.connect('library.db')
	except sqlite3.Error as e:
		print(f"Error connecting to database: {e}")
		conn = None
	finally:
		return conn
```

- `create_table()`: Creates the `books` table in the database.
```py
def create_table():
	try:
		conn = connection_to_database()
		cursor = conn.cursor()
		cursor.execute('''
			CREATE TABLE IF NOT EXISTS books(
			id INTEGER PRIMARY KEY,
			title TEXT NOT NULL,
			author TEXT NOT NULL,
			publisher TEXT NOT NULL,
			UNIQUE(title, author, publisher))
			''')
		conn.commit()
	except sqlite3.Error as e:
		print(f"Error creating table: {e}")
	finally:
		conn.close()
create_table()
```

- `add_book(title, author, publisher)`: Adds a new book to the database.
```py
def add_book(title, author, publisher):
	conn = connection_to_database()
	cursor = conn.cursor()
	try:
		cursor.execute("INSERT INTO books(title, author, publisher) VALUES (?, ?, ?)",
				 (title, author, publisher))
		conn.commit()
	except sqlite3.IntegrityError:
		print('\n\nError: A book with this title, author, and publisher already exists, or a required field is empty.')
	finally:
		conn.close()
```


## Requirements
sqlite3==3.45.1

## Usage

To run the program, simply execute the `e-library.py` script. You will be presented with a menu of options to add a book, list all books, update a book's details, delete a book, or exit the program.

```
> py .\e-library.py
```

**Menu**

![image](https://github.com/acfriday/e-library-python-sqlite3/assets/82184168/946eb0ae-9054-4e4b-886d-cd8eab99807c)

**Adding a book**

![image](https://github.com/acfriday/e-library-python-sqlite3/assets/82184168/9f754183-2eae-48d6-88d1-f39023da0c91)


**List all books to verify the book was added**

![image](https://github.com/acfriday/e-library-python-sqlite3/assets/82184168/d7183ddf-0086-47ae-a541-bdd89e818fb1)


**Update a specific book providing its ID**

![image](https://github.com/acfriday/e-library-python-sqlite3/assets/82184168/1cef0b97-ac6a-40a3-9b93-fd9d99df1eb0)


**List all books to verify the update was successful**

![image](https://github.com/acfriday/e-library-python-sqlite3/assets/82184168/73ffdc3a-4198-4b5d-bc0d-82cd9757b8d3)

**Delete a specific book providing its ID**

![image](https://github.com/acfriday/e-library-python-sqlite3/assets/82184168/27fd8575-57f9-4ac5-a19a-aa9ca84c823b)

**List all books to verify the deletion was successful**

![image](https://github.com/acfriday/e-library-python-sqlite3/assets/82184168/7bb7d483-7c71-4b65-8cbe-4ab003b297c1)
