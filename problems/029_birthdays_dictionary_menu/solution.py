# Birthdays Dictionary Menu (Corrected Version)

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    birthdays = {}
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
        elif choice == QUIT:
            print("Goodbye!")


def get_menu_choice():
    print()
    print("Friends and Their Birthdays")
    print("---------------------------")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quit the program")
    print()

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if LOOK_UP <= choice <= QUIT:
                return choice
            else:
                print("Enter a valid choice.")
        except ValueError:
            print("Enter a number.")


def look_up(birthdays: dict) -> None:
    name = input("Enter a name: ")
    print(birthdays.get(name, "Not found."))


def add(birthdays: dict) -> None:
    name = input("Enter a name: ")
    if name in birthdays:
        print("That entry already exists.")
    else:
        bday = input("Enter a birthday: ")
        birthdays[name] = bday


def change(birthdays: dict) -> None:
    name = input("Enter a name: ")
    if name in birthdays:
        bday = input("Enter the new birthday: ")
        birthdays[name] = bday
    else:
        print("That name is not found.")


def delete(birthdays: dict) -> None:
    name = input("Enter a name: ")
    if name in birthdays:
        del birthdays[name]
    else:
        print("That name is not found.")


if __name__ == "__main__":
    main()
