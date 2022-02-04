from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class Questions(FlaskForm):
    question2 = SelectField("level_1_question_1",
                            choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], validators=[DataRequired()])
    submit = SubmitField('submit')


class QuestionA(FlaskForm):
    question1 = RadioField("""level_4_question_1""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question2 = RadioField("""level_4_question_2""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question3 = RadioField("""level_4_question_3""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question4 = RadioField("""level_4_question_4""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question5 = RadioField("""level_4_question_5""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    submit = SubmitField('submit')
