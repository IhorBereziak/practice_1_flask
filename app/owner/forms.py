from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length, NumberRange

class RegisterOwner(Form):
    name = StringField('Name', [DataRequired(), length(2, 25, 'name must be 2-25 characters')])
    age = IntegerField('Age', [NumberRange(), length(10, 100, 'age must be 10-100 characters')])
    city = StringField('City', [DataRequired(), length(3, 20, 'city must be 3-20 characters')])
    save = SubmitField('Save')

class RegisterPet(Form):
    name = StringField('Name', [DataRequired(), length(2, 25, 'name must be 2-25 characters')])
    age = IntegerField('Age', [NumberRange(), length(1, 25, 'age must be 1-25 characters')])
    animal_type = StringField('Animal Type', [DataRequired(), length(2, 20, 'animal type must be 2-20 characters')])
    save = SubmitField('Save')