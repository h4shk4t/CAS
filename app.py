# Basic Flask app
from flask import Flask, request, render_template
import requests
import casparser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/fetch_cas', methods=['GET', 'POST'])
def fetch_cas():
    url = "https://kfintech-cas-mailback-automation.p.rapidapi.com/request_ecas"
    email = request.form['email']
    pan_no = request.form['pan_no']
    from_date = request.form['from_date']
    to_date = request.form['to_date']
    password = request.form['password']
    payload = {
        "email": email,
        "pan_no": pan_no,
        "from_date": from_date,
        "to_date": to_date,
        "password": password
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "eb8b8c3737msh83982885850bb0ap1569c6jsn5bc1266dfe30",
        "X-RapidAPI-Host": "kfintech-cas-mailback-automation.p.rapidapi.com"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.text
    except:
        return "Error"

@app.route('/parse_cas', methods=['GET', 'POST'])
def parse_cas():
    cas_file = request.files['cas_file']
    password = request.form['password']
    cas_file.save("cas.pdf")
    cas_data = casparser.read_cas_pdf("cas.pdf", password)
    return cas_data

if __name__ == '__main__':
    app.run(debug=True)
