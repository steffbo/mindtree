from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Franzi'


if __name__ == '__main__':
    app.run()
