# syntax=docker/dockerfile:labs

# use preset environment image
FROM cybardev/resumake-env:main

# add git repo and set up directories
ADD --keep-git-dir=true https://github.com/cybardev/resume.git /app
ENV PYTHONPATH $PYTHONPATH:/app/src
VOLUME [ "/app/resume" ]
WORKDIR /app/resume

# resume generator with default output directory
ENTRYPOINT [ "python3", "-m", "resumake.builder", "-o", "/app/resume" ]
