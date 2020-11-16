from flask import Flask, render_template

app = Flask(__name__, template_folder='webPages')
app.secret_key = "personalFinances"
app.debug = True

allMethods = ['GET', 'POST']

#View for the landing page
@app.route("/", methods = allMethods)
def landingPage():
    return render_template("index.html")
