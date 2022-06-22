"""Forms for playlist app."""

from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    """Form for login in app."""

    email = StringField("Email", validators=[InputRequired(), Length(max=50), Email()])
    password = StringField("Password", validators=[Length(max=50), InputRequired()])


class Signupform(FlaskForm):
    """Form for adding songs."""

    username = StringField("User name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = StringField(
        "Password",
        validators=[
            InputRequired(),
            EqualTo("confirmPassword", message="Passwords must match"),
        ],
    )
    confirmPassword = StringField("confirmPassword", validators=[InputRequired()])
