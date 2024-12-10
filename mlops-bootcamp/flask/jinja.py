### Building URL Dynamically
## Variable Rule
### Jinja2 Template Engine

### Jinja2 Template Engine
'''
{{ }} - expressions to print output in html
{% %} - conditions and loops
{# #} - comments    
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome'

@app.route('/index', methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>= 50:
        res='pass'
    else:  
        res='fail'
    return render_template('result.html', results=res)

# Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>= 50:
        res='pass'
    else:  
        res='fail'

    exp={'score':score, 'res':res}
    return render_template('result1.html', results=exp)

if __name__ == '__main__':
    app.run(debug=True)