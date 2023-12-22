import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.db import close_db

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "database.db"
    )
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.teardown_appcontext(close_db)

    db.init_app(app)
    from routes import main  # Importing the routes from the routes folder

    app.register_blueprint(main)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
