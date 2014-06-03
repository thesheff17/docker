#GENERIC Dockfile example 
FROM     ubuntu
MAINTAINER Dan Sheffner "Dan@Sheffner.org"


#changes the /etc/apt/source.list file to a local mirror
RUN echo '# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to' > /etc/apt/sources.list
RUN echo '# newer versions of the distribution.' >> /etc/apt/sources.list
RUN echo '' >> /etc/apt/sources.list
RUN echo 'deb http://192.168.1.5/ubuntu/ trusty main restricted' >> /etc/apt/sources.list
RUN echo 'deb-src http://192.168.1.5/ubuntu/ trusty main restricted' >> /etc/apt/sources.list
RUN echo '' >> /etc/apt/sources.list
RUN echo '## Major bug fix updates produced after the final release of the' >> /etc/apt/sources.list
RUN echo '## distribution.' >> /etc/apt/sources.list
RUN echo 'deb http://192.168.1.5/ubuntu/ trusty-updates main restricted' >> /etc/apt/sources.list
RUN echo 'deb-src http://192.168.1.5/ubuntu/ trusty-updates main restricted' >> /etc/apt/sources.list
RUN echo '' >> /etc/apt/sources.list
RUN echo "## Uncomment the following two lines to add software from the 'universe'" >> /etc/apt/sources.list
RUN echo '## repository.' >> /etc/apt/sources.list
RUN echo '## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu' >> /etc/apt/sources.list
RUN echo '## team. Also, please note that software in universe WILL NOT receive any' >> /etc/apt/sources.list
RUN echo '## review or updates from the Ubuntu security team.' >> /etc/apt/sources.list
RUN echo 'deb http://192.168.1.5/ubuntu/ trusty universe' >> /etc/apt/sources.list
RUN echo 'deb-src http://192.168.1.5/ubuntu/ trusty universe' >> /etc/apt/sources.list
RUN echo 'deb http://192.168.1.5/ubuntu/ trusty-updates universe' >> /etc/apt/sources.list
RUN echo 'deb-src http://192.168.1.5/ubuntu/ trusty-updates universe' >> /etc/apt/sources.list
RUN echo '' >> /etc/apt/sources.list
RUN echo '## N.B. software from this repository may not have been tested as' >> /etc/apt/sources.list
RUN echo '## extensively as that contained in the main release, although it includes' >> /etc/apt/sources.list
RUN echo '## newer versions of some applications which may provide useful features.' >> /etc/apt/sources.list
RUN echo '## Also, please note that software in backports WILL NOT receive any review' >> /etc/apt/sources.list
RUN echo '## or updates from the Ubuntu security team.' >> /etc/apt/sources.list
RUN echo '# deb http://192.168.1.5/ubuntu/ trusty-backports main restricted' >> /etc/apt/sources.list
RUN echo '# deb-src http://192.168.1.5/ubuntu/ trusty-backports main restricted' >> /etc/apt/sources.list
RUN echo '' >> /etc/apt/sources.list
RUN echo 'deb http://192.168.1.5/ubuntu/ trusty-security main restricted' >> /etc/apt/sources.list
RUN echo 'deb-src http://192.168.1.5/ubuntu/ trusty-security main restricted' >> /etc/apt/sources.list
RUN echo 'deb http://192.168.1.5/ubuntu/ trusty-security universe' >> /etc/apt/sources.list
RUN echo 'deb-src http://192.168.1.5/ubuntu/ trusty-security universe' >> /etc/apt/sources.list
RUN echo '# deb http://192.168.1.5/ubuntu/ trusty-security multiverse' >> /etc/apt/sources.list
RUN echo '# deb-src http://192.168.1.5/ubuntu/ trusty-security multiverse' >> /etc/apt/sources.list

# install
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y samba wget

#get config file
RUN rm /etc/samba/smb.conf
RUN cd /etc/samba/ && wget https://raw.githubusercontent.com/thesheff17/docker/master/samba/smb.conf
RUN useradd share01
RUN (echo share01; echo share01) | /usr/bin/smbpasswd -s -a share01

#setup
RUN mkdir /mnt/share01
RUN chmod 777 /mnt/share01

#ssh setup
#RUN apt-get install -y ssh vim
#RUN mkdir /var/run/sshd
#RUN useradd -m ubuntu -s /bin/bash
#RUN adduser ubuntu sudo
#RUN echo 'ubuntu:ubuntu'  |chpasswd

EXPOSE 135/tcp
EXPOSE 137/udp
EXPOSE 138/udp
EXPOSE 139/tcp
EXPOSE 445/tcp
#EXPOSE 22/tcp

#CMD    /usr/sbin/sshd -D

entrypoint ["/usr/sbin/smbd"]
cmd ["-F", "-S"]
