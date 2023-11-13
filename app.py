from flask import Flask

app = Flask('app.py')

@app.route('/') 
def hello_world():
    return 'Hello, future Jono. This is my first attempt at an app. I want you to know this will be worth it!'

if 'my app' == '__main__':
    app.run(debug=True)

