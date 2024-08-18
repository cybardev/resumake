# AUTHOR: cybardev
# Docker container for resume generator

# setup Ubuntu LTS environment
FROM ubuntu:22.04
ENV TZ=America/Halifax
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom && \
  echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99custom && \
  echo "Acquire::BrokenProxy    true;" >> /etc/apt/apt.conf.d/99custom

# install dependencies
RUN apt-get update
RUN apt-get install -y pandoc wkhtmltopdf poppler-utils fonts-roboto
RUN fc-cache -fv

# copy script files to container
COPY resources /app/resources/
COPY resumake.sh /app/

# mount input/output directory
VOLUME [ "/app/data" ]
WORKDIR /app

# invoke resume generator script
ENV OUTDIR="data"
ENTRYPOINT [ "bash", "resumake.sh" ]
CMD [ "data/resume.yml" ]
