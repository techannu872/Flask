from flask import Flask

app = Flask(__name__)

@app.route("/")  #'/' this implies for creating the home page
def home_page():
    return "<h1>Welcome to HomePage</h1>"

@app.route("/addition/<int:num1>/<int:num2>")
def addition(num1, num2):
    return f"<h1>The sum of {num1} and {num2} is {num1 + num2}</h1>"

if __name__ == "__main__":
    app.run(debug = True)