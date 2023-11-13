import src.main.python.db.worker_db as worker_db


def main():
    menu()
    return 0


def menu():
    while True:
        a = input("Choose your action:\n"
                  "'1' Init db\n"
                  "'0' Exit\n")

        if a == "1":
            worker_db.init_database()
            print("db inited")
        elif a == "0":
            return


if __name__ == "__main__":
    main()

