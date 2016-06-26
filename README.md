# pwsadmin
A simple Python wrapper around the Pro Wager Systems backoffice software.

## Running the Example API

Please note that the flask HTTP server found in `api.py` should not be exposed
to the Internet on any public interface. There is virtually no security
provided by this package and should not be used in a production environment.
You have been warned.

1. `git clone https://github.com/kylestev/pwsadmin`
2. `cd examples`
3. `virtualenv .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`
6. `cp .env.example .env`
7. `vi .env # edit according to your environment`
8. `python api.py`
9. `curl http://localhost:5000/api/rooms`

## Development

1. `git clone https://github.com/kylestev/pwsadmin`
2. `virtualenv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`

Your environment is now configured for running this package!
