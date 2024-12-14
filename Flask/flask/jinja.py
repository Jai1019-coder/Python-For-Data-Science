from flask import Flask,render_template, request, redirect, url_for

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

# @app.route('/submit', methods = ['GET','POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"Hello {name}"
#     return render_template('form.html')
@app.route('/success/<int:score>')
def success(score):
    return "Your Marks is "+str(score)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 40:
        res = 'PASSED'
    else : res = 'FAILED'
    return render_template('result.html',result = res)

@app.route('/successresult/<int:score>')
def successresult(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else : 
        res = "FAILED"
    result = {"marks" : score, "result" : res}
    return render_template('result1.html',result=result)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('resultif.html',score=score)

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successresult',score=total_score))


    ''' +----------------------+
        | User accesses /submit|
        +----------------------+
                |
                v
    +--------------------------+
    | Is request method POST?  |
    +--------------------------+
        /             \
        YES           NO
        |              |
        v              v
+----------------+  +---------------------------+
| Retrieve form  |  | Render getresult.html     |
| data: science, |  | (for GET request)         |
| maths, c, data |  +---------------------------+
+----------------+
        |
        v
+------------------------------+
| Calculate total_score:       |
| (science + maths + c +       |
|  data_science) / 4           |
+------------------------------+
        |
        v
+------------------------------------+
| Redirect to successresult/<score> |
+------------------------------------+
'''
    

if __name__ == '__main__':
    app.run(debug=True)


