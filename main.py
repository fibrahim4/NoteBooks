from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database simulation
books = []

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book.update(request.get_json())
            return jsonify(book)
    return 'Book not found', 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return 'Book deleted', 204
    return 'Book not found', 404

print('Flask app setup with CRUD operations for Book model is complete.')
