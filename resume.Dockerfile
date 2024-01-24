# syntax=docker/dockerfile:labs

# use preset environment image
FROM cybardev/resume-env

# add git repo and set up directories
ADD --keep-git-dir=true https://github.com/cybardev/resume.git /app
ENV PYTHONPATH $PYTHONPATH:/app/src
VOLUME [ "/app/static" ]

# resume generator with default output directory
ENTRYPOINT [ "python3", "-m", "resume.builder", "-o", "./static/assets" ]
