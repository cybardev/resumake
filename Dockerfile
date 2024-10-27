# AUTHOR: cybardev
# Docker container for resume generator

# Go environment setup
FROM alpine:3.20 AS base

# install system dependencies
RUN apk add --no-cache weasyprint font-roboto
RUN fc-cache -fv

# copy static files to container
WORKDIR /app
COPY static/site ./static/site/
COPY resources ./resources/

# create build stage
FROM golang:1.23.2-alpine3.20 AS build
WORKDIR /build

# download Go dependencies
COPY go.mod go.sum ./
RUN go mod download

# copy source code
COPY resume.go ./
COPY validators.go ./
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
