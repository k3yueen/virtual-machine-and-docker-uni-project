import os
from flask import Flask, render_template
 
app = Flask(__name__)
color = os.environ.get('MY_COLOR', 'white')  # Default to white if no color is set
 
@app.route("/")
def index():
    return render_template("index.html",
                           mytitle="MyPage",
                           mycontent="Welcome to my custom page",
                           mycolor=color)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
