from flask import Flask
from flask_cors import CORS
from folder.routes import point

app = Flask(__name__)
CORS(app)

app.register_blueprint(point)