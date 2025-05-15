# main.py

from flask import Flask
from app.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=5000)