FROM ubuntu:16.04

MAINTAINER Dan Sheffner <Dan@Sheffner.com>

# local.sources.list is a local mirror
# public.sources.list is a public mirror
COPY ./local.sources.list /etc/apt/sources.list

# helper ENV variables
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV EDITOR vim
ENV SHELL bash

# build date
RUN echo `date` > /root/build_date.txt

# after openssl is ruby required packages
# after pgk-config is pypy required packages
RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -yq curl wget python-pip python-dev \
    git python3-pip python3-dev build-essential gcc vim \
    lsb-release mysql-client libpq-dev libjpeg-dev ffmpeg tmux \
    screen php-mcrypt php-mysql php php-cli pypy libffi-dev \
    libssl-dev openssl openjdk-8-jdk libmemcached-dev nodejs npm \
    zlib1g-dev libssl-dev libreadline-dev libyaml-dev \
    libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev \
    python-software-properties libgdbm-dev libncurses5-dev \
    automake libtool bison libffi-dev gawk libgmp-dev pkg-config \
    gcc make libffi-dev pkg-config libz-dev libbz2-dev tcl-dev \
    libsqlite3-dev libncurses-dev libexpat1-dev libssl-dev pypy mercurial \
    libgc-dev liblzma-dev tcl8.4-dev tk8.4-dev tk-dev net-tools man && \
    apt-get autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# couchbase client
RUN wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-2-amd64.deb
RUN dpkg -i couchbase-release-1.0-2-amd64.deb
RUN apt-get update
RUN apt-get install -yq libcouchbase-dev libcouchbase2-bin
RUN rm couchbase-release-1.0-2-amd64.deb

# pip upgrades
RUN pip3 install --upgrade pip && pip2 install --upgrade pip

# virtualenv
RUN pip2 install virtualenvwrapper virtualenv && \
    cd /root/ && \
    /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh && \
    mkvirtualenv --python=/usr/bin/python3 venv3 && \
    mkvirtualenv venv2" && \
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> /root/.bashrc

# these files get messed up for some reason venv3
RUN \
    echo "#!/bin/bash" > /root/.virtualenvs/preactivate && \
    echo "# This hook is run before every virtualenv is activated." >> /root/.virtualenvs/preactivate && \
    echo "# argument: environment name " >> /root/.virtualenvs/preactivate && \
    echo "#!/bin/bash" > /root/.virtualenvs/venv3/bin/preactivate && \
    echo "# This hook is run before this virtualenv is activated." >> /root/.virtualenvs/venv3/bin/preactivate

# these files get messed up for some reason venv2
RUN \
    echo "#!/bin/bash" > /root/.virtualenvs/preactivate && \
    echo "# This hook is run before every virtualenv is activated." >> /root/.virtualenvs/preactivate && \
    echo "# argument: environment name " >> /root/.virtualenvs/preactivate && \
    echo "#!/bin/bash" > /root/.virtualenvs/venv2/bin/preactivate && \
    echo "# This hook is run before this virtualenv is activated." >> /root/.virtualenvs/venv2/bin/preactivate

# python3 pip
RUN \
   /bin/bash -c " source /root/.virtualenvs/venv3/bin/activate && \
   pip3 install boto3 django django-environ django-secure whitenoise \
    django-braces django-crispy-forms django-floppyforms django-model-utils \
    pillow django-allauth psycopg2 unicode-slugify django-autoslug pytz django-redis \
    redis pymysql libsass django-compressor django-sass-processor django-debug-toolbar \
    django_extensions django-nose django-axes python-dateutil pyflakes coverage sphinx \
    werkzeug django-test-plus factory_boy ipdb sqlalchemy bpython pylibmc jupyter"

# python3 flask
RUN /bin/bash -c " source /root/.virtualenvs/venv3/bin/activate && \
    pip3 install flask flask-bcrypt flask-login flask-migrate flask-sqlalchemy flask-script \
    flask-testing flask-wtf mako markupsafe wtforms alembic gunicorn itsdangerous py-bcrypt "

# python2 pip
RUN \
   /bin/bash -c " source /root/.virtualenvs/venv2/bin/activate && \
   pip install boto3 django django-environ django-secure whitenoise \
    django-braces django-crispy-forms django-floppyforms django-model-utils \
    pillow django-allauth psycopg2 unicode-slugify django-autoslug pytz django-redis \
    redis pymysql libsass django-compressor django-sass-processor django-debug-toolbar \
    django_extensions django-nose django-axes python-dateutil pyflakes coverage sphinx \
    werkzeug django-test-plus factory_boy ipdb sqlalchemy bpython pylibmc jupyter "

