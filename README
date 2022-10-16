## Deployment

This Docker image is built, pushed and published automatically on Github Packages, using Github actions. **Only on main branch**.

### Start in prod

First: pull latest container

    docker pull ghcr.io/madr/ea:main

Stop the running container:

    docker stop ea
    docker rm ea

Start new one by:

    ./ea-start.sh

## Backups

A crontab is making backup of the database every 30th minute.
