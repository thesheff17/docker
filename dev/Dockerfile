FROM ubuntu:rolling

# build date
RUN echo `date` > /root/build_date.txt

# after openssl is ruby required packages
# after pgk-config is pypy required packages
RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    curl \
    vim \
    tmux \
    man \
    python3 \
    python3-dev \
    python3-venv \
    libpq-dev \
    postgresql-client \
    postgresql-client-common && \
    apt-get autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN yes | unminimize

RUN \
    curl -q "https://bootstrap.pypa.io/get-pip.py" -o "/root/get-pip.py" && \
    python3 /root/get-pip.py 

CMD ["/bin/bash"]
