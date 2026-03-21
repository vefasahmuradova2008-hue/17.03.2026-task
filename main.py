from db import create_table
from datalayer import insert_data, show_data

def main():

    try:
        create_table()
        print("Table created succesfully")
    except Exception as e:
        print("Table already exists or something went wrong", e)

    try:
        insert_data()
        print("Data inserted succesfully")
    except Exception as e:
        print("Something went wrong", e)

    try:
        show_data()
    except Exception as e:
        print("Something went wrong", e)

if __name__== "__main__":
    main()
