FROM python:3

RUN pip install Flask

ADD app /app
ENV FLASK_APP /app

ENV FLASK_ENV development

ENTRYPOINT ["python3"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0", "--port", "80"]
