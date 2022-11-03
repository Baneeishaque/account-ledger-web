release: python manage.py migrate && python manage.py loaddata TLogin.yaml
web: gunicorn account_ledger_web.wsgi --log-file -
