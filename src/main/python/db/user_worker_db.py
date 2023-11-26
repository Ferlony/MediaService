import src.main.python.db.worker_db as worker_db
import argparse


def main(option):
    if option:
        menu(option)
    else:
        flag = True
        while flag:
            try:
                a = int(input("Choose your action:\n"
                            "'1' Init db\n"
                            "'0' Exit\n"))
                flag = menu(a)
            except Exception as e:
                print(e)
            
    return


def menu(a):
    if a == 1:
        worker_db.init_database()
        print("db inited")
    elif a == "0":
        return False
    
    return True


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-a", "--option", type=int, required=True, help="Init db = 1")
    pargs = arg_parser.parse_args()
    main(pargs.option)
