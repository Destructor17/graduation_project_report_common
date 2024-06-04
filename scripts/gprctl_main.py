def run():
    import os
    import argparse

    parser = argparse.ArgumentParser(
        prog="gprctl",
        description="Утилита для написания ПЗ к диплому",
    )
    parser.add_argument("action", choices=["build", "watch"])
    args = parser.parse_args()

    gpr_common_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    repo_path = os.path.dirname(gpr_common_path)
    assert os.path.basename(gpr_common_path) == "graduation_project_report_common"
    docker_dir_path = os.path.join(gpr_common_path, "docker")

    def build():
        os.chdir(docker_dir_path)
        os.system("docker-compose build")
        os.system(
            "docker-compose run --rm builder sh /build/graduation_project_report_common/docker/_build.sh"
        )

    def setup_environ():
        os.environ["MY_UID"] = str(os.getuid())
        os.environ["MY_GID"] = str(os.getgid())

    action = args.action
    if action == "build":
        setup_environ()
        build()
