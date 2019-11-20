From python:3

WORKDIR ./

ADD . /app

WORKDIR /app

#RUN apk add --update bash
#RUN apk add build-base
RUN pip install --upgrade pip
RUN python setup.py install

CMD ["/bin/bash"]
