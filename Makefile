CODE = pychardet tests
PYTHON = poetry run

.PHONY: pretty lint test

pretty:
	$(PYTHON) isort --apply --recursive $(CODE)
	$(PYTHON) unify --in-place --recursive $(CODE)

lint:
	$(PYTHON) flake8 --jobs 4 --statistics $(CODE)

test:
	$(PYTHON) pytest -n auto --boxed tests

coverage:
	$(PYTHON) pytest --cov=pychardet
	$(PYTHON) codecov
