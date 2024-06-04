FROM texlive/texlive:latest

COPY fonts /usr/local/share/fonts
RUN texhash
RUN fc-cache -f
RUN apt update && apt install -y librsvg2-bin
