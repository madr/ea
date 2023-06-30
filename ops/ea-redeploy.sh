docker pull ghcr.io/madr/ea:main
docker stop ea
docker rm ea
./ea-start.sh
docker exec -it ea ./manage.py migrate