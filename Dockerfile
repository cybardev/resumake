# AUTHOR: cybardev
# Docker container for resume generator

# Python environment setup
FROM python:3.12-slim AS base
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::http::No-Cache   true;" >> /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::BrokenProxy      true;" >> /etc/apt/apt.conf.d/99custom
WORKDIR /app

# install system dependencies
RUN apt-get update
RUN apt-get install --no-install-recommends -y pandoc wkhtmltopdf fonts-roboto
RUN fc-cache -fv

# create stage to install runner dependencies
FROM base AS pkgs
RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

# install Python dependencies
RUN pip install "poetry==1.8.3"
COPY pyproject.toml poetry.lock ./
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
RUN poetry install --only=main

# create stage to run app in and import dependencies
FROM base AS main
COPY --from=pkgs /app/.venv /app/.venv
ENV PATH=/app/.venv/bin:$PATH

# copy script files to container
COPY resources /app/resources/
COPY resumake.sh /app/
COPY api.py /app/
COPY static/site /app/static/site/

# run resumake server
CMD [ "fastapi", "run", "api.py", "--port", "80" ]
