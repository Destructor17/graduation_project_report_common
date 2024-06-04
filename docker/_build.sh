cd $(dirname $0)/../..

make --directory=graduation_project_report_common/docker
ret_code=$?

if test $ret_code -ne 0
then
    rm _build/*.pdf
    rm -r _build/config
    exit $ret_code
fi

export HOME=/data/
latexmk -xelatex -halt-on-error -output-directory=_build -interaction=nonstopmode
ret_code=$?

if test $ret_code -ne 0
then
    # rm _build/*.pdf
    exit $ret_code
fi
