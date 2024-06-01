$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
$root_dir = Split-Path $dir

Function RunMyStuff {
    Clear-Host
    docker-compose run --rm support_builder sh /build/graduation_project_report_common/docker/_support_build.sh 
    docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh
}

Function Watch {    
    $global:FileChanged = $false
    $filters = '*.tex','*.png','config.json'
    $events = 'Changed','Created','Deleted','Renamed'
    foreach ($filter in $filters)
    {
        $watcher = New-Object IO.FileSystemWatcher $root_dir, $filter -Property @{ 
            IncludeSubdirectories = $true 
            EnableRaisingEvents = $true
        }

        foreach ($event in $events) {
            Register-ObjectEvent $watcher $event -Action {$global:FileChanged = $true} > $null
        }
    }

    while ($true){
        while ($global:FileChanged -eq $false){
            Start-Sleep -Milliseconds 100
        }
        RunMyStuff
        $global:FileChanged = $false
    }
}

Push-Location $dir/docker
    docker-compose build
    $Env:MY_UID = "$(id -u)"
    $Env:MY_GID = "$(id -g)"
    RunMyStuff
    Watch
Pop-Location
