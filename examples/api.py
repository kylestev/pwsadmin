from pwsadmin.backoffice import PWSAdmin

from dotenv import load_dotenv, find_dotenv
from os.path import dirname, join
from flask import Flask, jsonify
import os

load_dotenv(find_dotenv())


def create_pws():
    return PWSAdmin(os.environ.get('PWS_ADMIN_URL'),
                    os.environ.get('PWS_ADMIN_USER'),
                    os.environ.get('PWS_ADMIN_PASS'))

PWS = create_pws()
PWS.login()

app = Flask('pwsadmin')

@app.route('/api/rooms')
def rooms():
    global PWS
    return jsonify(PWS.rooms())

if __name__ == '__main__':
    print 'This Flask server is for DEVELOPMENT environments ONLY.'
    print 'It runs with debug mode enable which allows for code execution.'
    print 'This SHOULD NOT be run in a production environment.'

    answer = raw_input('Do you wish to continue? (y/N) ').strip()
    if answer and answer.lower()[0] == 'y':
        app.run(debug=True)
