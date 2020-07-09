install:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements.txt

install-dev:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements-dev.txt

build:
	docker-compose up

test:
	pytest -sv tests/

black:
	black --target-version py38 src/ tests/

fix:
	black -l 120 src/ tests/

clean:
	rm -rf dist/ build/  || true

.PHONY: freeze clean
.SILENT: src_package
