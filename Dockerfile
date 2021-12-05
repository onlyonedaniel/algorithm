FROM python:3.8
COPY . /var/www/
COPY ./conf/sources.list /etc/apt/
COPY ./conf/.pip /root/
WORKDIR /var/www/src
RUN apt-get update
RUN pip3 install poetry && cd src/Python && poetry config virtualenvs.create false && poetry install 
CMD [ "python3" ]