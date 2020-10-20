# Dockerizing Django with Postgres, Gunicorn, and Nginx

## Read the following article for instructions on how to build this.

Check out the [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).

## To build this project follow the instructions bellow for development or production release.

### Development

Uses the default Django development server.

1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
2. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
