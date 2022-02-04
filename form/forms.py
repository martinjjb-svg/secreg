from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class Questions(FlaskForm):
    question2 = SelectField("level_1_question_1",
                            choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], validators=[DataRequired()])
    submit = SubmitField('submit')