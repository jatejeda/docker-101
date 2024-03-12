# Dockerize a simple Python script with third-party modules

We differ between:

- Dockerfile: Blueprint for building images
- Image: Template for running containers
- Container: Running process with the packaged project

## 1. Build the Docker image

```console
$ docker build -t python-spotify . 
```

## 2. Run the Docker image (starts the container)

Without user input:

```console
$ docker run python-spotify
```

If you want to access the container:

```console
$ docker run -it python-spotify /bin/bash
```

-i: interactive, -t: pseudo terminal