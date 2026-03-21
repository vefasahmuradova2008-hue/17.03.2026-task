import oracledb

def get_connection():
    return oracledb.connect(
        user="SYS",
        password="123456789",
        dsn="localhost:1521/XEPDB1",
        mode=oracledb.SYSDBA
    )
def create_table():
    conn=get_connection()
    cursor= conn.cursor()
    try:
        cursor.execute("DROP TABLE books")
    except:
        pass
    try:
        cursor.execute("DROP TABLE authors")
    except:
        pass

    cursor.execute("""
    create table authors(
    auth_id int primary key,
    name varchar(255))
    """)

    cursor.execute("""
    create table books(
    book_id int primary key,
    title varchar(255),
    price int,
    auth_id int,
    
    CONSTRAINT fk_author FOREIGN KEY (auth_id) REFERENCES authors(auth_id))
    """)

    conn.commit()
    cursor.close()
    conn.close()
