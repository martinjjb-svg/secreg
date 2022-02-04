from flask import Flask, render_template, url_for, redirect
from form.forms import Questions

app = Flask(__name__)
app.config['SECRET_KEY'] = '453672hhy678'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


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
