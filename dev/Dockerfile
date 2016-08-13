FROM ubuntu:16.04

MAINTAINER Dan Sheffner <Dan@Sheffner.com>

# bugs:
# tmux doesn't work some bug with the screen thing
# feel free to research and submit a patch

# helper ENV variables
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

# local.sources.list is a local mirror
# public.sources.list is a public mirror
# use whatever you have
COPY ./public.sources.list /etc/apt/sources.list
# COPY ./local.sources.list /etc/apt/sources.list

# updates
RUN apt-get update
RUN apt-get upgrade -y

# packages
RUN apt-get install -yq curl wget python-pip python-dev \
    git python3-pip python3-dev build-essential gcc vim-gnome \
    lsb-release mysql-client libpq-dev libjpeg-dev ffmpeg tmux \
    screen php-mcrypt php-mysql php php-cli pypy libffi-dev \
    libssl-dev openssl

# ruby requirements:
RUN apt-get install -yq zlib1g-dev libssl-dev libreadline-dev libyaml-dev \
    libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev \
    python-software-properties libgdbm-dev libncurses5-dev \
    automake libtool bison libffi-dev gawk libgmp-dev pkg-config

# couchbase client
RUN wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-2-amd64.deb
RUN dpkg -i couchbase-release-1.0-2-amd64.deb
RUN apt-get update
RUN apt-get install -yq libcouchbase-dev libcouchbase2-bin
RUN rm couchbase-release-1.0-2-amd64.deb

# pip upgrades
RUN pip install --upgrade pip
RUN pip3 install --upgrade pip

# python pip
RUN pip install virtualenvwrapper boto3 couchbase django django-environ django-secure \
    whitenoise django-braces django-crispy-forms django-floppyforms django-model-utils \
    pillow django-allauth psycopg2 unicode-slugify django-autoslug pytz django-redis \
    redis pymysql libsass django-compressor django-sass-processor django-debug-toolbar \
    django_extensions django-nose django-axes python-dateutil pyflakes coverage sphinx \
    werkzeug django-test-plus factory_boy ipdb sqlalchemy pycodestyle

# python3 pip
RUN pip3 install boto3 couchbase django django-environ django-secure whitenoise \
    django-braces django-crispy-forms django-floppyforms django-model-utils \
    pillow django-allauth psycopg2 unicode-slugify django-autoslug pytz django-redis \
    redis pymysql libsass django-compressor django-sass-processor django-debug-toolbar \
    django_extensions django-nose django-axes python-dateutil pyflakes coverage sphinx \
    werkzeug django-test-plus factory_boy ipdb sqlalchemy pycodestyle

# flask
RUN pip install flask flask-bcrypt flask-login flask-migrate flask-sqlalchemy flask-script \
    flask-testing flask-wtf mako markupsafe wtforms alembic gunicorn itsdangerous py-bcrypt

# flask
RUN pip3 install flask flask-bcrypt flask-login flask-migrate flask-sqlalchemy flask-script \
    flask-testing flask-wtf mako markupsafe wtforms alembic gunicorn itsdangerous py-bcrypt

# compile python3 from source
# not needed until versions are different between distro and python.org
# WORKDIR /root/
# RUN wget --quiet https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
# RUN tar -xf Python-3.5.1.tar.xz
# WORKDIR /root/Python-3.5.1/
# RUN ./configure
# RUN make -j8
# RUN make install

# go
RUN wget --quiet https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.6.2.linux-amd64.tar.gz
RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> /root/.bashrc
RUN rm go1.6.2.linux-amd64.tar.gz

# go compile from source
RUN mkdir /root/git/
WORKDIR /root/git/
RUN git clone https://github.com/golang/go.git
WORKDIR /root/git/go/src/
RUN GOROOT_BOOTSTRAP=/usr/local/go/ GOOS=linux GOARCH=amd64 ./bootstrap.bash

# ruby install
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby
RUN curl -sSL https://get.rvm.io | bash -s stable --rails
RUN gem install bundler

# vim setup
RUN mkdir -p /root/.vim/autoload /root/.vim/bundle /root/.vim/colors/ /root/.vim/ftplugin/
RUN curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
WORKDIR /root/.vim/bundle/
RUN git clone https://github.com/tpope/vim-sensible.git
RUN git clone https://github.com/kien/ctrlp.vim.git
RUN git clone https://github.com/scrooloose/nerdtree
RUN git clone https://github.com/Lokaltog/vim-powerline.git
RUN git clone https://github.com/jistr/vim-nerdtree-tabs.git
RUN git clone https://github.com/davidhalter/jedi-vim.git
WORKDIR /root/.vim/colors/
RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/wombat256mod.vim
WORKDIR /root/.vim/ftplugin/
RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/python_editing.vim
WORKDIR /root/
RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/vimrc
RUN mv vimrc .vimrc

# tmux files
# WORKDIR /root/
# RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/tmux_virtical2.sh
# RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/tmux_horizontal3.sh

# git clone repo
WORKDIR /root/git/
RUN git clone https://github.com/kubernetes/kubernetes.git

# cleanup
RUN apt-get autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# switch back working dir
WORKDIR /root/

# command to run
CMD ["/bin/bash"]
