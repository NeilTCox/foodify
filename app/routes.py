from flask import request
from flask import render_template
from app import app
from tinychain import Blockchain
import pickle

blockchain = Blockchain("GENESIS BLOCK")

@app.route('/save')
def save():
    with open('blockchain_chain.txt', 'w') as file:
        file.write(pickle.dumps(blockchain.chain))
    file.close()

    metadata = [blockchain.genesis_block.hash.hexdigest(), blockchain.last_block.hash.hexdigest()]
    with open ('blockchain_meta.txt', 'w') as file:
        file.writelines(metadata)
    file.close()
    

@app.route('/load')
def load():
    with open('blockchain_chain.txt', 'r') as file:
        blockchain.chain = pickle.load(file)
    file.close()

    with open('blockchain_meta.txt', 'r') as file:
        metadata = file.readlines()
    blockchain.genesis_block = blockchain.chain[metadata[0]]
    blockchain.last_block = blockchain.chain[metadata[1]]


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
    if request.method == 'POST':  #this block is only entered when the form is submitted
        foodtype = request.form.get('FoodType')
        certification = request.form.get('Certification')


        foodid = blockchain.add_block((foodtype, certification)).hash

        return render_template('farmer-feedback.html', title='Farmer', user=user, foodid=foodid, foodtype=foodtype, certification=certification)


    return render_template('farmer.html', title='Farmer', user=user)

######################################################################
@app.route('/forms/consumer', methods=['GET', 'POST'])
def consumer():
    user = {'username': 'Nic'}
    if request.method == 'POST':  #this block is only entered when the form is submitted
        foodid = request.form.get('FoodID')

        food = blockchain.explore_block(foodid).data
        foodtype = food[0]
        certification = food[1]

        return render_template('consumer-feedback.html', title='consumer', user=user, foodid=foodid, foodtype=foodtype, certification=certification)


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
