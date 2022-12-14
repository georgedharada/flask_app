from flask import Flask, redirect, url_for #comment
app = Flask(__name__) #create instance of webapp

@app.route("/") # give it a root so know where to find the app
def home():  #define pages that will be on website
    return "Hello! This is the main page <h1>HELLO<h1>"  #return what will be displayed on page

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
        return redirect(url_for("home"))

if __name__ == "__main__":  #run the app
    app.run()

