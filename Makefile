TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

lint:  ## Check code style
	@echo ${TAG}Check code style${END}
	pipenv run py.test --pep8 practice
	pipenv run py.test --pylint practice
	pipenv run py.test --mypy practice
	@echo

test:  ## Run unittests
	@echo ${TAG}Running unittests${END}
	pipenv run nosetests --cover-branches --with-coverage --cover-erase --cover-package=practice --cover-html --cover-tests
	@echo