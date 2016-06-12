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
RUN apt-get install -yq curl wget git python3-pip python3-dev \
    build-essential gcc vim-gnome lsb-release mysql-client \
    libpq-dev libjpeg-dev ffmpeg tmux screen libffi-dev

# pip upgrades
RUN pip3 install --upgrade pip

# python3 pip
RUN pip3 install boto3 django django-environ django-secure whitenoise \
    django-braces django-crispy-forms django-floppyforms django-model-utils \
    pillow django-allauth psycopg2 unicode-slugify django-autoslug pytz django-redis \
    redis pymysql libsass django-compressor django-sass-processor django-debug-toolbar \
    django_extensions django-nose django-axes python-dateutil pyflakes coverage sphinx \
    werkzeug django-test-plus factory_boy ipdb sqlalchemy pycodestyle

# flask
RUN pip3 install flask flask-bcrypt flask-login flask-migrate flask-sqlalchemy flask-script \
    flask-testing flask-wtf mako markupsafe wtforms alembic gunicorn itsdangerous py-bcrypt

# go
RUN wget --quiet https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.6.2.linux-amd64.tar.gz
RUN echo 'export PATH=$PATH:/usr/local/go/bin' >> /root/.bashrc
RUN rm go1.6.2.linux-amd64.tar.gz

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

# cleanup
RUN apt-get autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# command to run
CMD ["/bin/bash"]
