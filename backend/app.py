from flask import Flask
from flask_cors import CORS
from routes.rsvp    import rsvp_bp
from routes.guests  import guests_bp
from routes.stats   import stats_bp
from models.database import db
import os

app = Flask(__name__)
CORS(app, origins=["https://divi.deehub.dev"])

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY']              = os.environ['SECRET_KEY']

db.init_app(app)

app.register_blueprint(rsvp_bp,    url_prefix='/api')
app.register_blueprint(guests_bp,  url_prefix='/api')
app.register_blueprint(stats_bp,   url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, port=5000)
