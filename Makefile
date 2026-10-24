PY ?= python3

.PHONY: check validate build sqlite find hooks

check: validate
	$(PY) scripts/build.py --check

validate:
	$(PY) scripts/validate.py

build:
	$(PY) scripts/build.py

sqlite:
	$(PY) scripts/build.py --sqlite

hooks:
	git config core.hooksPath .githooks
