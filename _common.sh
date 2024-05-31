export MY_UID="$(id -u)" 
export MY_GID="$(id -g)"

docker-compose build || exit 1
