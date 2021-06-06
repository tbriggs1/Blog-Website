from flask import Flask

app = Flask(__name__)

# Name here and name in the arguement need to be the same
@app.route('/home/<int:id>')
def hello(id):
    # This is how you get data from the URL 
    return "Hello, " + str(id)

if __name__ == "__main__":
    app.run(debug=True)