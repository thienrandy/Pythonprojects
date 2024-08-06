import sqlite3

db_name = "jordans.db"  # global variable


def connect_to_db():
    db_connect = sqlite3.connect(db_name)
    db_cursor = db_connect.cursor()
    print("Connected to Database.")
    return db_connect, db_cursor


def create_table(db_cursor):
    sql = """CREATE TABLE jordan_sneakers (
             id INTEGER PRIMARY KEY,
             self TEXT,
             model TEXT,
             color TEXT,
             release_year INTEGER,
             size REAL,
             price REAL
             )"""
    db_cursor.execute(sql)
    print("Created table")


def drop_table(db_cursor):
    sql = "DROP TABLE IF EXISTS jordan_sneakers"
    db_cursor.execute(sql)
    print("Dropped table.")


def insert_row(db_cursor):
    sql = "INSERT INTO jordan_sneakers (self, model, color, release_year, size, price) VALUES (?, ?, ?, ?, ?, ?)"
    self = input("Enter self (str): ")
    model = input("Enter the model (str): ")
    color = input("Enter the color (str): ")
    release_year = int(input("Enter year made (int): "))
    size = float(input("Enter the size (float): "))
    price = float(input("Enter the price (float): "))

    tuple_of_values = (self, model, color, release_year, size, price)

    db_cursor.execute(sql, tuple_of_values)
    print("Inserted row into Table.")


def select_all(db_cursor):
    sql = "SELECT * FROM jordan_sneakers"
    db_cursor.execute(sql)


def select_row(db_cursor):
    model = input("Enter the model to retrieve: ")
    sql = "SELECT * FROM jordan_sneakers WHERE model=?"
    db_cursor.execute(sql, (model,))


def update_row(db_cursor):
    model = input("Enter the model to update: ")
    release_year = int(input("Enter the new release year (int): "))
    price = float(input("Enter the new price (float): "))
    sql = "UPDATE jordan_sneakers SET release_year=?, price=? WHERE model=?"
    db_cursor.execute(sql, (release_year, price, model))


def delete_row(db_cursor):
    model = input("Enter the model to delete: ")
    sql = "DELETE FROM jordan_sneakers WHERE model=?"
    db_cursor.execute(sql, (model,))


def display_menu(db_connect, db_cursor):
    while True:
        print("Menu:")
        print("Enter S to get started and create a new database")
        print("Enter C to create a new row")
        print("Enter R to retrieve data")
        print("Enter U to update row")
        print("Enter D to delete a row")
        print("Enter Q to quit the program")
        choice = input("Enter your choice: ").upper()

        if choice == "S":
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == "C":
            insert_row(db_cursor)
        elif choice == "R":
            select_row(db_cursor)
        elif choice == "U":
            update_row(db_cursor)
        elif choice == "D":
            delete_row(db_cursor)
        elif choice == "Q":
            print("Goodbye")
            break
        else:
            print("Invalid choice of", choice)
        db_connect.commit()
        select_all(db_cursor)


def main():
    db_connect, db_cursor = connect_to_db()
    display_menu(db_connect, db_cursor)
    db_connect.close()


main()
