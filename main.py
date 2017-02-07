from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/mictionary/add/<type>/<int:amount>')
def add(type, amount):

    print('type: ' + type + ', amount ' + str(amount))

    return 'success'

if __name__ == '__main__':
    app.run(debug=True)