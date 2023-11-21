VENV_PATH=.venv

clean:
	@rm -rf $(VENV_PATH)

install:
	python3 -m venv $(VENV_PATH)
	python3 -m ensurepip --upgrade
	$(VENV_PATH)/bin/pip install matplotlib


test:
	@$(VENV_PATH)/bin/pytest -rP

test-ci:
	@$(VENV_PATH)/bin/pytest -rP
	@$(VENV_PATH)/bin/flake8 src

run:
	@python3 src/main.py

lint:
	@$(VENV_PATH)/bin/flake8 src