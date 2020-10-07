from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField ,validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Sign Up')
class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remeber me')
	submit=SubmitField('Login')

class ContactForm(Form): 
	name = TextField("Name",  validators=[DataRequired(message="Enter Your Name Please")])
	email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	subject = TextField("Subject",  validators=[DataRequired(message="Enter A subject Please")])
	message = TextAreaField("Message",  validators=[DataRequired(message="Enter A message Please")])
	submit = SubmitField("Send")
