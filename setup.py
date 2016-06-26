from setuptools import setup, find_packages

def parse_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name = 'pwsadmin',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = parse_requirements(),
    author = 'Kyle Stevenson',
    author_email = 'kyle@kylestevenson.me',
    description = 'A simple JSON API wrapper around the Pro Wager Systems backoffice software.',
    keywords = 'pro wager systems',
    license = 'MIT',
    url = 'https://github.com/kylestev/pwsadmin'
)
