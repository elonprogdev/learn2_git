from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    if request.args.get('name') and request.args.get('age'):
        return render_template("index.html", user_name = request.args.get('name'), user_age = "("+ request.args.get('age') + ")")
    else:
        return render_template("index.html")
        

@app.route("/about")
def about():
    return render_template("about.html")

@app.route ("/input_data", methods=["GET"])
def input_data():
    name = request.args["name"]
    age = request.args["age"]
    return redirect(url_for('index', name=name, age=age))



if __name__ == "__main__":
    app.run(debug=True)

