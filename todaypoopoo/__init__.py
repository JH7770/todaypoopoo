from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config/dev.py')
    from .views import main_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)

    return app
    # app.config.from_envvar('APP_CONFIG_FILE')

