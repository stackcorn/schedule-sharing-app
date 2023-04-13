FROM python:3.9.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/

COPY build.sh /usr/bin/
RUN chmod +x /usr/bin/build.sh
ENTRYPOINT ["build.sh.sh"]
EXPOSE 3000

CMD ["python" "manage.py" "runserver" "0.0.0.0:8000"]