from flask import Flask
from config import Config
from models import db
from routes import employee_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(employee_bp)

@app.route("/")
def home():
    return {
        "application": "Flask CRUD API",
        "status": "Running"
    }, 200

@app.route("/health")
def health():
    return {
        "status": "UP"
    }, 200