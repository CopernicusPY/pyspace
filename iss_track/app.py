from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def iss_track():
    return render_template('index.html')
app.run(debug=True)
