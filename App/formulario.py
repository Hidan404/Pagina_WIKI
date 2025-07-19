from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import FlaskForm, StringField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
