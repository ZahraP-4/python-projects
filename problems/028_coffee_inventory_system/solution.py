# Coffee Inventory System (Single File Version)

FILENAME = "coffee.txt"


def add_record():
    another = 'y'
    file = open(FILENAME, 'a')

    while another.lower() == 'y':
        print("\nEnter coffee data:")
        description = input("Description: ")
        quantity = float(input("Quantity (in pounds): "))

        file.write(description + "\n")
        file.write(str(quantity) + "\n")

        another = input("Add another record? (y/n): ")

    file.close()
    print("Record(s) added.")


def show_records():
    try:
        file = open(FILENAME, 'r')
        description = file.readline()

        while description != "":
            quantity = float(file.readline())
            description = description.rstrip('\n')

            print("Description:", description)
            print("Quantity:", quantity)
            print()

            description = file.readline()

        file.close()
    except FileNotFoundError:
        print("No data file found.")


def search_record():
    found = False
    search = input("Enter description to search for: ")

    try:
        file = open(FILENAME, 'r')
        description = file.readline()

        while description != "":
            quantity = float(file.readline())
            description = description.rstrip('\n')

            if description == search:
                print("Description:", description)
                print("Quantity:", quantity)
                found = True

            description = file.readline()

        file.close()

        if not found:
            print("Item not found.")

    except FileNotFoundError:
        print("No data file found.")


def main():
    choice = 0

    while choice != 4:
        print("\nCoffee Inventory Menu")
        print("---------------------")
        print("1. Add Records")
        print("2. Show Records")
        print("3. Search Record")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_record()
        elif choice == 2:
            show_records()
        elif choice == 3:
            search_record()
        elif choice == 4:
            print("Goodbye!")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
