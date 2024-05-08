FROM python:alpine3.19

ADD ./requirements.txt /opt/segun_db/

WORKDIR /opt/segun_db/

RUN pip install -r requirements.txt

ADD . /opt/segun_db/

EXPOSE 8080
CMD python /opt/segun_db/app.py
