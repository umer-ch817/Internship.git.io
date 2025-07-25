from datetime import datetime, timedelta

books = {}     
borrowed = {}   

def add_book():
    book_id = input("enter book id: ").strip()
    if book_id in books:
        print("book id already exists\n")
        return
    
    title = input("enter book title: ").strip()
    author = input("enter author name: ").strip()
    try:
        quantity = int(input("enter quantity: "))
    except ValueError:
        print("quantity must be a number\n")
        return

    books[book_id] = {
        "title": title,
        "author": author,
        "quantity": quantity,
        "available": quantity
    }
    print("book added successfully\n")

def view_books():
    if not books:
        print("no books available\n")
        return
    print("\navailable books:")
    print(f"{'id':<10}{'title':<30}{'author':<20}{'available':<10}")
    print("-" * 70)
    for book_id, info in books.items():
        print(f"{book_id:<10}{info['title']:<30}{info['author']:<20}{info['available']:<10}")
    print()

def borrow_book():
    book_id = input("enter book id to borrow: ").strip()
    if book_id not in books:
        print("book not found\n")
        return

    if books[book_id]["available"] <= 0:
        print("book not available\n")
        return

    member_name = input("enter your name: ").strip()
    borrow_date = datetime.now()
    due_date = borrow_date + timedelta(days=14)

    borrowed[book_id] = {
        "member": member_name,
        "borrow_date": borrow_date,
        "due_date": due_date
    }

    books[book_id]["available"] -= 1
    print(f"book borrowed due date is {due_date.date()}\n")

def return_book():
    book_id = input("enter book id to return: ").strip()
    if book_id not in borrowed:
        print("this book is not borrowed\n")
        return

    return_date = datetime.now()
    due_date = borrowed[book_id]["due_date"]

    fine = 0
    if return_date > due_date:
        days_late = (return_date - due_date).days
        fine = days_late * 10

    books[book_id]["available"] += 1
    del borrowed[book_id]

    print("book returned")
    if fine > 0:
        print(f"you are {days_late} days late fine: rs. {fine}\n")
    else:
        print("thanks for returning on time\n")

def main():
    while True:
        print("====== library system ======")
        print("1. add book")
        print("2. view books")
        print("3. borrow book")
        print("4. return book")
        print("5. exit")
        choice = input("choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("goodbye")
            break
        else:
            print("invalid choice try again\n")
            
main()
