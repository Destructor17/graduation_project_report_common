$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Push-Location $dir/docker
    $Env:MY_UID = "$(id -u)" 
    $Env:MY_GID = "$(id -g)"
    docker-compose build
    docker-compose run --rm support_builder sh /build/graduation_project_report_common/docker/_support_build.sh 
    docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
Pop-Location
