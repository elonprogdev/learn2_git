from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    if request.args.get('name'):
        return render_template("index.html", user_name = request.args.get('name'))
    else:
        return render_template("index.html")
        

@app.route("/about")
def about():
    return render_template("about.html")

@app.route ("/input_name", methods=["GET"])
def input_name():
    name = request.args["name"]
    return redirect(url_for('index', name=name))



if __name__ == "__main__":
    app.run(debug=True)

