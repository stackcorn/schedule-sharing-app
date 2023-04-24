FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt


RUN chmod a+x build.sh
ENTRYPOINT [ "./build.sh" ]
EXPOSE 8000
CMD [ "gunicorn", "config.wsgi:application" ]