from flask import Flask, render_template, url_for, redirect
from forms.forms import Questions, QuestionA

app = Flask(__name__)
app.config['SECRET_KEY'] = '453672hhy678'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/questionA", methods=["GET", "POST"])
def questionA():
    form = QuestionA()

    if form.is_submitted():
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        answer5 = form.question5.data
        if answer1 == 'yes' or answer2 == 'yes' or answer3 == 'yes' or answer4 == 'yes':
            if answer5 == 'no':
                return redirect(url_for("question1"))
            else:
                return render_template('index.html')
        else:
            return render_template('index.html')

    else:
        return render_template('sec_definition.html', form=form)


@app.route("/question1", methods=["GET", "POST"])
def question1():
    form = Questions()

    if form.is_submitted():
        answer = form.question2.data
        if answer == "a":
            return redirect(url_for('index'))
        elif answer == "b":
            return redirect(url_for('question1'))

        else:
            return render_template('questions.html', form=form)

    return render_template('questions.html', form=form)


if __name__ == '__main__':
    app.run()
