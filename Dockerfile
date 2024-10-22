# AUTHOR: cybardev
# Docker container for resume generator

# Go environment setup
FROM golang:1.23.2-bookworm AS base
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::http::No-Cache   true;" >> /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::BrokenProxy      true;" >> /etc/apt/apt.conf.d/99custom
WORKDIR /app

# install system dependencies
RUN apt-get update
RUN apt-get install --no-install-recommends -y pandoc wkhtmltopdf fonts-roboto
RUN fc-cache -fv

# create build stage
FROM base AS build

# download Go dependencies
COPY go.mod go.sum ./
RUN go mod download

# copy source code
COPY resumake.go ./

# build executable
ENV CGO_ENABLED=0
ENV GOOS=linux
RUN go build -o resumake

# create runtime stage
FROM base AS main
COPY --from=build /app/resumake /app/resumake

# copy static files to container
COPY static/site /app/static/site/
COPY resources /app/resources/

# run resumake server
EXPOSE 80
CMD [ "./resumake" ]
