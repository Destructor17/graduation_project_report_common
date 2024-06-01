cd $(dirname $0)/docker

. ../_common.sh

while true
do
    clear
    docker-compose run --rm support_builder sh /build/graduation_project_report_common/docker/_support_build.sh &&\
    docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
    sh _list_watched.sh | inotifywait -e modify,create,delete,move --fromfile -
done
