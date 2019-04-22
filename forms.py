from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField


class ScanForm(FlaskForm):
    radiobuttons = RadioField('Label', choices=[('user', 'Twitter User'), ('query', 'Search Query')], render_kw={"class": "with-gap"})
    inputField = StringField('Username', render_kw={"class": "input-field", "style": "border-bottom: 1px solid royalblue; width: 500px; text-align: center", "placeholder":"Enter a Twitter User's Handle or Search Query"})
    submit = SubmitField('Scan', render_kw={"class": "waves-effect waves-light btn findbtn", "style": "background-color:#42a5f5"})
