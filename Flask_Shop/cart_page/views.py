import flask
import flask_login
import registration_page
import registration_page.models
from shop.settings import DATABASE
from .models import Cart
def show_cart_page():
    if flask.request.method == "POST":
        cart = Cart(
            name = flask.request.form['name'],
            surname = flask.request.form['surname'],
            phone = flask.request.form['phone'],
            email = flask.request.form['email'],
            city = flask.request.form['city'],
            nova_poshta = flask.request.form['mail'],
            wishes = flask.request.form['wishes']
        )

        DATABASE.session.add(cart)
        DATABASE.session.commit()
    user = registration_page.models.User.query.all()
    for users in user:
            flask_login.login_user(users)
    if not flask_login.current_user.is_authenticated:
        return flask.render_template(template_name_or_list="cart.html")
    else:
        if flask_login.current_user.is_authenticated:
            name = True
            name2 = users.login
            is_admin = flask_login.current_user.is_admin
            return flask.render_template(template_name_or_list="cart.html", name = name, name2 = name2, is_admin = is_admin)