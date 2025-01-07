def manage_inventory():
    """Manages the library book inventory."""

    book_inventory = {
        "The Lord of the Rings": 10,
        "Pride and Prejudice": 5,
        "The Girl with the Dragon Tattoo": 15,
        "The Great Gatsby": 7,
        "Gone Girl": 11,
        "The Woman in Cabin 10": 8
    }

    overdue_fees = {}

    for book_title, days_loaned in book_inventory.items():
        if days_loaned > 14:
            overdue_fees[book_title] = (days_loaned - 14) * 5

    if overdue_fees:
        print("Overdue Books:")
        for book_title, late_fee in overdue_fees.items():
            print(f"{book_title}: Late Fee: {late_fee} taka")
    else:
        print("All books are returned on time.")

    while True:
        choice = input("Enter 'a' to add a book, 'r' to remove a book, or 'q' to quit: ")

        if choice == 'a':
            new_book = input("Enter the title of the book to add: ")
            days_loaned = int(input("Enter the number of days since loaned out: "))
            book_inventory[new_book] = days_loaned
        elif choice == 'r':
            remove_book = input("Enter the title of the book to remove: ")
            if remove_book in book_inventory:
                del book_inventory[remove_book]
            else:
                print("Book not found in inventory.")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please enter 'a', 'r', or 'q'.")


manage_inventory()