from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="Halaman Index",isi="Selamat Datang di web saya")
@app.route('/about')
def about():
    return render_template('about.html',title="Halaman About",isi="BIODATA SAYA")
@app.route('/myproject')
def myproject():
    return render_template('myproject.html',title="My Project")
if __name__=="__main__":
    app.run(debug=True)
 