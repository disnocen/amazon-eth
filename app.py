# import flask
from flask import Flask, request, jsonify, render_template, redirect, url_for
import csv
import requests
import web3

# convert ethereum to amount for transaction
def ethereum_to_wei(amount):
    return str(hex(int(amount * 10 ** 18)))

# read the data from the book_data.csv file. return a dictionary with isbn,
# title, author and price.
def read_data():
    with open('book_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        bookdata = [row for row in reader]
    return bookdata
# [{'isbn': '9789029510424', 'title': 'Un Gentiluomo a Mosca', 'author': 'Amor Towles', 'price': '1.5'}, {'isbn': '9788854524699', 'title': "Le vie dell'Eden", 'author': 'Eshkol Nevo', 'price': '1'}]

# return link of front cover of isbn from google books
def get_cover(isbn):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn
    response = requests.get(url)
    data = response.json()
    if data['totalItems'] == 0:
        return None
    else:
        return data['items'][0]['volumeInfo']['imageLinks']['thumbnail']

#initialize flask app
app = Flask(__name__)


#index page
@app.route('/')
def index():
    return render_template('index.html')

# booklist page
@app.route('/booklist')
def booklist():
    title = "Book List"
    bookdata = read_data()
    return render_template('booklist.html', title=title, bookdata=bookdata)


# bookdetail page
@app.route('/bookinfo/<isbn>')
def bookdetail(isbn):
    title = "Book Detail"
    bookdata = read_data()
    for book in bookdata:
        if book['isbn'] == isbn:
            # get front cover of isbn from google books
            front_cover = get_cover(isbn)
            price_hex = ethereum_to_wei(float(book['price']))
            return render_template('bookdetail.html', front_cover =
                                   front_cover, price_hex = price_hex, author=book['author'], title=book['title'], price=book['price'])
    return render_template('bookdetail.html', title="Not found", author="Not found", price="Not found")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
