# flask-shell-ipython

Replace default `flask shell` command by similar command running IPython.

## Usage

Just install:

    pip install flask-shell-ipython

And here are you go:

    > flask shell
    Python 3.5.1 (default, Mar  3 2016, 09:29:07)
    [GCC 5.3.0] on linux
    IPython: 5.0.0
    App: discharges [debug]
    Instance: /home/ei-grad/repos/discharges/instance

   
   
   #Flask Cheat Sheet and Quick Reference
   #Barebones App
from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
 return 'Hello, World!'
if __name__ == '__main__':
 app.run(debug=True)
#Flask Cheat Sheet and Quick Reference
#Routing
@app.route('/hello/<string:name>') # example.com/hello/Anthony
def hello(name):
 return 'Hello ' + name + '!' # returns hello Anthony!
#Allowed Request Methods
@app.route('/test') #default. only allows GET requests
@app.route('/test', methods=['GET', 'POST']) #allows only GET and POST.
@app.route('/test', methods=['PUT']) #allows only PUT
#Configuration
#direct access to config
app.config['CONFIG_NAME'] = 'config value'
#import from an exported environment variable with a path to a config file
app.config.from_envvar('ENV_VAR_NAME')
#Templates
from flask import render_template
@app.route('/')
def index():
 return render_template('template_file.html', var1=value1, ...)
#JSON Responses
import jsonify
@app.route('/returnstuff')
def returnstuff():
 num_list = [1,2,3,4,5]
 num_dict = {'numbers' : num_list, 'name' : 'Numbers'}
 #returns {'output' : {'numbers' : [1,2,3,4,5], 'name' : 'Numbers'}}
 return jsonify({'output' : num_dict})
#Access Request Data
request.args['name'] #query string arguments
request.form['name'] #form data
request.method #request type
request.cookies.get('cookie_name') #cookies
request.files['name'] #files
#Redirect
from flask import url_for, redirect
@app.route('/home')
def home():
 return render_template('home.html')
@app.route('/redirect')
def redirect_example():
 return redirect(url_for('index')) #sends user to /home
#Abort
from flask import abort()
@app.route('/')
def index():
 abort(404) #returns 404 error
 render_template('index.html') #this never gets executed
#Set Cookie
from flask import make_response
@app.route('/')
def index():
 resp = make_response(render_template('index.html'))
 resp.set_cookie('cookie_name', 'cookie_value')
 return resp
#Session Handling
import session
app.config['SECRET_KEY'] = 'any random string' #must be set to use sessions
#set session
@app.route('/login_success')
def login_success():
 session['key_name'] = 'key_value' #stores a secure cookie in browser
 return redirect(url_for('index'))
#read session
@app.route('/')
def index():
 if 'key_name' in session: #session exists and has key
