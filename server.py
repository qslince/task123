from flask import Flask
from flask_login import LoginManager
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init("db/mars_explorer.db")


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


if __name__ == '__main__':
    main()
