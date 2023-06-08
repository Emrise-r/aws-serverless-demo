FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt /tmp/
COPY ./source/server/* ./

RUN python -m pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt

CMD python --file simple_auth_server.py