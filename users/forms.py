from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
import re


def password_check(form, field):
    specChars = "!@#$%^&*()-+?_=,<>/"
    if not (re.search("[A-Z]", field.data) and re.search("[a-z]", field.data) and
            re.search("[0-9]", field.data) and any(x in specChars for x in field.data)):
        raise ValidationError("Must contain 1 digit, 1 lowercase, 1 uppercase and 1 special character.")


def number_check(form, field):
    if not re.search("[0-9]{4}-[0-9]{3}-[0-9]{4}", field.data):
        raise ValidationError("Number must be in format XXXX-XXX-XXXX.")


def name_check(form, field):
    specChars = "!@#$%^&*()-+?_=,<>/"
    if any(x in specChars for x in field.data):
        raise ValidationError("Name must not contain special characters.")


class RegisterForm(FlaskForm):
    email = StringField(validators=[DataRequired("Email is required."), Email("Enter valid email format.")])
    firstname = StringField(validators=[DataRequired("Firstname is required."), name_check])
    lastname = StringField(validators=[DataRequired("Lastname is required."), name_check])
    phone = StringField(validators=[DataRequired("Phone is required."), number_check])
    password = PasswordField(
        validators=[DataRequired("Password is required."), Length(6, 12, "Must be between 6 and 12 characters."),
                    password_check])
    confirm_password = PasswordField(
        validators=[DataRequired("Password must match"), EqualTo("password", "Password must match.")])
    pin_key = StringField(validators=[DataRequired("Pin Key must be 32 characters in length"), Length(32, 32)])
    submit = SubmitField()
