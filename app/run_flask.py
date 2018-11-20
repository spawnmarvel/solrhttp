from flask import Flask, render_template, request
import run_get
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = ""
    req = "GET"
    if request.method == "POST":
        req = "POST"
        if request.form["action"] == "GetDefault":
            try:
                data = run_get.get_docs_default()
            except Exception as e:
                data = ["error", str(e)]
    #GET
    return render_template("index.html", data=data, req=req)


if __name__ == "__main__":
    app.run(debug=True)