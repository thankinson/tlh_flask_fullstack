from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, SelectField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo

class NewUser(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired(), Length(min=5)])
    user_email = EmailField('User Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm password')