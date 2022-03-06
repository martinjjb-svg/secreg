from flask import Flask, render_template, url_for, redirect, request
from form.forms import (Sec_def, Form_risk_retainer1, Form_risk_retainer2, Form_risk_retainer3,
                        Form_sole_purpose, Form_retention_type, Form_transparency_reporting, Form_jurisdiction)

app = Flask(__name__)
app.config['SECRET_KEY'] = '453672hhy678'



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/definitions")
def definitions():
    return render_template("definitions.html")


@app.route("/end")
def end():
    return render_template("end.html")


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
                return redirect(url_for("jurisdiction"))
            else:
                return render_template('end.html')
        else:
            return render_template('end.html')
    return render_template('sec_definition.html', form=form)


@app.route("/jurisdiction", methods=["GET", "POST"])
def jurisdiction():
    form = Form_jurisdiction()

    if form.is_submitted():
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        if answer1 == 'yes' and answer2 == 'no' and answer4 == 'no':
            return redirect(url_for("question1a"))
        elif answer2 == 'yes' and answer1 == 'no' and answer3 == 'no':
            return redirect(url_for("question1b"))
        elif answer1 == 'yes' and answer2 == 'yes':
            return redirect(url_for("question1c"))
        elif answer1 == 'yes' and answer4 == 'yes':
            return redirect(url_for("question1c"))
        elif answer2 == 'yes' and answer3 == 'yes':
            return redirect(url_for("question1c"))
        elif answer1 == 'no' and answer2 == 'no' and answer3 == 'no' and answer4 == 'no':
            return render_template('end.html')

        else:
            return render_template('not_compliant.html')
    return render_template('jurisdiction.html', form=form)


@app.route("/question1a", methods=["GET", "POST"])
def question1a():
    form = Form_risk_retainer1()
    heading = """As a relevant entity is established in the EU the EU Securitisation Regulation will apply. 
    This requires that the transaction complies with specific due diligence, risk retention and transparency and 
    reporting requirements. """
    heading2 = """An entity or entities that satisfy one of the following types must hold and continue to hold for the
    life of the transaction a net material economic interest of not less than 5% in the transaction, calculated in 
    accordance with the EU Regulation, and held in one of the forms specified by the EU Regulation
    (the 'Risk Retainer')."""
    heading3 = """The retention must not be split amongst different types of retainers but can be met by:
    Article 3(4)(a) multiple originators / multiple original lenders pro rata to the exposures for which it was
    originator/original lender; Article 3(4)(b) by a single originator or original lender provided that: 
    (i) it has established and is managing the ABCP programme or other securitisation; or (ii) it has established the
    ABCP programme or other securitisation and has contributed more than 50 % of the total securitised exposures
    (by nominal value at origination)"""
    heading4 = """In relation to sponsors it may also be the sponsor whose economic interest is most appropriately
    aligned with investors as agreed by the multiple sponsors on objective criteria including the fee structures, the
    involvement in the establishment and management of the ABCP programme or other securitisation and exposure to credit
    risk of the securitisation or multiple sponsors proportionately to the number of sponsors."""
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('retention_type'))
        elif answer == "b":
            return redirect(url_for('retention_type'))
        elif answer == "c":
            return redirect(url_for('sole_purpose'))
        elif answer == "d":
            return redirect(url_for('sole_purpose'))
        elif answer == "e":
            return redirect(url_for('sole_purpose'))
        elif answer == "f":
            return redirect(url_for('sole_purpose'))
    return render_template('questions.html', form=form, heading=heading, heading2=heading2, heading3=heading3, heading4=heading4)


@app.route("/question1b", methods=["GET", "POST"])
def question1b():
    form = Form_risk_retainer2()
    heading = """As a relevant entity is established in the UK the UK Securitisation Regulation will apply. 
    This requires that the transaction complies with specific due diligence, risk retention and transparency and 
    reporting requirements. """
    heading2 = """An entity or entities that satisfy one of the following types must hold and continue to hold for the
    life of the transaction a net material economic interest of not less than 5% in the transaction, calculated in 
    accordance with the UK Regulation, and held in one of the forms specified by the UK Regulation 
    (the 'Risk Retainer')."""
    heading3 = """The retention must not be split amongst different types of retainers but can be met by:
    Article 3(4)(a) multiple originators / multiple original lenders pro rata to the exposures for which it was
    originator/original lender; Article 3(4)(b) by a single originator or original lender provided that: (i) it has
    established and is managing the ABCP programme or other securitisation; or (ii) it has established the ABCP
    programme or other securitisation and has contributed more than 50 % of the total securitised exposures (by nominal
    value at origination)"""
    heading4 = """In relation to sponsors it may also be the sponsor whose economic interest is most appropriately
    aligned with investors as agreed by the multiple sponsors on objective criteria including the fee structures, the
    involvement in the establishment and management of the ABCP programme or other securitisation and exposure to credit
    risk of the securitisation or multiple sponsors proportionately to the number of sponsors."""
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('retention_type'))
        elif answer == "b":
            return redirect(url_for('retention_type'))
        elif answer == "c":
            return redirect(url_for('sole_purpose'))
        elif answer == "d":
            return redirect(url_for('sole_purpose'))
        elif answer == "e":
            return redirect(url_for('sole_purpose'))
        elif answer == "f":
            return redirect(url_for('sole_purpose'))
    return render_template('questions.html', form=form, heading=heading, heading2=heading2, heading3=heading3, heading4=heading4)


