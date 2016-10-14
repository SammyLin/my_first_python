from flask import Flask
app = application = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route('/<word>')
def convert_to_uppercase(word):
    return word.upper()


if __name__ == "__main__":
    app.run()
