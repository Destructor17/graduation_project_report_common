all: ../config/env.sty ../config/economic_loc.tex ../../_build/EXISTS

../config/env.sty: cfggen.py ../../config.json
	mkdir -p ../config
	python3 cfggen.py

../config/economic_loc.tex: cfggen.py ../../config.json
	mkdir -p ../config
	python3 cfggen.py

../../_build/EXISTS:
	mkdir -p ../../_build
	touch ../../_build/EXISTS
