# pwsadmin
A simple JSON API wrapper around the Pro Wager Systems backoffice software.

Please note that the flask HTTP server found in `api.py` should not be exposed
to the Internet on any public interface. There is virtually no security
provided by this package and should not be used in a production environment.
You have been warned.

## Development

1. `git clone https://github.com/kylestev/pwsadmin`
2. `virtualenv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `cp .env.example .env`
6. `vi .env # edit according to your environment`
7. `python pwsadmin/api.py`
8. `curl http://localhost:5000/api/rooms`
