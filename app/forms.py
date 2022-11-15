from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import Email, DataRequired


class Contact(FlaskForm):
    username = StringField("name", validators=[DataRequired()], render_kw={"placholder": "Name"})
    email = EmailField("email", validators=[DataRequired(), Email()], render_kw={"placholder": "Email"})
    location = StringField("Location", render_kw={"plachuolder": "Location"})
    budget = StringField("Budget", validators=[DataRequired()], render_kw={"placholder": "Budget"})
    subject = StringField("Subject", validators=[DataRequired()], render_kw={"placholder": "Subject"})
    message = StringField("message", validators=[DataRequired()], render_kw={"placholder": "Message"})
    