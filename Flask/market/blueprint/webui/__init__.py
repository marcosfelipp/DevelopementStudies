from flask import Blueprint

from .routes import *

bp = Blueprint("webui", __name__, template_folder="templates")
bp.add_url_rule("/", view_func=home_page)
bp.add_url_rule("/market", view_func=market_page, methods=['GET', 'POST'])
bp.add_url_rule("/register", view_func=register_page, methods=['GET', 'POST'])
bp.add_url_rule("/login", view_func=login_page, methods=['GET', 'POST'])
bp.add_url_rule("/logout", view_func=logout_page)


def init_app(app):
    app.register_blueprint(bp)
