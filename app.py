from flask import Flask,render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/linkedin')
def linkedin():
    return redirect("https://www.linkedin.com/in/harsh-raut-626312288/")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'form submitted'

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
import os
import csv


def write_to_csv(data):
    file_exists = os.path.isfile('database.csv')

    with open('database.csv', mode='a', newline='') as database2:
        # Extracting the data from the dictionary
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        subject = data.get('subject')
        message = data.get('message')
        project = data.get('project')

        # CSV writer initialization
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write the header if the file does not exist or is empty
        if not file_exists or os.stat('database.csv').st_size == 0:
            csv_writer.writerow(['Name', 'Email', 'Phone', 'Subject', 'Message', 'Project'])

        # Write the row of data
        csv_writer.writerow([name, email, phone, subject, message, project])


if __name__ == '__main__':
    app.run(debug=True)