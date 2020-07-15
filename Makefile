install:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements.txt

install-dev:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements-dev.txt

proto:
	python -m grpc_tools.protoc --proto_path=src/proto/  --python_out=src/generated/ --grpc_python_out=src/generated/ query_servicer.proto

build:
	proto
	docker-compose up

test:
	pytest -sv tests/

black:
	black --target-version py38 src/ tests/

fix:
	black -l 120 src/ tests/

clean:
	rm -rf dist/ build/  || true

run:
	python main.py

.PHONY: freeze clean
.SILENT: src_package
