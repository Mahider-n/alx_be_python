def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            itemname = input("Enter item name to be added: ")
            shopping_list.append(itemname)
            pass
        elif choice == '2':
            itemname_todelete = input("Enter item name to be removed: ")
            if itemname_todelete in shopping_list:
                shopping_list.pop(itemname_todelete)
            "The item to be deleted is not found"
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()