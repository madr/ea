## Deployment

This Docker image is built, pushed and published automatically on Github Packages, using Github actions. **Only on main branch**.

### Start in prod

Start new one by:

    ./ea-start.sh

Fetch and update existing by:

    ./ea-redeploy.sh

### Backups

A crontab is making backup of the database every 30th minute.

## Local development

Initial setup, using `virtualenv`, only needed once:

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt

Initial django setup, only needed once:

    cd src
    mkdir data
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

Local dev is now available at http://localhost:8000, and the admin
interface is available at http://localhost:8000/admin/.