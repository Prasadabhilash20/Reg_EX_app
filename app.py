from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/results', methods=['POST'])
# def results():
#     test_string = request.form['test_string']
#     regex = request.form['regex']
#     matches = re.findall(regex, test_string)
#     return render_template('index.html', test_string=test_string, regex=regex, matches=matches)

@app.route('/results', methods=['POST'])
def results():
    try:
        test_string = request.form['test_string']
        regex = request.form['regex']  # Access the submitted regex pattern
        matches = re.findall(regex, test_string)
        return render_template('index.html', test_string=test_string, regex=regex, matches=matches)
    except KeyError:
        # Handle case where 'regex' key is missing in form data
        error_message = "Please enter a regular expression pattern."
        return render_template('index.html', error_message=error_message)


@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    if re.match(email_regex, email):
        validation_message = "Valid email address!"
    else:
        validation_message = "Invalid email address."
    return render_template('index.html', validation_message=validation_message)

if __name__ == '__main__':
    app.run(debug=True)
