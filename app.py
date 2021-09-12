from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = "46E665878F1FD315FE6C39B3C2119640"

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)