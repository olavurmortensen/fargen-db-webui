FROM python:3

COPY requirements.txt /
RUN pip install -r requirements.txt

ADD app /app
ENV FLASK_APP /app

ENV FLASK_ENV development

ENTRYPOINT ["python3"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0", "--port", "80"]
