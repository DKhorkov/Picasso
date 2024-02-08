# Picasso API

"Picasso API" - Django REST API that allows users
to upload files to server (<b><i>domain/upload/</i></b> url), 
where files will be processed asynchronously using Celery, 
and get list of all files (<b><i>domain/files/</i></b> url), 
uploaded to server.

Technical specifications, on basis of which application 
was developed, are located in
<b><i>technical_specifications.pdf</i></b> file.

### Run via docker:

To run application via docker, use next command line in 
project's root directory:

    make -C docker clean && make -C docker build && make -C docker run


### Run using source files:

To run application using source files, use next command 
line in project's root directory:

    bash startup.sh
