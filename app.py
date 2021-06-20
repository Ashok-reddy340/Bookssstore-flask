#from flask import Flask,redirect,url_for
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/books')
def books():
    books=['Book1','Book2','Book3']
    return render_template('books.html',books=books)

# @app.route('/admin')
# def welcome_admin():
#     return 'welcome admin'
# @app.route('/guest/<guest>')
# def welcome_guest(guest):
#     return 'welocome guest %s' % guest
# @app.route('/user/<name>')
# def welcome_user(name):
#     if name == 'admin':
#         return redirect(url_for('welcome_admin')) 
#     else:
#         return redirect(url_for('welcome_guest',guest=name))



         
    
    

app.run(debug=True)    

