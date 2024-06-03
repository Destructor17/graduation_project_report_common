FROM mirisbowring/texlive_ctan_full:2019

COPY builder_patch /
RUN texhash
