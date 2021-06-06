from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Name here and name in the arguement need to be the same
@app.route('/home/<int:id>')
def hello(id):
    # This is how you get data from the URL 
    return "Hello, " + str(id)   

# Allows your request methods so you can't get the page is post is required
@app.route('/onlyget', methods=['POST', 'GET'])
def get_req():
    return 'you can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)