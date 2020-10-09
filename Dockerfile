FROM python:3
MAINTAINER suvern
ENV active prod
RUN mkdir -p src
COPY . src
WORKDIR src
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 11000
ENTRYPOINT python3 manage.py runserver 0.0.0.0:11000