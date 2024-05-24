FROM ubuntu:24.04

# Notes:
#    I assume this docker image is for dev work.
#    I do not care about the docker image size or build time.
#    The key is to abstract this out to a quicker docker image pull.

# call build.sh to debug more with BUILDKIT_PROGRESS param
# ./build.sh  

# docker build . -t thesheff17/dev:latest

RUN echo `date` > /root/build_date.txt

RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    build-essential \
    curl \
    git \
    htop \
    libbz2-dev \
    libgraphviz-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libpq-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    llvm \
    make \
    man \
    postgresql-client \
    postgresql-client-common \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    software-properties-common \
    sudo \
    tk-dev \
    tk-dev \
    tmux \
    vim \
    wget \
    xz-utils \
    zlib1g-dev \
    && \
    apt-get autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# pyenv
RUN curl https://pyenv.run | bash

# python versions compiled from source
RUN PYTHON_CONFIGURE_OPTS="-enable-optimizations --with-lto --enable-shared" /root/.pyenv/bin/pyenv install 3.10.14
RUN PYTHON_CONFIGURE_OPTS="-enable-optimizations --with-lto --enable-shared" /root/.pyenv/bin/pyenv install 3.11.4
RUN PYTHON_CONFIGURE_OPTS="-enable-optimizations --with-lto --enable-shared" /root/.pyenv/bin/pyenv install 3.12.3

RUN yes | unminimize

# ppa versions
RUN add-apt-repository ppa:deadsnakes/ppa --yes
RUN apt-get update && \
    apt-get install -y python3.10 python3.10-dev python3.10-venv python3.11 python3.11-dev python3.11-venv

# PIP STUFF
COPY requirements.txt /root/requirements.txt

RUN \
    mkdir /root/.venv/

# ppa 3.10
RUN \
  /usr/bin/python3.10 -m venv /root/.venv/python3.10-ppa && \
  /bin/bash -c "source /root/.venv/python3.10-ppa/bin/activate && \
  pip install --upgrade pip && \
  pip3 install -r /root/requirements.txt"

# ppa 3.11
RUN \
  /usr/bin/python3.11 -m venv /root/.venv/python3.11-ppa && \
  /bin/bash -c "source /root/.venv/python3.11-ppa/bin/activate && \
  pip install --upgrade pip && \
  pip3 install -r /root/requirements.txt"

# apt-get 3.12
RUN \
  /usr/bin/python3.12 -m venv /root/.venv/python3.12-apt && \
  /bin/bash -c "source /root/.venv/python3.12-apt/bin/activate && \
  pip install --upgrade pip && \
  pip3 install -r /root/requirements.txt"

# compile from source 3.10
RUN \
  /root/.pyenv/versions/3.10.14/bin/python3 -m venv /root/.venv/python3.10-source && \
  /bin/bash -c "source /root/.venv/python3.10-source/bin/activate && \
  pip install --upgrade pip && \
  pip3 install -r /root/requirements.txt"

# compile from source 3.11
RUN \
  /root/.pyenv/versions/3.11.4/bin/python3 -m venv /root/.venv/python3.11-source && \
  /bin/bash -c "source /root/.venv/python3.11-source/bin/activate && \
  pip install --upgrade pip && \
  pip3 install -r /root/requirements.txt"

# compile from source 3.12
RUN \
  /root/.pyenv/versions/3.12.3/bin/python3 -m venv /root/.venv/python3.12-source && \
  /bin/bash -c "source /root/.venv/python3.12-source/bin/activate && \
  pip install --upgrade pip && \
  pip3 install -r /root/requirements.txt"

CMD ["/bin/bash"]