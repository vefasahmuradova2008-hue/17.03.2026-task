from db import get_connection

def insert_data():
    connection=get_connection()
    cursor=connection.cursor()

    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (1, 'Orxan Pamuk')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (2, 'Elif Shafak')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (3, 'George Orwell')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (4, 'J.K. Rowling')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (5, 'Fyodor Dostoevsky')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (6, 'Lev Tolstoy')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (7, 'Mark Twain')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (8, 'Jane Austen')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (9, 'Ernest Hemingway')")
    cursor.execute("INSERT INTO authors (auth_id, name) VALUES (10, 'Agatha Christie')")

    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (1, 'My Name is Red', 20, 1)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (2, 'The Bastard of Istanbul', 18, 2)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (3, '1984', 15, 3)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (4, 'Harry Potter', 25, 4)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (5, 'Crime and Punishment', 22, 5)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (6, 'War and Peace', 30, 6)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (7, 'Tom Sawyer', 17, 7)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (8, 'Pride and Prejudice', 19, 8)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (9, 'The Old Man and the Sea', 16, 9)")
    cursor.execute("INSERT INTO books (book_id, title, price, auth_id) VALUES (10, 'Murder on the Orient Express', 21, 10)")

    connection.commit()
    cursor.close()
    connection.close()

def show_data():
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("""
        select a.auth_id, a.name, b.book_id, b.price, b.title
        from authors a
        join books b on a.auth_id=b.auth_id
    """)
    rows=cursor.fetchall()

    for row in rows:
        print(row)
    connection.commit()
    cursor.close()
    connection.close()