# import flask
from flask import Flask, request, jsonify, render_template, redirect, url_for
import csv

# read the data from the book_data.csv file. return a dictionary with isbn,
# title, author and price.
def read_data():
    with open('book_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        bookdata = [row for row in reader]
    return bookdata


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



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
