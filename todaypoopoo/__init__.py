from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config/dev.py')

    # db init

    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    migrate.init_app(app, db)

    # blueprint
    from .views import main_views, auth_views, poopoo_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(poopoo_views.bp)


    # db
    from .models import user_model
    return app
    # app.config.from_envvar('APP_CONFIG_FILE')

