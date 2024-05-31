all: ../../_build/disk.png ../../_build/config/env.sty ../../_build/config/economic_loc.tex

../../_build/disk.png: ../images/disk.svg ../../config.json disk_svg_processor.py
	mkdir -p ../../_build
	python3 disk_svg_processor.py ../images/disk.svg ../../config.json | rsvg-convert -o ../../_build/disk.png -w 1024 -h 1024

../../_build/EXISTS:
	mkdir -p ../../_build
	touch ../../_build/EXISTS

../../_build/config/env.sty: cfggen.py ../../config.json
	mkdir -p ../../_build/config
	python3 cfggen.py

../../_build/config/economic_loc.tex: cfggen.py ../../config.json
	mkdir -p ../../_build/config
	python3 cfggen.py
