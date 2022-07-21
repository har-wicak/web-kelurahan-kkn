from flask import Flask, render_template, url_for

app = Flask(__name__)

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