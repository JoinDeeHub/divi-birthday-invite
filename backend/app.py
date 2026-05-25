from flask import Flask
from flask_cors import CORS
from routes.rsvp import rsvp_bp
from routes.guests import guests_bp
from routes.stats import stats_bp
from models.database import db
import os

app = Flask(__name__)

CORS(app, origins=[
    "https://divi-doll-birthday.netlify.app",
    "http://localhost:3000"
])

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(rsvp_bp, url_prefix="/api")
app.register_blueprint(guests_bp, url_prefix="/api")
app.register_blueprint(stats_bp, url_prefix="/api")

@app.route("/")
def health():
    return {"status": "ok", "service": "divi-birthday-invite-api"}, 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False, port=5000)
