from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my simple web service!'

@app.route('/endpoint1')
def endpoint1():
    return 'Hello, this is first endpoint'

@app.route('/endpoint2')
def endpoint2():
    return 'bye, this is last endpoint'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


