from operations import *

print("\n===== Mini Library Management System Demo =====\n")

# Add books
print(add_book("B101", "Python Programming", "John Smith", "Education", 5))
print(add_book("B102", "Data Structures", "Alice Doe", "Education", 3))
print(add_book("B103", "The Galaxy", "Mark Star", "Sci-Fi", 2))

# Add members
print(add_member("M001", "Abdulai Bah", "abdulai@gmail.com"))
print(add_member("M002", "Zainab Kamara", "zainab@gmail.com"))

# Search for a book
print("\nSearch result for 'Python':")
print(search_books("Python"))

# Borrow books
print("\nBorrowing books...")
print(borrow_book("M001", "B101"))
print(borrow_book("M002", "B103"))

# Try borrowing again when no copies left
print(borrow_book("M002", "B103"))

# Return book
print("\nReturning books...")
print(return_book("M002", "B103"))

# Update a book
print("\nUpdating book details...")
print(update_book("B101", total_copies=7))

# Delete a book (only if all copies are available)
print("\nDeleting a book...")
print(delete_book("B102"))

# Delete a member (only if no borrowed books)
print("\nDeleting a member...")
print(delete_member("M001"))

print("\n===== Demo Completed Successfully =====")
