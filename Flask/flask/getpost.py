from flask import Flask,render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1/>Govind Jaiswal Welcomes you to his place"
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f"Welcome {name}"
    else:
        return render_template('form.html')

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)