cd $(dirname $0)/docker

set -ex

. ../_common.sh

docker-compose run --rm support_builder sh /build/graduation_project_report_common/docker/_support_build.sh 
docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
