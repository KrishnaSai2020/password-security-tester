import requests
import hashlib
import re
from flask import Flask, render_template, request, redirect
import traceback

app = Flask(__name__)


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check the api and try again ')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5char)
    return get_password_leaks_count(response, tail)


def check_strength(password):
    pattern = re.compile(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!?]).*$")
    return pattern.fullmatch(password)


def main(password):
    count = pwned_api_check(password)
    if count:
        return count


@app.route('/')
def my_home():
    return render_template('home.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            count = main(data['password'])
            return render_template('result.html', data=count)
    except Exception:
        return render_template('home.html')
