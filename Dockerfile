# AUTHOR: cybardev
# Docker container for resume generator

# use Ubuntu LTS environment
FROM ubuntu:22.04
ENV TZ=America/Halifax
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install dependencies
RUN apt-get update
RUN apt-get install -y pandoc wkhtmltopdf fonts-roboto
RUN fc-cache -fv

# run resume generator
WORKDIR /resumake
CMD [ "resumake.sh" ]