# python2 flask
RUN /bin/bash -c " source /root/.virtualenvs/venv2/bin/activate && \
    pip install flask flask-bcrypt flask-login flask-migrate flask-sqlalchemy flask-script \
    flask-testing flask-wtf mako markupsafe wtforms alembic gunicorn itsdangerous py-bcrypt "

# compile python3 from source
WORKDIR /root/
RUN wget --quiet https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
RUN tar -xf Python-3.6.3.tar.xz
WORKDIR /root/Python-3.6.3/
# RUN ./configure --enable-loadable-sqlite-extensions
RUN ./configure --enable-optimizations --enable-loadable-sqlite-extensions
RUN make -j9
RUN make install

# go
RUN wget --quiet https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.9.1.linux-amd64.tar.gz
RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> /root/.bashrc
RUN echo 'export GOBIN=/root/go/bin' >> /root/.bashrc
RUN echo 'export GOPATH=/root/go/bin' >> /root/.bashrc
RUN rm go1.9.1.linux-amd64.tar.gz

# vim modules
RUN mkdir -p /root/.vim/autoload /root/.vim/bundle /root/.vim/colors/ /root/.vim/ftplugin/
RUN curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
WORKDIR /root/.vim/bundle/
RUN git clone https://github.com/tpope/vim-sensible.git
RUN git clone https://github.com/ctrlpvim/ctrlp.vim.git

# project died
# RUN git clone https://github.com/kien/ctrlp.vim.git
RUN git clone https://github.com/scrooloose/nerdtree
RUN git clone https://github.com/Lokaltog/vim-powerline.git
RUN git clone https://github.com/jistr/vim-nerdtree-tabs.git
RUN git clone https://github.com/python-mode/python-mode.git
# RUN git clone --recursive https://github.com/davidhalter/jedi-vim.git
RUN git clone https://github.com/fatih/vim-go.git
RUN git clone https://github.com/vim-syntastic/syntastic.git

WORKDIR /root/.vim/colors/
RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/wombat256mod.vim
WORKDIR /root/.vim/ftplugin/
RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/python_editing.vim
WORKDIR /root/
RUN wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/vimrc2
RUN mv vimrc2 .vimrc

# go packages
RUN export PATH=$PATH:/usr/local/go/bin && \
    export GOPATH=/root/go/bin && \
    export GOBIN=/root/go/bin && \
    go get github.com/nsf/gocode && \
    go get github.com/alecthomas/gometalinter && \
    go get golang.org/x/tools/cmd/goimports && \
    go get golang.org/x/tools/cmd/guru && \
    go get golang.org/x/tools/cmd/gorename && \
    go get github.com/golang/lint/golint && \
    go get github.com/rogpeppe/godef && \
    go get github.com/kisielk/errcheck && \
    go get github.com/jstemmer/gotags && \
    go get github.com/klauspost/asmfmt/cmd/asmfmt && \
    go get github.com/fatih/motion && \
    go get github.com/zmb3/gogetdoc && \
    go get github.com/josharian/impl

# ruby install
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby
RUN curl -sSL https://get.rvm.io | bash -s stable --rails
# RUN gem install bundler

# go compile from source
RUN mkdir /root/git/
WORKDIR /root/git/
RUN git clone https://github.com/golang/go.git
WORKDIR /root/git/go/src/
RUN GOROOT_BOOTSTRAP=/usr/local/go/ GOOS=linux GOARCH=amd64 ./bootstrap.bash

# pypy from source
# This keeps erorring out.  If want to sumbit a patch please do.
RUN \
    cd /root/ && \
    hg clone https://bitbucket.org/pypy/pypy && cd pypy/pypy/goal && \
    pypy ../../rpython/bin/rpython -Ojit targetpypystandalone && \
    ln -s /root/pypy/pypy/goal/pypy-c /usr/bin/pypy-c

# pypy rpython/bin/rpython --opt=jit pypy/goal/targetpypystandalone.py
# cp -r /usr/include/tcl8.4/* /usr/include/ && \
# make share location
RUN mkdir -p /root/git/

# tmux setup
# ADD tmuxinator /root/.tmuxinator
RUN echo 'set-option -g default-shell /bin/bash' > /root/.tmux.conf

# Copy over samples
COPY ./webserver.go /root/bin/
COPY ./webserver.py /root/bin/
COPY ./versions.sh /root/bin/

# put back public mirror
COPY ./public.sources.list /etc/apt/sources.list

# gem tmux no longer used
# CMD ["/usr/local/bin/tmuxinator", "start", "default"]

# CMD ["/bin/bash"]
WORKDIR /root/
CMD ["/usr/bin/tmux"]
