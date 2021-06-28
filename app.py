#from flask import Flask,redirect,url_for
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import os
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file="sqlite:///{}".format(os.path.join(project_dir,"mydatabse.db"))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=database_file
db = SQLAlchemy(app)
 
class Book(db.Model):

        name = db.Column(db.String(100), unique = True, nullable = False ,primary_key = True)
        author = db.Column(db.String(100),nullable = False) 

@app.route('/updatebooks')
def updatebooks():

        books = Book.query.all()
        return render_template('updatebooks.html',books = books) 
  
@app.route('/update',methods=['POST'])
def update():
        newname = request.form['newname']
        oldname = request.form['oldname']
        newauthor = request.form['newauthor']
        book = Book.query.filter_by(name=oldname).first()
        book.name = newname
        book.author = newauthor
        db.session.commit()
        return redirect('/books')
@app.route('/delete',methods=['POST'])
def delete():

        name = request.form['name']
        book = Book.query.filter_by(name=name).first()
        db.session.delete(book)
        db.session.commit()
        return redirect('/books')



@app.route('/addbook')
def addbook():

        return render_template('addbook.html')

@app.route('/submitbook',methods=['POST'])
def submitbook():

        name = request.form['name']
        author = request.form['author']
        book = Book(name=name, author=author)
        db.session.add(book)
        db.session.commit()
        return redirect('/books')    
  #      return 'data submit Book name is %s and author is %s' % (name, author)

@app.route('/books')
def books():
        books=Book.query.all()
#    books =[{'name':'Book1','author':'Author','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-1-CRC.png'},
#            {'name':'Book2','author':'Author1','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-1-CRC.png'},
#            {'name':'Book3','author':'Author2','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-1-CRC.png'}]
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



         
    
    
    
if __name__ == "__main__":
        app.run(debug=True)
   

