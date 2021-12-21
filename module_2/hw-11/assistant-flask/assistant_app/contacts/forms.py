from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Enter name', validators=[DataRequired(), Length(min=2, max=140)])
    phone = IntegerField('Enter phone', validators=[DataRequired()])
    address = TextAreaField('Enter address', validators=[DataRequired(), Length(min=2, max=140)])
    email = StringField('Enter email', validators=[DataRequired(), Email(), Length(min=2, max=140)])
    submit = SubmitField('Submit')
