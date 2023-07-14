from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<div style="height: calc(100vh - 16px); display: flex; align-items: center; justify-content: center; flex-direction: column; background-color: #000619; color: #c9c9c9;">' \
            '<h1>Hello! This is a test Python / Flask application!</h1>' \
            '<h2>Feel free to do nothing at all!</h2>' \
            '<h3>(Because this application does nothing at all)</h3>' \
           '</div>'


if __name__ == '__main__':
    app.run()
