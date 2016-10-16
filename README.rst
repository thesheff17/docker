docker
======

*************
docker images
*************

dev-min: minimum python3 and go dev env

::
    $ mkdir /tmp/git
    $ docker run -it -v /tmp/git:/root/git thesheff17/dev-min

dev: giant dev env

::
    $ mkdir /tmp/git
    $ docker run -it -v /tmp/git:/root/git thesheff17/dev

compile for you own:

::

    $ git clone https://github.com/thesheff17/docker.git
    $ cd docker/dev/
    $ docker build . -t thesheff17/dev:latest
    $ cd ../dev-min
    $ docker build . -t thesheff17/dev-min:latest

dockerPull.sh - used to pull down a list of good docker images
docker_pal.py - wrapper around docker to cleanup during docker builds
clean.sh      - another cleanup script for docker
