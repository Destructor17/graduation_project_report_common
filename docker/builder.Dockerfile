FROM archlinux:latest

RUN pacman -Sy texlive texlive-langcyrillic texlive-langgreek --noconfirm
COPY fonts /usr/local/share/fonts
RUN texhash
RUN fc-cache -f
