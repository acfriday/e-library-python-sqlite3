import sqlite3

def connection_to_database():
	try:
		conn = sqlite3.connect('library.db')
	except sqlite3.Error as e:
		print(f"Error connecting to database: {e}")
		conn = None
	finally:
		return conn

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

def update_book(id, title, author, publisher):
	conn = connection_to_database()
	cursor = conn.cursor()
	try:
		cursor.execute("UPDATE books SET title = ?, author = ?, publisher = ? WHERE id = ?",
					   (title, author, publisher, id))
		if cursor.rowcount == 0:
			print("\n\n\nNo book with this ID exists in the database.")
		else:
			conn.commit()
	except sqlite3.Error as e:
		print(f"Error: {e}")
	finally:
		conn.close()

def list_books_from_author():
	conn = connection_to_database()
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT * FROM books")
		if cursor.rowcount == 0:
			print("\n\n\nThere are no books in the database currently.")
		else:
			books = cursor.fetchall()
			for book in books:
				print(book)
	except sqlite3.Error as e:
		print(f"Error: {e}")
	finally:
		conn.close()

def delete_book(id):
	conn = connection_to_database()
	cursor = conn.cursor()
	try:
		cursor.execute("DELETE FROM books WHERE id = ?", (id,))
		if cursor.rowcount == 0:
			print("\n\n\nNo book with this ID exists in the database.")
		else:
			conn.commit()
	except sqlite3.Error as e:
		print(f"Error: {e}")
	finally:
		conn.close()

def menu():
	while True:
		print("\n##### E-LIBRARY #####\n")
		print(
            "1. Add book information\n" \
			"2. List all books in the database\n" \
		    "3. Provide the ID of a book you would like to update details for\n" \
			"4. Provide the ID of a book you would like to delete\n" \
            "5. Enter '5' to exit the program from this main menu.\n"
		)
		response = input("Welcome! Enter your choice from the provided options above: ")
		if response == '1':
			title = input("Book title: ")
			author = input("Author name: ")
			publisher = input("Publisher name: ")
			add_book(title, author, publisher)

		elif response == '2':
				list_books_from_author()
	
		elif response == '3':
			try:
				id = int(input("ID of the book to update: "))
				title = input("New book title: ")
				author = input("New author: ")
				publisher = input("New publisher: ")
				update_book(id, title, author, publisher)
			except ValueError:
				print("\n\n\nInvalid input. Please enter a valid number.")

		elif response == '4':
			try:
				id = int(input("ID of the book to delete: "))
				delete_book(id)
			except ValueError:
				print("\n\n\nInvalid input. Please enter a valid number.")

		elif response == '5':
			break
		else:
			print("\n\n\nError! Invalid option selected, try again.")

if __name__ == '__main__':
	menu()