FROM ubuntu:14.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yqq install \
    build-essential python-pip software-properties-common \
    openjdk-7-jdk && \
    add-apt-repository ppa:fkrull/deadsnakes && \
    apt-get update

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

EXPOSE 5000

RUN DEBIAN_FRONTEND=noninteractive apt-get -yqq install \
    python2.5 python2.6 python2.7 python3.1 python3.2 python3.3 python3.4 python3.6

ADD http://search.maven.org/remotecontent?filepath=org/python/jython-installer/2.7-b4/jython-installer-2.7-b4.jar /tmp/jython-installer-2.7-b4.jar

RUN mkdir -p /opt
ADD https://bitbucket.org/pypy/pypy/downloads/pypy3-2.4.0-linux64.tar.bz2 /tmp/
RUN cd /opt && tar -xf /tmp/pypy3-2.4.0-linux64.tar.bz2
ADD https://bitbucket.org/pypy/pypy/downloads/pypy-2.5.0-linux64.tar.bz2 /tmp/
RUN cd /opt && tar -xf /tmp/pypy-2.5.0-linux64.tar.bz2

RUN java -jar /tmp/jython-installer-2.7-b4.jar -d /opt/jython-2.7-b4 -s -t all
ENV PATH /opt/jython-2.7-b4/bin:$PATH
RUN jython

ENV PATH /opt/pypy-2.5.0-linux64/bin:/opt/pypy3-2.4.0-linux64/bin:$PATH

ENV PYTHON_BUILD_DOCKER=true

RUN apt-get install python3.6

RUN apt install python3-pip -y --upgrade

COPY . /app

RUN chmod +x ./build_and_test.sh

ENTRYPOINT [ "./build_and_test.sh" ]