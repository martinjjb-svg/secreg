from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired


class Sec_def(FlaskForm):
    question1 = RadioField("""question_1""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question2 = RadioField("""question_2""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question3 = RadioField("""question_3""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question4 = RadioField("""question_4""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_due_dil(FlaskForm):
    question1 = RadioField("""question_1""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question2 = RadioField("""question_2""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question3 = RadioField("""question_3""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question4 = RadioField("""question_4""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_inv(FlaskForm):
    question = SelectField("Choose which applies",
                           choices=[('a', '(a) investors are based in the EU'),
                                    ('b', '(b) investors are based in the UK'),
                                    ('c', '(c) investors may be in the UK or the EU'),
                                    ('d', '(d) investors not in the UK or the EU')], validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_risk_retainer1(FlaskForm):
    question = SelectField("Choose which applies",
                           choices=[('a', '(a) sponsor'),
                                    ('b', '(b) original lender'),
                                    ('c', '(c) limb(a) originator'),
                                    ('d', '(d) limb(b) originator'),
                                    ('e', '(e) multi-originator 3(4)(a)'),
                                    ('f', '(f) multi-originator 3(4)(b)')], validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_risk_retainer2(FlaskForm):
    question = SelectField("Choose which applies",
                           choices=[('a', '(a) sponsor'),
                                    ('b', '(b) original lender'),
                                    ('c', '(c) limb(a) originator'),
                                    ('d', '(d) limb(b) originator'),
                                    ('e', '(e) multi-originator 3(4)(a)'),
                                    ('f', '(f) multi-originator 3(4)(b)')], validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_risk_retainer3(FlaskForm):
    question = SelectField("Choose which applies",
                           choices=[('a', '(a) sponsor'),
                                    ('b', '(b) original lender'),
                                    ('c', '(c) limb(a) originator'),
                                    ('d', '(d) limb(b) originator'),
                                    ('e', '(e) multi-originator 3(4)(a)'),
                                    ('f', '(f) multi-originator 3(4)(b)')], validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_sole_purpose(FlaskForm):
    question1 = RadioField("""question_1""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question2 = RadioField("""question_2""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question3 = RadioField("""question_3""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question4 = RadioField("""question_4""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_retention_type(FlaskForm):
    question = SelectField("Choose which applies",
                           choices=[('a', '(a) 5% of nominal value of each tranche sold'),
                                    ('b', '(b) Revolving - 5% of nominal value of each of the securitised exposures'),
                                    ('c', '(c) Random selection - 5% of nominal value of the securitised exposures'),
                                    ('d', '(d) First loss tranche or tranches with same of more severe risk profile of at least 5%'),
                                    ('e', '(e) First loss exposure of not less than 5% of every securitised exposure ')], validators=[DataRequired()])
    submit = SubmitField('submit')


class Form_transparency_reporting(FlaskForm):
    question1 = RadioField("""question_1""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question2 = RadioField("""question_2""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question3 = RadioField("""question_3""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    question4 = RadioField("""question_4""",
                           choices=[('yes', 'yes'), ('no', 'no')],
                           validators=[DataRequired()])
    submit = SubmitField('submit')
