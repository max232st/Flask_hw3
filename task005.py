# Задание №5.
# Создать форму регистрации для пользователя. Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на обработку персональных данных.
# Валидация должна проверять, что все поля заполнены корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.
import secrets

from flask import Flask, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

from forms_5 import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '29748935cb458a359ff3cf7f0eac2956a059e3aa6d2a8e8c04c9ffe9a'
csrf = CSRFProtect(app)
"""
Токен
>>> import secrets
>>> secrets.token_hex()
"""
print(secrets.token_hex)

# Database example to avoid using databases in all of the tasks
EXAMPLE_DB = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    form_notifications = []
    if request.method == 'POST' and form.validate():
        user = form.data.copy()
        if user['name'] not in EXAMPLE_DB:
            EXAMPLE_DB[user['name']] = dict(
                ((key, value) for key, value in user.items() if key != 'name')
            )
        form_notifications.append(
            f'User {user["name"]} successfully registered!'
        )
        return redirect(url_for('main', username=user['name']))
    return render_template(
        'task005.html', form=form, form_notifications=form_notifications
    )


@app.route('/<username>/')
def main(username: str):
    user_data = EXAMPLE_DB.get(username, {})
    return render_template('task005_main.html', username=username, **user_data)


if __name__ == '__main__':
    app.run()
