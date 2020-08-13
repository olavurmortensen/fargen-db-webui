FROM python:3

RUN pip install Flask

ADD hello.py /
ENV FLASK_APP hello.py

ENTRYPOINT ["python3"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0", "--port", "80"]
