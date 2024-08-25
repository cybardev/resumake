# AUTHOR: cybardev
# Docker container for resume generator

# setup Ubuntu LTS environment
FROM ubuntu:22.04
ENV TZ=Etc/GMT
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::BrokenProxy    true;" >> /etc/apt/apt.conf.d/99custom
WORKDIR /app

# install system dependencies
RUN apt-get update
RUN apt-get install -y python3 python3-pip pandoc wkhtmltopdf fonts-roboto
RUN fc-cache -fv

# install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# copy script files to container
COPY resources /app/resources/
COPY resumake.sh /app/
COPY api.py /app/
COPY static/site /app/static/site/

# run resumake server
CMD [ "fastapi", "run", "api.py", "--port", "80" ]
