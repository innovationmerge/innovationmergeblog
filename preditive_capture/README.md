## readme of the preditive-capture

Author : innovationmerge
Version: 1.0
Descritption: Auto capture of photos when object detected

#### Requirements: 
- Python > 3.7
- `pip install cookiecutter`
- `pip install poetry`

#### Run the project using poetry
- `poetry install`
- `poetry run python main.py`

#### Add project dependencies using poetry 
- `poetry add package_name`

#### List project dependencies using poetry 
- `poetry show --tree`

#### Check latest version of a project dependencies using poetry 
- `poetry show --latest`

#### Update project dependencies using poetry 
- `poetry update`

#### Check project virtual environment path using poetry 
- `poetry env info --path`

#### Test the project using poetry and Pytest
- `poetry run pytest`

#### Check code coverageusing poetry and Pytest
- `poetry run pytest --cov-report html a_b --cov=a_b --cov-branch`

#### Auto fix Linting issues of the project using poetry and black
- `black <folder>`

#### Check Linting of the project using poetry and flake8
- `poetry run flake8`

#### Test the code with multiple python versions and linting problems using poetry and tox
- `poetry run tox`

#### Build the project using poetry
-  `poetry build`

#### Code Security check
-  `poetry run bandir -r .`

#### Generate exe file
-  `poetry run pyinstaller main.py`