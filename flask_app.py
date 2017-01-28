from flask import Flask, request, render_template
from fancifier import synonymreplacer

app = Flask(__name__)

@app.route('/fancifier/')
def fancifier():
    return render_template("fancifier.html")

@app.route('/fancifier/', methods=['POST'])
def fancifier_post():
    text = request.form['input']
    processed_text = synonymreplacer(text)
    return processed_text

if __name__ == "__main__":
    app.run(debug=False)

