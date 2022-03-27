from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def iss_track():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404
# @app.errorhandler(500)
# def page_not_found(e):
#     return render_template("errors/500.html"), 500
app.run(debug=True)
