from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Kontak(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nama = db.Column(db.String(50), nullable = False)
#     email = db.Column(db.String(50), nullable = False)
#     text = db.Column(db.String(1000), nullable = False)



@app.route('/')
def index():
    return render_template('index.html', page_title = "Web Kelurahan KKN")

@app.route('/pemerintahan')
def pemerintahan():
    return render_template('pemerintahan.html', page_title = "Laman Pemerintahan Desa")

@app.route('/profil')
def profil():
    return render_template('profil.html', page_title = "Profil Desa")

@app.route('/kontak')
def kontak():
    return render_template('kontak.html', page_title = "Kontak Kami")

if __name__ == "__main__":
    app.run(debug=True)