@app.route("/question1c", methods=["GET", "POST"])
def question1c():
    form = Form_risk_retainer3()
    heading = """As relevant entities are established in the EU and the UK the EU and UK Securitisation Regulations will
     apply. This requires that the transaction complies with specific due diligence, risk retention and transparency and 
    reporting requirements. """
    heading2 = """An entity or entities that satisfy one of the following types must hold and continue to hold for the
    life of the transaction a net material economic interest of not less than 5% in the transaction, calculated in 
    accordance with the EU and UK Regulations, and held in one of the forms specified by the Regulations (the 'Risk
    Retainer')."""
    heading3 = """The retention must not be split amongst different types of retainers but can be met by:
    Article 3(4)(a) multiple originators / multiple original lenders pro rata to the exposures for which it was
    originator/original lender; Article 3(4)(b) by a single originator or original lender provided that: (i) it has
    established and is managing the ABCP programme or other securitisation; or (ii) it has established the ABCP
    programme or other securitisation and has contributed more than 50 % of the total securitised exposures (by nominal
    value at origination)"""
    heading4 = """In relation to sponsors it may also be the sponsor whose economic interest is most appropriately 
    aligned with investors as agreed by the multiple sponsors on objective criteria including the fee structures, the
    involvement in the establishment and management of the ABCP programme or other securitisation and exposure to credit 
    risk of the securitisation or multiple sponsors proportionately to the number of sponsors."""
    if form.is_submitted():
        answer = form.question.data
        if answer == "a":
            return redirect(url_for('retention_type'))
        elif answer == "b":
            return redirect(url_for('retention_type'))
        elif answer == "c":
            return redirect(url_for('sole_purpose'))
        elif answer == "d":
            return redirect(url_for('sole_purpose'))
        elif answer == "e":
            return redirect(url_for('sole_purpose'))
        elif answer == "f":
            return redirect(url_for('sole_purpose'))
    return render_template('questions.html', form=form, heading=heading, heading2=heading2, heading3=heading3, heading4=heading4)


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
            return render_template('not_compliant.html')
    return render_template('sole_purpose.html', form=form)


@app.route("/retention_type", methods=["GET", "POST"])
def retention_type():
    form = Form_retention_type()
    heading = """"""
    heading2 = """The Risk Retainer must retain on an ongoing basis a material net economic interest in the 
    securitisation of not less than 5%, measured at the origination and determined by the notional value for
    off-balance-sheet items. Where the originator, sponsor or original lender have not agreed between them who will
    retain the material net economic interest, the originator shall retain the material net economic interest. 
    The material net economic interest shall not be subject to any credit-risk mitigation or hedging."""
    heading3 = """Originators shall not select assets to be transferred to the SSPE with the aim of rendering losses on
    the assets transferred to the SSPE, measured over the life of the transaction, or over a maximum of 4 years where
    the life of the transaction is longer than four years, higher than the losses over the same period on comparable
    assets held on the balance sheet of the originator. Where the competent authority finds evidence suggesting
    contravention of that prohibition, the competent authority shall investigate the performance of assets
    transferred to the SSPE and comparable assets held on the balance sheet of the originator. If the performance
    of the transferred assets is significantly lower than that of the comparable assets held on the balance sheet
    of the originator as a consequence of the intent of the originator, the competent authority shall impose a
    sanction [EU version: pursuant to Articles 32 and 33] [UK version: for the contravention]."""

    heading4 = """"""
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
    return render_template('questions.html', form=form, heading=heading, heading2=heading2, heading3=heading3, heading4=heading4)


@app.route("/transparency_reporting", methods=["GET", "POST"])
def transparency_reporting():
    form = Form_transparency_reporting()

    if form.is_submitted():
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        answer5 = form.question4.data
        if answer1 == 'yes' and answer2 == 'yes' and answer3 == 'yes' and answer4 == 'yes' and answer5 == 'yes':
            return redirect(url_for("compliance"))
        else:
            return render_template('not_compliant.html')
    return render_template('transparency_reporting.html', form=form)


@app.route("/compliance")
def compliance():
    return render_template("compliance.html")


@app.route("/not_compliant")
def not_compliant():
    return render_template("not_compliant.html")

if __name__ == '__main__':
    app.run()
