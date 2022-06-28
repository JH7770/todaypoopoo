from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('../config/dev.py')
    app.config.from_envvar('APP_CONFIG_FILE')
    # db init

    db.init_app(app)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
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

