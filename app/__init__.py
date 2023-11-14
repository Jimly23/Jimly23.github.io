from flask import Flask

def create_app():
    app = Flask(__name__)

    # Konfigurasi aplikasi
    app.config['SECRET_KEY'] = 'Hardiansyah_23'

    # Daftar rute atau blueprint
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
