from flask import request
from flask import render_template
from app import app

dict = {}

@app.route('/save')
def save():
    return function()

@app.route('/load')
def load():
    return function()




@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nic'}
    return render_template('index.html', title='Home', user=user)

@app.route('/forms/')
def forms():
    user = {'username': 'Nic'}
    return render_template('forms.html', title='Forms', user=user)


######################################################################
@app.route('/forms/farmer', methods=['GET', 'POST'])
def farmer():
    user = {'username': 'Nic'}
    #print("Fuck")
    if request.method == 'POST':  #this block is only entered when the form is submitted
        #print("Shit")
        foodid = request.form.get('FoodID')
        certification = request.form.get('Certification')
        #print("Bitch")

        dict[foodid] = certification
        print(dict)

        return render_template('farmer-feedback.html', title='Farmer', user=user, foodid=foodid, certification=certification)


    return render_template('farmer.html', title='Farmer', user=user)

######################################################################
@app.route('/forms/consumer', methods=['GET', 'POST'])
def consumer():
    user = {'username': 'Nic'}
    #print("Fuck")
    if request.method == 'POST':  #this block is only entered when the form is submitted
        #print("Shit")
        foodid = request.form.get('FoodID')
        #print("Bitch")

        print(dict)
        certification = dict[foodid]

        return render_template('consumer-feedback.html', title='consumer', user=user, foodid=foodid, certification=certification)


    return render_template('consumer.html', title='Consumer', user=user)


######################################################################
@app.route('/about')
def about():
    user = {'username': 'Nic'}
    return render_template('about.html', title='About', user=user)


# @app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
# def form_example():
#     if request.method == 'POST':  #this block is only entered when the form is submitted
#         language = request.form.get('language')
#         framework = request.form['framework']
#
#         return '''<h1>The language value is: {}</h1>
#                   <h1>The framework value is: {}</h1>'''.format(language, framework)
#
#     return '''<form method="POST">
#                   Language: <input type="text" name="language"><br>
#                   Framework: <input type="text" name="framework"><br>
#                   <input type="submit" value="Submit"><br>
#               </form>'''
