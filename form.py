from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set a secret key for CSRF protection

class AQIForm(FlaskForm):
    PM25 = FloatField('PM2.5', validators=[DataRequired(), NumberRange(min=0)])
    PM10 = FloatField('PM10', validators=[DataRequired(), NumberRange(min=0)])
    NO = FloatField('NO', validators=[DataRequired(), NumberRange(min=0)])
    NO2 = FloatField('NO2', validators=[DataRequired(), NumberRange(min=0)])
    NOx = FloatField('NOx', validators=[DataRequired(), NumberRange(min=0)])
    NH3 = FloatField('NH3', validators=[DataRequired(), NumberRange(min=0)])
    CO = FloatField('CO', validators=[DataRequired(), NumberRange(min=0)])
    SO2 = FloatField('SO2', validators=[DataRequired(), NumberRange(min=0)])
    O3 = FloatField('O3', validators=[DataRequired(), NumberRange(min=0)])
    Benzene = FloatField('Benzene', validators=[DataRequired(), NumberRange(min=0)])
    Toluene = FloatField('Toluene', validators=[DataRequired(), NumberRange(min=0)])
    Xylene = FloatField('Xylene', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('submit')

@app.route('/', methods=["POST"])
def index():
    form = AQIForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.name.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('AQI.html', form=form)


if __name__ == '__main__':
    app.run(debug=True) 