FROM python:3.8

WORKDIR /P13

ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV DEBUG=True

ADD . /P13

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /P13

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT