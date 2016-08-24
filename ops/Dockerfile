FROM centos:latest
MAINTAINER Arpit Srivastava <arpit2438735@gmail.com>

ENV APP_USER flask
ENV APP_ROOT /code
ENV PYTHONUNBUFFERED 1

RUN groupadd -r ${APP_USER} \
    && useradd -r -m \
    --home-dir ${APP_ROOT} \
    -s /usr/sbin/nologin \
    -g ${APP_USER} ${APP_USER}

# In order to set psycopg2 package need to install(postgresql-devel gcc)
RUN yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel && \
    yum install -y python-devel.x86_64 && \
    yum install -y postgresql-devel gcc&& \
    yum clean all
    
#CURL pip package for python
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

WORKDIR ${APP_ROOT}

#USER ${APP_USER}
#Copying all source file
COPY . ${APP_ROOT}/
RUN pip install -r requirement.txt
