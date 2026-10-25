PY ?= python3
TMP ?= /tmp/simgrammar-determinism

.PHONY: check validate build sqlite find hooks determinism sources calibrate-sheet

check: validate
	$(PY) scripts/build.py --check

validate:
	$(PY) scripts/validate.py

build:
	$(PY) scripts/build.py

sqlite:
	$(PY) scripts/build.py --sqlite

# I11: two builds under different hash seeds must be byte-identical (CI runs this on every push)
determinism:
	rm -rf $(TMP) && mkdir -p $(TMP)
	PYTHONHASHSEED=1 $(PY) scripts/build.py --out $(TMP)/a
	PYTHONHASHSEED=2 $(PY) scripts/build.py --out $(TMP)/b
	diff -r $(TMP)/a $(TMP)/b && echo "determinism OK"

# network: fetch cited sources and check claim quotes and store ids (not part of the build)
sources:
	$(PY) scripts/check_sources.py

calibrate-sheet:
	$(PY) scripts/calibrate.py sheet

hooks:
	git config core.hooksPath .githooks
