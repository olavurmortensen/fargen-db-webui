FROM python:3

RUN pip install Flask

ADD app /app
ENV FLASK_APP /app

# FIXME: for testing, remove this.
RUN mkdir /html_test
ADD test/html/linkseq-main-hboc-all.html /html_test

ENV FLASK_ENV development

ENTRYPOINT ["python3"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0", "--port", "80"]
