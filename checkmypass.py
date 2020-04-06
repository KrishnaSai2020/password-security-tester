import requests
import hashlib
import sys
import re
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('home.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form
            return redirect('/result.html')
        except:
            return 'something went wrong not try again'


# def request_api_data(query_char):
#     url = 'https://api.pwnedpasswords.com/range/' + query_char
#     res = requests.get(url)
#     if res.status_code != 200:
#         raise RuntimeError(f'error fetching: {res.status_code}, check the api and try again ')
#     return res
#

# def get_password_leaks_count(hashes, hash_to_check):
#     hashes = (line.split(':') for line in hashes.text.splitlines())
#     for h, count in hashes:
#         if h == hash_to_check:
#             return count
#     return 0
#
#
# def pwned_api_check(password):
#     sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
#     first5char, tail = sha1password[:5], sha1password[5:]
#     response = request_api_data(first5char)
#     return get_password_leaks_count(response, tail)
#
#
# def check_strength(password):
#     pattern = re.compile(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!?]).*$")
#     return pattern.fullmatch(password)
#
#
# def main(args):
#     for password in args:
#         count = pwned_api_check(password)
#         if count:
#             print(f'{password} was found {count} times... you should change it')
#         else:
#             print("your password hasn't been hacked yet")
#             print('lets check its strength..')
#             if check_strength(password) is not None:
#                 print('your password is very strong')
#             else:
#                 print("your password hasn't been hacked yet but you still change it as it is not very strong")
#     return 'done!'
#
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))
