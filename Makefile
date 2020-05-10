install:
	poetry install

lint:
	poetry run flake8 gendiff

publish:
	poetry build
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi

.PHONY: install lint publish
