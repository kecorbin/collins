FROM python:2.7-alpine
ADD . /opt/plugin
WORKDIR /opt/plugin
RUN pip install -r requirements.txt
CMD python plugin.py

