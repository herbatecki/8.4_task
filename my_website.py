from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/mypage/me')
def presenting():
    return render_template('me.html')

@app.route('/mypage/contact', methods= ['GET', 'POST'])
def contacting():
    return render_template('contact.html')
def forming():
    print('receiving POST')
    print(request.form)
    return redirect('/')

@app.route('/message', methods=['POST'])
def post_message():
    return "OK posting"