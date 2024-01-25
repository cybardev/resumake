# AUTHOR: cybardev
# Docker container for resume generator

# use Ubuntu LTS environment
FROM ubuntu:22.04

# install dependencies
RUN apt-get update
RUN apt install -y python3 python3-pip pandoc wkhtmltopdf poppler-utils

# install resume generator from PyPI
RUN python3 -m pip install resumake

# mount input/output directory
VOLUME [ "/app/resume" ]
WORKDIR /app/resume

# resume generator with default output directory
ENTRYPOINT [ "python3", "-m", "resumake.builder", "-o", "/app/resume" ]
