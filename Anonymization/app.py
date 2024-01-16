# Step 1: Install necessary packages
# Run the following commands in your terminal:
# pip install Flask pandas faker flask-wtf tqdm

# Step 2: Create the main application file (app.py)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from faker import Faker
import pandas as pd
from tqdm import tqdm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'  # Create a folder named 'uploads' in the same directory as this script

class AnonymizeForm(FlaskForm):
    fake_fields = [('None', 'None'), ('first_name', 'First Name'), ('last_name', 'Last Name'), ('email', 'Email')]
    submit = SubmitField('Anonymize')

def anonymize_data(input_file, selected_columns):
    fake = Faker()
    df = pd.read_csv(input_file)

    for column, fake_field in selected_columns.items():
        if fake_field != 'None':
            df[column] = df[column].apply(lambda x: getattr(fake, fake_field)() if pd.notnull(x) else x)

    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AnonymizeForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            input_file = request.files['file']
            selected_columns = request.form.getlist('columns')

            if not input_file or not input_file.filename.endswith('.csv'):
                flash('Please provide a valid CSV file.')
                return redirect(url_for('index'))

            filename = secure_filename(input_file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            input_file.save(input_path)

            columns = pd.read_csv(input_path, nrows=0).columns.tolist()
            choices = [(col, col) for col in columns]
            setattr(form, 'columns', SelectField('Select Column', choices=choices, validators=[DataRequired()]))

            df = anonymize_data(input_path, dict(zip(selected_columns, form.fake_fields.data)))

            output_filename = f'anonymized_{filename}'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            df.to_csv(output_path, index=False)

            flash('Data anonymized successfully!')
            return redirect(url_for('index'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
