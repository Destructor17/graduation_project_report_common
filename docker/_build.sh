cd $(dirname $0)/../..

# export PATH="$(cd /usr/local/texlive/????/bin/*; pwd):$PATH"
export HOME=/data/
latexmk -xelatex -halt-on-error -output-directory=_build -interaction=nonstopmode
ret_code=$?

if test $ret_code -ne 0
then
    # rm _build/*.pdf
    exit $ret_code
fi
