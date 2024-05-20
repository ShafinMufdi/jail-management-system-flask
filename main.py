from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/jailmanage'
app.secret_key = 'jail'

from routes.route import register_routes
register_routes(app)

# Initialize SQLAlchemy with the app instance
db.init_app(app)
12
if __name__ == '__main__':
    app.run(debug=True)