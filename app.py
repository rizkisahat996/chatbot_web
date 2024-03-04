from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "tes dulu bro"

if __name__ == '__main__':
    app.run()