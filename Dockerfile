# AUTHOR: cybardev
# Docker container for resume generator

# setup Ubuntu LTS environment
FROM ubuntu:22.04
ENV TZ=America/Halifax
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::http::No-Cache true;" >> /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::BrokenProxy    true;" >> /etc/apt/apt.conf.d/99custom

# install dependencies
RUN apt-get update
RUN apt-get install -y pandoc wkhtmltopdf poppler-utils fonts-roboto
RUN fc-cache -fv

# copy script files to container
COPY resources /app/resources/
COPY resumake.sh /app/

# configure directories
VOLUME [ "/app/data" ]
WORKDIR /app
ENV INDIR="data"
ENV OUTDIR="data"
ENV TMPDIR="/app/resources"

# invoke resume generator script
ENTRYPOINT [ "bash", "resumake.sh" ]
CMD [ "resume.yml" ]
