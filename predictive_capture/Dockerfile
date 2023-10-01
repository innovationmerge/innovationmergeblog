FROM python:3.9.2

RUN pip install poetry

WORKDIR /code

COPY pyproject.toml /code/

RUN poetry install
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY preditive-capture/ /code/preditive-capture

CMD ["poetry", "run", "python", "main.py"s]