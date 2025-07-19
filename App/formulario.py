from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from wtforms import FlaskForm, StringField, SubmitField
from wtforms.validators import DataRequired
from App.models import User, db


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    
    def save_user(self):
        user = User(
            username=self.username.data,
            email=self.email.data,
            password=self.password.data
        )
        db.session.add(user)
        db.session.commit()
        return user