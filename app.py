from flask import Flask, render_template, url_for, redirect, request
from form.forms import (Sec_def, Form_due_dil, Form_inv, Form_risk_retainer1, Form_risk_retainer2, Form_risk_retainer3,
                        Form_sole_purpose, Form_retention_type, Form_transparency_reporting)

app = Flask(__name__)
app.config['SECRET_KEY'] = '453672hhy678'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/definitions")
def definitions():
    return render_template("definitions.html")


@app.route("/sec_def", methods=["GET", "POST"])
def sec_def():
    form = Sec_def()

    if form.is_submitted():
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        if answer1 == 'yes' or answer2 == 'yes' or answer3 == 'yes':
            if answer4 == 'no':
                return redirect(url_for("due_dil"))
            else:
                return render_template('index.html')
        else:
            return render_template('index.html')
    return render_template('sec_definition.html', form=form)


@app.route("/due_dil", methods=["GET", "POST"])
def due_dil():
    form = Form_due_dil()

    if form.is_submitted():
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        if answer1 == 'yes' and answer3 == 'yes':
            return redirect(url_for("question1"))
        elif answer2 == 'yes' and answer4 == 'yes':
            return redirect(url_for("question1"))
        else:
            return render_template('index.html')
    return render_template('due_dil.html', form=form)


@app.route("/question1", methods=["GET", "POST"])
def question1():
    form = Form_inv()
    heading = """The transaction will constitute a securitisation for the purposes of the EU and UK Regulations. """
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('question1a'))
        elif answer == "b":
            return redirect(url_for('question1b'))
        elif answer == "c":
            return redirect(url_for('question1c'))
        elif answer == "d":
            return redirect(url_for('question1d'))
    return render_template('questions.html', form=form, heading=heading)


@app.route("/question1a", methods=["GET", "POST"])
def question1a():
    form = Form_risk_retainer1()
    heading = """The EU Securitisation Regulation will apply. An entity must act as Risk retainer"""
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('index'))
        elif answer == "b":
            return redirect(url_for('question1'))
        elif answer == "c":
            return redirect(url_for('sole_purpose'))
        elif answer == "d":
            return redirect(url_for('sole_purpose'))
        elif answer == "e":
            return redirect(url_for('sole_purpose'))
        elif answer == "f":
            return redirect(url_for('sole_purpose'))
    return render_template('questions.html', form=form, heading=heading)


@app.route("/question1b", methods=["GET", "POST"])
def question1b():
    form = Form_risk_retainer2()
    heading = """The UK Securitisation Regulation will apply. An entity must act as Risk retainer"""
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('index'))
        elif answer == "b":
            return redirect(url_for('question1'))
        elif answer == "c":
            return redirect(url_for('sole_purpose'))
        elif answer == "d":
            return redirect(url_for('sole_purpose'))
        elif answer == "e":
            return redirect(url_for('sole_purpose'))
        elif answer == "f":
            return redirect(url_for('sole_purpose'))
    return render_template('questions.html', form=form, heading=heading)


@app.route("/question1c", methods=["GET", "POST"])
def question1c():
    form = Form_risk_retainer3()
    heading = """Both the EU Securitisation Regulation and UK Securitisation Regulation will apply. 
    An entity must act as Risk retainer"""
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('index'))
        elif answer == "b":
            return redirect(url_for('question1'))
        elif answer == "c":
            return redirect(url_for('sole_purpose'))
        elif answer == "d":
            return redirect(url_for('sole_purpose'))
        elif answer == "e":
            return redirect(url_for('sole_purpose'))
        elif answer == "f":
            return redirect(url_for('sole_purpose'))
    return render_template('questions.html', form=form, heading=heading)


@app.route("/sole_purpose", methods=["GET", "POST"])
def sole_purpose():
    form = Form_sole_purpose()

    if form.is_submitted():
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        if answer1 == 'yes' and answer2 == 'yes' and answer3 == 'yes' and answer4 == 'yes':
            return redirect(url_for("retention_type"))
        else:
            return render_template('index.html')
    return render_template('sole_purpose.html', form=form)


@app.route("/retention_type", methods=["GET", "POST"])
def retention_type():
    form = Form_retention_type()
    heading = """Retention type"""
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('transparency_reporting'))
        elif answer == "b":
            return redirect(url_for('transparency_reporting'))
        elif answer == "c":
            return redirect(url_for('transparency_reporting'))
        elif answer == "d":
            return redirect(url_for('transparency_reporting'))
        elif answer == "e":
            return redirect(url_for('transparency_reporting'))
    return render_template('questions.html', form=form, heading=heading)


@app.route("/transparency_reporting", methods=["GET", "POST"])
def transparency_reporting():
    form = Form_transparency_reporting()

    if form.is_submitted():
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        if answer1 == 'yes' and answer2 == 'yes' and answer3 == 'yes' and answer4 == 'yes':
            return redirect(url_for("index"))
        else:
            return render_template('index.html')
    return render_template('transparency_reporting.html', form=form)


if __name__ == '__main__':
    app.run()
