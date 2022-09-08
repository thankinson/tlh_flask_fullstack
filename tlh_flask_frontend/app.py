from flask import Flask, render_template
from application.crateuser import NewUser

# application 
app = Flask(__name__)
app.config['SECRET_KEY']='bew_ldJsjOWMQvGqF50ebw'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    new_user = NewUser()
    return render_template('login.html', form=new_user)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)