from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
    # app.config.from_envvar('APP_CONFIG_FILE')

