# AUTHOR: cybardev
# Docker container for resume generator

# Go environment setup
FROM debian:bookworm-slim AS base
RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::http::No-Cache   true;" >> /etc/apt/apt.conf.d/99custom
RUN echo "Acquire::BrokenProxy      true;" >> /etc/apt/apt.conf.d/99custom

# install system dependencies
RUN apt-get update
RUN apt-get install --no-install-recommends -y pandoc wkhtmltopdf fonts-roboto
RUN fc-cache -fv

# copy static files to container
WORKDIR /app
COPY static/site ./static/site/
COPY resources ./resources/

# create build stage
FROM golang:1.23.2-bookworm AS build
WORKDIR /build

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
COPY --from=build /build/resumake /app/resumake

# run resumake server
EXPOSE 80
CMD [ "./resumake" ]
