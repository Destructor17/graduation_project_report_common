cd $(dirname $0)/docker

set -ex

. ../_common.sh

docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
