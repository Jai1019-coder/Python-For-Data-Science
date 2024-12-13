from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1/>Govind Jaiswal Welcomes you to his place"
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)