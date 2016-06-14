docker
======

*************
docker images
*************

dev-min: minimum python3 and go dev env

::

    $ docker run -it --entrypoint /bin/bash thesheff17/dev-min

dev: giant dev env

::

    $ docker run -it --entrypoint /bin/bash thesheff17/dev

compile for you own:

::

    $ git clone https://github.com/thesheff17/docker.git
    $ cd docker/dev/
    $ docker build -t thesheff17/dev:latest .
    $ cd ../dev-min
    $ docker build -t thesheff17/dev-min:latest .
    $ docker run -d --name dev-min thesheff17/dev-min
    $ docker run -d --name dev thesheff17/dev

dockerPull.sh - used to pull down a list of good docker images
