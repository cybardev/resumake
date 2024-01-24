# AUTHOR: cybardev
# Prepare environment for resume generator

# use Ubuntu LTS environment
FROM ubuntu:22.04
WORKDIR /app
ENV TZ=America/Halifax
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install dependencies
RUN apt-get update
RUN apt install -y git python3 pandoc wkhtmltopdf poppler-utils
