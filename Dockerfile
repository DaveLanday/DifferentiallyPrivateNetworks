From python:3

WORKDIR ./

ADD . /app

WORKDIR /app

# Install Pip and Run setup.py
RUN pip install --upgrade pip
RUN python setup.py install

# Install jupyter
RUN pip install jupyter

CMD ["/bin/bash"]
