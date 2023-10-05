from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {"PNG", "JPG", "png", "jpg"}


class DestinationForm(FlaskForm):
    name = StringField("Country", validators=[InputRequired()])
    # adding two validators, one to ensure input is entered and other to check if the
    # description meets the length requirements
    description = TextAreaField("Description", validators=[InputRequired()])
    image = FileField(
        "Destination Image",
        validators=[
            FileRequired(message="Image cannot be empty"),
            FileAllowed(ALLOWED_FILE, message="Only PNG or JPG files allowed"),
        ],
    )
    currency = StringField("Currency", validators=[InputRequired()])
    submit = SubmitField("Create")


# VERY MINIMAL VALIDATION BELOW, NEED MORE FOR ASSIGNMENT
class CommentForm(FlaskForm):
    text = TextAreaField("Comment", [InputRequired()])
    submit = SubmitField("Create")


class LoginForm(FlaskForm):
    user_name = StringField(
        "Username", validators=[InputRequired("Please enter your username")]
    )
    password = PasswordField(
        "Password", validators=[InputRequired("Please enter your password")]
    )
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired()])
    email_id = StringField(
        "Email Address",
        validators=[InputRequired(), Email("Please enter a valid email address")],
    )
    password = PasswordField(
        "Password", validators=[InputRequired("Please enter your password")]
    )
    confirm = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired("Please re-enter your password"),
            EqualTo("password", message="Password must match"),
        ],
    )
    submit = SubmitField("Register")
