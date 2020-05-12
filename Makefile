install:
	poetry install

lint:
	poetry run flake8 gendiff

publish:
	poetry build
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi

selfcheck:
	poetry check

test:
	poetry run pytest gendiff tests

check: selfcheck test lint
	

.PHONY: check install lint publish test selfcheck
