FROM bitnami/jenkins:2.332.3-debian-11-r3

USER root
RUN apt update
RUN apt-get install build-essential \
	zlib1g-dev \
	libncurses5-dev \
	libgdbm-dev \
	libnss3-dev \
	libssl-dev \
	libsqlite3-dev \
	libreadline-dev \
	libffi-dev wget \
	libbz2-dev \
  jq \
	bc \
  dnsutils \
	groff \
 less -y

# install k6
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
RUN echo "deb https://dl.k6.io/deb stable main" | tee /etc/apt/sources.list.d/k6.list
RUN apt update
RUN apt-get install k6

# install python 3.7.4
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
RUN tar -xf Python-3.7.4.tgz
RUN ./Python-3.7.4/configure --enable-optimizations

RUN make altinstall
RUN rm -rf ./Python-3.7.4
RUN rm ./Python-3.7.4.tgz

WORKDIR /usr/local/bin/
RUN ln -s pip3.7 pip
RUN ln -s python3.7 python3
RUN ln -s python3.7 python

ENTRYPOINT [ "/opt/bitnami/scripts/jenkins/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/jenkins/run.sh" ]

