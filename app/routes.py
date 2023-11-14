from flask import request, render_template
from flask import Blueprint
# from app import model
from .model import DatabaseManager

main_routes = Blueprint('main',__name__)

@main_routes.route('/')
def awal():
    return render_template('index.html')

# FREE QUOTE
@main_routes.route('/quote', methods=['GET','POST'])
def free_quote():
    if request.method == 'POST':
        web = request.form['web']
        email = request.form['email']

        DatabaseManager().freeQuote(email,web)
        return '<p>Berhasil Terkirim</p>'

# SEND MESSAGE
@main_routes.route('/message', methods=['post'])
def message():
    username = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    DatabaseManager().sendMessage(username,email,subject,message)
    return {'msg':'berhasil'}, 201

