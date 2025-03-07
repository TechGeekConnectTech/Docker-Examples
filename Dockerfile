FROM python:3.9

WORKDIR /myapp

COPY ./mysqlconnect.py .
RUN pip install pymysql
RUN pip install cryptography

CMD ["python","mysqlconnect.py"]