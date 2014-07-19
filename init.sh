virtualenv .venv

. .venv/bin/activate
pip install -r requirements.txt

pycco server.py -d docs/pycco
