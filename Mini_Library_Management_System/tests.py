from operations import *

# Reset data before testing
books.clear()
members.clear()

print("\n===== Running Library System Tests =====\n")

# 1. Test adding a book
result = add_book("B200", "Clean Code", "Robert Martin", "Education", 4)
assert result == "Book added successfully.", "Test 1 Failed: add_book"

# 2. Test adding a member
result = add_member("M200", "John Doe", "john@example.com")
assert result == "Member added successfully.", "Test 2 Failed: add_member"

# 3. Test borrowing a book
result = borrow_book("M200", "B200")
assert result == "Book borrowed successfully.", "Test 3 Failed: borrow_book"

# 4. Test returning a book
result = return_book("M200", "B200")
assert result == "Book returned successfully.", "Test 4 Failed: return_book"

# 5. Test deleting a book only when all copies are available
result = delete_book("B200")
assert result == "Book deleted successfully.", "Test 5 Failed: delete_book"

print("All tests passed successfully!\n")
