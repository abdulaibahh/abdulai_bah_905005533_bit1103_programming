books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Education", "History")


def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return "Book added successfully."


def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            return "Member already exists."
    new_member = {
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    }
    members.append(new_member)
    return "Member added successfully."


def search_books(keyword):
    results = []
    for isbn, details in books.items():
        if keyword.lower() in details["title"].lower() or keyword.lower() in details["author"].lower():
            results.append({isbn: details})
    return results if results else "No books found."


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found."
    if genre and genre not in genres:
        return "Invalid genre."
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies:
        diff = total_copies - books[isbn]["total_copies"]
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available_copies"] += diff
    return "Book updated successfully."


def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available_copies"] != books[isbn]["total_copies"]:
        return "Cannot delete book. Some copies are borrowed."
    del books[isbn]
    return "Book deleted successfully."


def borrow_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found."
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available_copies"] == 0:
        return "No copies left."
    if len(member["borrowed_books"]) >= 3:
        return "Borrow limit reached."
    member["borrowed_books"].append(isbn)
    books[isbn]["available_copies"] -= 1
    return "Book borrowed successfully."


def return_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found."
    if isbn not in member["borrowed_books"]:
        return "Book not borrowed by this member."
    member["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    return "Book returned successfully."


def delete_member(member_id):
    global members
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found."
    if len(member["borrowed_books"]) > 0:
        return "Cannot delete member with borrowed books."
    members = [m for m in members if m["member_id"] != member_id]
    return "Member deleted successfully."
