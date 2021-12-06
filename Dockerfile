FROM python:3.8
COPY . /var/www/
COPY ./conf/sources.list /etc/apt/
COPY ./conf/.pip /root/
COPY ./conf/.config /root/
WORKDIR /var/www/src
RUN apt-get update
RUN pip3 install poetry -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN cd Python && poetry config virtualenvs.create false && poetry install 
CMD [ "python3" ]