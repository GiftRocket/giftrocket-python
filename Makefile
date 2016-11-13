.PHONY: lint
lint:
	flake8 giftrocket


.PHONY: test
test: lint
	py.test --cov giftrocket -s -rxs ./tests/


.PHONY: setup
setup:
	pip install -r requirements.txt
