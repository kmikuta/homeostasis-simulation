VENV_PATH=.venv

install:
	python3 -m venv $(VENV_PATH)
	python3 -m ensurepip --upgrade
	$(VENV_PATH)/bin/pip install -r requirements.txt

test:
	@$(VENV_PATH)/bin/pytest -rP

lint:
	@$(VENV_PATH)/bin/flake8 src

run:
	@python3 src/main.py

clean:
	@rm -rf $(VENV_PATH)
	@rm -rf .pytest_cache